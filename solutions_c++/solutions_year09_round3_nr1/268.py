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

int lm[65];
void solve(int test)
{

	ll num[12];
	ll alph[29];
	char buf[65];
	gets(buf);
	memset(num,-1,sizeof(num));
	memset(alph,-1,sizeof(alph));
	int size=strlen(buf);
	ll va[65];
	ll current=0;
	For(i,0,size-1)
	{
		if(('a'<=buf[i])&&(buf[i]<='z'))
		{
			if(alph[buf[i]-'a']==-1)
			{
				va[i]=lm[current];
				alph[buf[i]-'a']=lm[current];
				current++;
			}
			else
			{
				va[i]=alph[buf[i]-'a'];
			}
		}
				if(('0'<=buf[i])&&(buf[i]<='9'))
		{
			if(num[buf[i]-'0']==-1)
			{
				va[i]=lm[current];
				num[buf[i]-'0']=lm[current];
				current++;
			}
			else
			{
				va[i]=num[buf[i]-'0'];
			}
		}
	}
	ll base;
	if(current==1)
		base=2;
	else
		base=current;
	ll ans=0;
	For(i,0,size-1)
	{
		ans=ans*base+va[i];
	}
	fprintf(stderr,"test=%d\n",test);
	cout<<"Case #"<<test<<": "<<ans<<endl;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	lm[0]=1;
	lm[1]=0;
	For(i,2,64)
	{
		lm[i]=i;
	}
	cin>>N;
	char buf[50];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}