
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
typedef long long lld;
using namespace std;
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME))
#define MAX 0x7f7f7f7f
#define N 40
char f[N][N];
int mp[N][N];
int m,n;
int flag[N][N];
int ans[N];
bool check(int x,int y,int len)
{
	for(int i=x;i<x+len;i++)
	{
		for(int j=y;j<y+len;j++)
		{
			if(flag[i][j]==1)
			{
				return 0;
			}
		}
	}
	for(int i=y+1;i<y+len;i++)
	{
		if(mp[x][i]==mp[x][i-1])
		return 0;
	}
	for(int i=x+1;i<x+len;i++)
	{
		for(int j=y;j<y+len;j++)
		{
			if(mp[i][j]==mp[i-1][j])
			return 0;
		}
	}
	return 1;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
	int T,csn=1;
	scanf("%d",&T);
	int num;
	while(T--)
	{
		memset(mp,0,sizeof(mp));
		scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++)
		{
			scanf("%s",f[i]);
			for(int j=0;j<n/4;j++)
			{
				if(f[i][j]>='0'&&f[i][j]<='9')
				{
					num=f[i][j]-'0';
				}
				else
				{
					num=f[i][j]-'A'+10;
				}
				if((1&num))
				mp[i][j*4+3]=1;
				if((2&num))
				mp[i][j*4+2]=1;
				if((4&num))
				mp[i][j*4+1]=1;
				if((8&num))
				mp[i][j*4+0]=1;
			}
		}
//		for(int i=0;i<m;i++)
//		{
//			for(int j=0;j<n;j++)
//			{
//				cout<<mp[i][j];
//			}
//			cout<<endl;
//		}
		memset(ans,0,sizeof(ans));
		memset(flag,0,sizeof(flag));
		for(int len=min(m,n);len>=2;len--)
		{
			for(int i=0;i<m;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(flag[i][j]==1)
					continue;
					if(check(i,j,len))
					{
						ans[len]++;
						for(int i1=i;i1<i+len;i1++)
						{
							for(int j1=j;j1<j+len;j1++)
							{
								flag[i1][j1]=1;
							}
						}
					}
				}
			}
		}
		int tot=0;
		ans[1]=m*n;
		for(int i=2;i<=min(m,n);i++)
		{
			ans[1]-=ans[i]*i*i;
		}
		for(int i=1;i<=min(m,n);i++)
		{
			if(ans[i]!=0)
			{
				tot++;
			}
		}
		printf("Case #%d: %d\n",csn++,tot);
		for(int i=min(m,n);i>=1;i--)
		{
			if(ans[i]!=0)
			{
				printf("%d %d\n",i,ans[i]);
			}
		}
	}
	return 0;
}

