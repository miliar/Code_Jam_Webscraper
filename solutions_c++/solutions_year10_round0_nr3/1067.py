#define _CRT_SECURE_NO_DEPRECATE
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double zero=1e-6;
const double limit=1e8;
#define SZ(x) (int(x.size()))
typedef long long int64;
typedef unsigned long long uint64;
template<class T> T sqr(T x) {return x*x;}
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(T a,T b){ return a*(b/gcd(a,b));}
int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t;return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
template<class T> string toString(T x){ ostringstream sout; sout<<x; return sout.str();}


#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("in.txt");
#define cin inf
#endif

ofstream outf("out.txt");
#define cout outf


int cnt[1000];
int next[1000];

int t,n,k,r;
int g[1000];
int c(int s)
{
	if(cnt[s] != -1)
		return cnt[s];

	int left = k;
	int now = s;
	if(left >= g[now])
	{
		left -= g[now];
		if ( ++now == n)
			now = 0;

		while(left >= g[now] && now!= s)
		{
			left -= g[now];
			if( ++now >= n)
			{
				now=0;
			}
		}
	}
	left = k - left;
	next[s] = now;
	cnt[s] = left;
	return left;
}
int main(int argc, char* argv[])
{
	cin>>t;
	for(int it=0;it<t;it++)
	{
		cout<<"Case #"<<it+1<<": ";

		memset(cnt,-1,sizeof(cnt));
		memset(next,-1,sizeof(next));
		cin>>r>>k>>n;
		
		for(int i=0;i<n;i++)
			cin>>g[i];

		long long ret= 0;
		int now = 0;
		for(int i=0;i<r;i++)
		{
			ret += c(now);
			now = next[now];
		}
		cout<<ret<<endl;
	}
	return 0;
}
