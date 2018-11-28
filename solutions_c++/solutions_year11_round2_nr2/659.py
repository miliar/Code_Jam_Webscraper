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
#define eps (1e-7)
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
#define maxn  1100
int c,d;

double a[maxn];
int cnt=0;
double b[maxn];
int solve(double x)
{
	int i,j;
	b[0]=a[0]-x;
	for(i=1; i<cnt; i++)
	{
		double tp=b[i-1]+d;
		double dis=fabs(tp-a[i]);
		if(dis<=x)
		{
			b[i]=tp;
		}
		else
		{
			if(a[i]<tp)
				return 0;
			else
				b[i]=a[i]-x;
		}
	}
	return 1;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif
    int i,j,k,t,cas=0;
    scanf("%d", &t);
	while(t--)
	{
		cnt=0;
		printf("Case #%d: ",++cas);
		scanf("%d%d", &c,&d);
		int p,v;
		for(i=0; i<c; i++)
		{
			scanf("%d%d", &p,&v);
			while(v--)
			a[cnt++]=p;
		}
		sort(a,a+cnt);
		double r=1000000;
		double l=0;
		double ans=0;
		while(r-l>eps)
		{
			double mid=(l+r)/2;
			if(solve(mid))
			{
				ans=mid;
				r=mid;
			}
			else
			{
				l=mid;
			}
		}
		printf("%.6lf\n",ans);
	}
}
