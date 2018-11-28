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
#define Sort(a) sort(All(a))
#define Eo(x) { cerr << #x << " = " << (x) << endl; } 
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }


#define MAX 1001
int ha[MAX];
int hb[MAX];
void solve(int test)
{
  int N;
	  int res=0;
	cin>>N;
	Rep(i,N)
		{
			cin>>ha[i]>>hb[i];
		}
	for(int i=0;i<N;i++)
		for(int j=i+1;j<N;j++)
			{
				if((ha[i]>ha[j])&(hb[i]<hb[j]))
					res++;
			if((ha[i]<ha[j])&(hb[i]>hb[j]))
					res++;
			}

	cout<<"Case #"<<test<<": "<<res<<endl;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	cin>>N;
	char buf[90];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}