#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<assert.h>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
const int inf=1000000000;
const double pi=acos(-1.0);
#define eps (1e-15)
#define L(x) ((x)<<1)
#define R(x) ((x)<<1|1)
#define see(x)(cerr<<"[line:"<<__LINE__<<" "<<#x<<" "<<x<<endl)
#define se(x) cerr<<x<<" "
template<class T>T& ls(T& a,T b)
{ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b)
{ if(b>a) a=b; return a;}
inline int to_i(const string& s)
{int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n)
{char buf[32];sprintf(buf,"%d",n);return string(buf);}
#define maxn  1030
int n,m;

int gcd(int b,int a)
{
	if(b==0)	return a;
	return gcd(a%b,b);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif
    int i,j,k;
	int t,cas=1;
	scanf("%d", &t);
	for(; cas<=t; cas++)
	{
		int pd,pg;
		int ans=0;
		scanf("%d%d%d", &n,&pd,&pg);
		if(pd==100)
		{
			if(pg==0)
				ans=0;
			else
				ans=1;
		}
		else if(pd==0)
		{
			if(pg==100)
				ans=0;
			else ans=1;
		}
		else
		{
			if(pg==100 ||pg==0)
				ans=0;
			else
			{
				int d=gcd(pd,100);
			//printf("%d %d %d\n",pd,100,d);
				int tp=100/d;
				if(tp<=n)
					ans=1;
				else
					ans=0;
			}
		}
		printf("Case #%d: ", cas);
		if(ans)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
}
