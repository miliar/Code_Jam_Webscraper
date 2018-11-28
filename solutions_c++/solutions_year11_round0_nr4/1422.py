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
#ifdef DBG
#define see(x) (cerr<<"[Line : "<< __LINE__<<"] : "<<#x<<"="<<x<<endl)
#define se(x) cerr<<x<<" "
#else
#define see(x) //
#define se(x) //
#endif
template<class T>T& ls(T& a,T b)
{ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b)
{ if(b>a) a=b; return a;}
inline int to_i(const string& s)
{int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n)
{char buf[32];sprintf(buf,"%d",n);return string(buf);}
#define maxn  12030
int n,m;
int a[maxn];
int flag[maxn];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif
    int i,j,k,t;
	scanf("%d", &t);
	int cas=0;
	while(t--)
	{
		scanf("%d", &n);
		double ans=0;
		for(i=1; i<=n ;i++)
		{	
			scanf("%d", &a[i]);
			if(a[i]==i)
			ans++;
		}
		ans=n-ans;
		printf("Case #%d: %.6lf\n",++cas,ans);
	}
}
