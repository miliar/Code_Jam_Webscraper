
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
#define N 55
char mp[N][N];
int intmp[N][N];
int newmp[N][N];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
	int T,csn=1;
	scanf("%d",&T);
	int n,k;
	while(T--)
	{
		memset(intmp,0,sizeof(intmp));
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
		{
			scanf("%s",mp[i]);
			for(int j=0;j<n;j++)
			{
				if(mp[i][j]=='R')
				{
					intmp[i][j]=1;
				}
				else if(mp[i][j]=='B')
				{
					intmp[i][j]=2;
				}
			}
		}
		memset(newmp,0,sizeof(newmp));
		int cnt;
		for(int i=0;i<n;i++)
		{
			cnt=n-1;
			for(int j=n-1;j>=0;j--)
			{
				if(intmp[n-1-i][j]!=0)
				{
					newmp[cnt--][i]=intmp[n-1-i][j];
				}
			}
		}
		int f1=0,f2=0;
		int cc;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(newmp[i][j]==1)
				{
					cc=1;
					for(int l=j+1;l<n;l++)
					{
						if(newmp[i][l]==1)
						{
							cc++;
						}
						else
						break;
					}
					if(cc>=k)
					{
						f1=1;
						break;
					}
				}
			}
			if(f1==1)
			break;
		}
		if(f1==0)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(newmp[j][i]==1)
					{
						cc=1;
						for(int l=j+1;l<n;l++)
						{
							if(newmp[l][i]==1)
							{
								cc++;
							}
							else
							break;
						}
						if(cc>=k)
						{
							f1=1;
							break;
						}
					}
				}
				if(f1==1)
				break;
			}
		}
		if(f1==0)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(newmp[i][j]==1)
					{
						int l;
						for(l=0;l<k;l++)
						{
							if(i+l<n&&j+l<n&&newmp[i+l][j+l]==1)
							{
							}
							else
							break;
						}
						if(l==k)
						{
							f1=1;
							break;
						}
						for(l=0;l<k;l++)
						{
							if(i-l>=0&&j-l>=0&&newmp[i-l][j-l]==1)
							{
							}
							else
							break;
						}
						if(l==k)
						{
							f1=1;
							break;
						}
					}
				}
				if(f1==1)
				break;
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(newmp[i][j]==2)
				{
					cc=1;
					for(int l=j+1;l<n;l++)
					{
						if(newmp[i][l]==2)
						{
							cc++;
						}
						else
						break;
					}
					if(cc>=k)
					{
						f2=1;
						break;
					}
				}
			}
			if(f2==1)
			break;
		}
		if(f2==0)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(newmp[j][i]==2)
					{
						cc=1;
						for(int l=j+1;l<n;l++)
						{
							if(newmp[l][i]==2)
							{
								cc++;
							}
							else
							break;
						}
						if(cc>=k)
						{
							f2=1;
							break;
						}
					}
				}
				if(f2==1)
				break;
			}
		}
		if(f2==0)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(newmp[i][j]==2)
					{
						int l;
						for(l=0;l<k;l++)
						{
							if(i+l<n&&j+l<n&&newmp[i+l][j+l]==2)
							{
							}
							else
							break;
						}
						if(l==k)
						{
							f2=1;
							break;
						}
						for(l=0;l<k;l++)
						{
							if(i-l>=0&&j-l>=0&&newmp[i-l][j-l]==2)
							{
							}
							else
							break;
						}
						if(l==k)
						{
							f2=1;
							break;
						}
					}
				}
				if(f2==1)
				break;
			}
		}
		printf("Case #%d: ",csn++);
		if(f1==1&&f2==1)
		{
			printf("Both\n");
		}
		else if(f1==1&&f2==0)
		{
			printf("Red\n");
		}
		else if(f1==0&&f2==0)
		{
			printf("Neither\n");
		}
		else
		{
			printf("Blue\n");
		}
	}
	return 0;
}

