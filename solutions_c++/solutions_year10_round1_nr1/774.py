#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char mp[52][52];
int a[52][52];
int tp[52];
int fp[52];
int f[52][52];
int t,k,n;
int dir[8][2]={1,0,-1,0,1,1,-1,-1,1,-1,-1,1,0,-1,0,1};
int sum;
bool check(int x,int y)
{
	if(x >= 0&&x < n&&y>=0&&y<n)
		return true;
	else
		return false;
}
bool cal(int x,int y)
{
	int i,u,v;
	int tmp = f[x][y];
	int sum;
	for(i=0;i<8;i+=2)
	{
		sum = 1;
		u = x + dir[i][0];
		v = y + dir[i][1];
		while(check(u,v)&&f[u][v]==tmp)
		{
			sum++;
			u += dir[i][0];
			v += dir[i][1];
		}
		u = x + dir[i+1][0];
		v = y + dir[i+1][1];
		while(check(u,v)&&f[u][v]==tmp)
		{
			sum++;
			u += dir[i+1][0];
			v += dir[i+1][1];
		}
		if(sum >= k)
			return true;
	}
	return false;
}
int main()
{
	int i,j,l,tmp;
	int flag1,flag2;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	while(scanf("%d",&t)!=EOF)
	{
		for(i=1;i<=t;i++)
		{
			flag1 = flag2 = 0;
			memset(tp,0,sizeof(tp));
			memset(fp,0,sizeof(fp));
			memset(f,0,sizeof(f));
			scanf("%d%d",&n,&k);
			for(j=0;j<n;j++)
			{
				scanf("%s",mp[j]);
				for(l=n-1;l>=0;l--)
				{
					if(mp[j][l]!='.')
					{
						if(mp[j][l] == 'R')
							tmp = 1;
						else
							tmp = 2;
						a[j][tp[j]] = tmp;
						tp[j]++;
					}
				}
				for(l=0;l<tp[j];l++)
				f[n-l-1][n-j-1] = a[j][l];
			}
			for(j=0;j<n;j++)
			{
				for(l=0;l<n;l++)
				{
					if(f[j][l]!=0)
					{
						if(cal(j,l))
						{
							if(f[j][l]==1)
								flag1 = 1;
							else if(f[j][l]==2)
								flag2 = 1;
						}
					}
				}
			}
			printf("Case #%d: ",i);
			if(flag1 == 1 && flag2 == 1)
			{
				printf("Both\n");
			}
			else if(flag1 == 0 && flag2 == 1)
			{
				printf("Blue\n");
			}
			else if(flag1 == 1 && flag2 == 0)
			{
				printf("Red\n");
			}
			else
				printf("Neither\n");
		}
	}
	return 0;
}
