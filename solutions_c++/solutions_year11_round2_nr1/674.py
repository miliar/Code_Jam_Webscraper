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
#define maxn  110
int n,m;
char s[110][110];
int g[maxn][maxn];
int num[maxn],nnum[maxn];
int win[maxn],wwin[maxn];
double p[maxn],op[maxn],oop[maxn],ans[maxn];
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
		memset(s,0,sizeof(s));
		memset(g,0,sizeof(g));
		memset(p,0,sizeof(p));
		memset(op,0,sizeof(op));
		memset(oop,0,sizeof(oop));
		memset(win,0,sizeof(win));
		memset(num,0,sizeof(num));
		memset(ans,0,sizeof(ans));
		printf("Case #%d:\n",++cas);
		scanf("%d",&n);
		for(i=0; i<n; i++)
		{
			scanf("%s",&s[i][0]);
			for(j=0; j<n; j++)
			{
				if(s[i][j]=='1')
				{
					num[i]++;
					win[i]++;
					g[i][j]=1;
				}
				else if(s[i][j]=='0')
				{	
					num[i]++;
					g[i][j]=-1;
				}
				else
				{
					g[i][j]=0;	
				}
			}
			if(num[i]==0)	
				p[i]=0;
			else
				p[i]=(double)win[i]/num[i];
			ans[i]+=0.25*p[i];
		}
		
		for(i=0; i<n; i++)
		{ 
			memset(wwin,0,sizeof(wwin));
			memset(nnum,0,sizeof(nnum));
			for(j=0;j<n;j++)
			{
				if(j==i)	continue;
				for(k=0; k<n;k++)
				{
					if(k==i)	continue;
					if(g[j][k]==1)
					{
						wwin[j]++;
						nnum[j]++;
					}			
					else if(g[j][k]==-1)
					{
						nnum[j]++;
					}					
				}
				if(nnum[j]==0)	
					p[j]=0;
				else
					p[j]=(double)wwin[j]/nnum[j];
			}
			for(j=0; j<n; j++)
			if(g[i][j]!=0)
				op[i]+=p[j];
				
		
			if(num[i]!=0)
				op[i]/=num[i];
			else
				op[i]=0;	
		
			ans[i]+=0.5*op[i];
		}
		for(i=0; i<n; i++)
		{
			for(j=0; j<n;j++)
			if(g[i][j]!=0)
			{
				oop[i]+=op[j];
			}
			if(num[i]!=0)
				oop[i]/=(double)num[i];
			else
				oop[i]=0;
			ans[i]+=0.25*oop[i];
		}
		
		for(i=0; i<n; i++)
		{
			printf("%.6lf\n",ans[i]);
		}
	}
}
