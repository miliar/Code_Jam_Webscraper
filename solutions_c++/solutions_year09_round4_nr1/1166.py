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
#include <string>
#include <vector>

#include <cstring>
#include <cassert>

#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
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

int m[41];
int v[41];
char buf[51];
void solve(int test)
{
	memset(v,0,sizeof(v));
	int N;
	cin>>N;
	gets(buf);
	For(i,1,N)
	{
		char c;
		gets(buf);
		istringstream isin(buf);
		For(j,1,N)
		{
			isin>>c;
			if(c=='1')
				v[i]=j;
		}		


	}
	int ans=0;
    For(i,1,N)
	{
		m[i]=v[i]-i;
	}
	while(1)
	{
		int start=1;
		For(i,1,N)
		{
			if(m[i]<=0)
				start++;
			else
				break;
		}
		if(start==(N+1))
			break;
		int end=start+m[start];
		int dest;
		For(i,start+1,N)
		{
			if((i+m[i])<=start)
			{
				dest=i;
				break;
			}
		}
		Ford(i,dest,start+1)
			m[i]=m[i-1]-1;
		m[start]=0;

		ans+=dest-start;
	}

	fprintf(stderr,"test=%d\n",test);
	cout<<"Case #"<<test<<": "<<ans<<endl;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	cin>>N;
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}