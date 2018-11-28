#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }



int ans=0;

int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int totcase;
	cin>>totcase;
	For(test,1,totcase)
	{
		int cap,roud,group;
		cin>>roud>>cap>>group;
		vector<int> cache;
		Rep(i,group)
			{
				int g;
				cin>>g;
				cache.push_back(g);
			}
		vector<int> next(group,-1);
		vector<int> visit(group,-1);
		vector<int> cancap(group,0);
		int start=0;
		int cur=0;
	  while(visit[start]==-1)
			{
			visit[start]=cur;
			cur++;
			int tot=0;
			int i;
			for(i=start;i<group;i++)
				{
					tot+=cache[i];
					if(tot>cap)
						{
							tot-=cache[i];
							break;
						}
				}
			if(i==group)
			for(i=0;i<start;i++)
				{
					tot+=cache[i];
					if(tot>cap)
						{
							tot-=cache[i];
							break;
						}
				}
			if(i==group)
				i=0;
			next[start]=i;
			cancap[start]=tot;
			start=i;
			}
		long long res=0;
    int cyc=cur-visit[start];
    if((roud-visit[start])>=cyc)
			{
				long long tot=0;
				tot+=cancap[start];
				int i=next[start];
				while(i!=start)
					{
						tot+=cancap[i];
						i=next[i];
					}
				res+=tot*((roud-visit[start])/cyc);
				roud=(roud-visit[start])%cyc;
				roud+=visit[start];
			}
		int n=0;
		while(roud)
			{
				res+=cancap[n];
				n=next[n];			
				roud--;
			}

			cout<<"Case #"<<test<<": "<<res<<endl;
	}
}

