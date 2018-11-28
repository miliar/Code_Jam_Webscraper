#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int d[12][1100];
int dd[12];
int ok[1100];
bool g[1100][1100];
int n,m,ans;
bool check(int a,int b)
{
	int i;
	for(i=0;i<m;i++)
	{
		if(i>0)
		{
			if((a&(1<<i))&&(b&(1<<(i-1))))return false;
		}
		if(i+1<m)
		{
			if((a&(1<<i))&&(b&(1<<(i+1))))return false;
		}
	}
	return true;
}
bool ook(int t)
{
	int i;
	for(i=1;i<m;i++)
		if((t&(1<<i))&&(t&(1<<(i-1))))return false;
	return true;
}
int countbit(int t){return t?countbit(t&(t-1))+1:0;}
int main()
{
	int ii,cs,css,i,j,up;
	char t[100];
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		memset(d,0,sizeof(d));
		memset(dd,0,sizeof(dd));
		memset(ok,0,sizeof(ok));
		memset(g,0,sizeof(g));
		ans=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",t);
			dd[i]=0;
			for(j=0;j<m;j++)
				if(t[j]!='x')dd[i]=dd[i]*2+1;
				else dd[i]*=2;
		}
		up=1<<m;
		for(i=0;i<up;i++)
			ok[i]=ook(i);
		for(i=0;i<up;i++)
			for(j=0;j<up;j++)
				g[i][j]=check(i,j);
		for(i=0;i<up;i++)
			if((dd[0]&i)==i&&ok[i])d[0][i]=countbit(i);
			else d[0][i]=0;
		for(ii=1;ii<n;ii++)
			for(i=0;i<up;i++)
			{
				for(j=0;j<up;j++)
					if(ok[i]&&ok[j]&&g[i][j]&&(dd[ii]&j)==j)
					{
						d[ii][j]>?=d[ii-1][i]+countbit(j);
					}
					else d[ii][j]>?=d[ii-1][i];
			}
		for(ans=0,i=0;i<up;i++)
			ans>?=d[n-1][i];
		printf("Case #%d: %d\n",css,ans);
	}
	return 0;
}
