#include<iostream>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<algorithm>
#include<queue>
using namespace std;
char map[201][201],temp[201];
bool use[201][201];
int dx[4]={0,0,1,-1},dy[4]={1,-1,0,0};
int x[40001],y[40001],step[40001];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int i,j,k,l,m,n,sum,number,test,t;
	scanf("%d",&test);
	for (t=1;t<=test;t++)
	{
		scanf("%d",&n);
		memset(map,' ',sizeof(map));
		memset(use,false,sizeof(use));
		gets(temp);
		for (i=n-1;i>=0;i--)
		{
			gets(temp);
			l=strlen(temp);
			for (j=0;j<l;j++)
				map[100-i][100-n+j+1]=temp[j];
		}
		for (i=1;i<n;i++)
		{
			gets(temp);
			l=strlen(temp);
			for (j=0;j<l;j++)
				map[100+i][100-n+j+1]=temp[j];
		}
		memset(x,0,sizeof(x));
		memset(y,0,sizeof(y));
		memset(step,0,sizeof(step));
		int head=0,tail=1;
		x[1]=100;y[1]=100;
		use[x[1]][y[1]]=true;
		while (head<tail)
		{
			head++;
			bool flag=true;
			for (i=100-n;i<=100+n;i++)
			{
				for (j=100-n;j<=100+n;j++)
				{
					if (map[i][j]!=' ')
					{
						if (map[i][y[head]*2-j]!=' '&&map[i][y[head]*2-j]!=map[i][j])
						{
							flag=false;
							break;
						}
						if (map[x[head]*2-i][j]!=' '&&map[x[head]*2-i][j]!=map[i][j])
						{
							flag=false;
							break;
						}
					}
				}
				if (!flag)
					break;
			}
			if (flag)
				break;
			for (i=0;i<4;i++)
			{
				tail++;
				x[tail]=x[head]+dx[i];
				y[tail]=y[head]+dy[i];
				step[tail]=step[head]+1;
				if (use[x[tail]][y[tail]])
					continue;
				use[x[tail]][y[tail]]=true;
			}
		}
		cout<<tail<<endl;
		printf("Case #%d: %d\n",t,(n+step[tail])*(n+step[tail])-n*n);
	}
	return 0;
}		
