#include<stdio.h>
#include<memory.h>
#include<vector>
#include<algorithm>
using namespace std;

int n,m;
int like[2000][2000],liken[2000],u[2000],fir[2000];
int c[2000],d[2000],st[2000];
int h[2000][2000],hn[2000];
bool b[2000];

int main()
{
	int test,T,i,j,k;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(T=1;T<=test;T++)
	{
		scanf("%d%d",&n,&m);
		memset(d,0,sizeof(d));
		memset(liken,0,sizeof(liken));
		memset(fir,-1,sizeof(fir));
		for(i=0;i<m;i++)
		{
			c[i]=0;
			scanf("%d",&j);
			d[i]=j;
			for(;j>0;j--)
			{
				int x,y;
				scanf("%d%d",&x,&y);
				if(y==0)
				{
					c[i]++;
					like[i][liken[i]++]=x-1;
				}
				else
				{
					fir[i]=x-1;
				}
			}
			sort(like[i],like[i]+liken[i]);
		}
		int top=0;
		memset(hn,0,sizeof(hn));
		memset(u,0,sizeof(u));
		for(i=0;i<m;i++)
		{
			if(c[i]==0)
			{
				st[top++]=i;
			}
			else if(liken[i]>0)
			{
				h[like[i][0]][hn[like[i][0]]++]=i;
				u[i]++;
			}
		}
		memset(b,0,sizeof(b));
		printf("Case #%d: ",T);
		while(top>0)
		{
			j=st[top-1];
			if(fir[j]==-1)
			{
				printf("IMPOSSIBLE\n");
				break;
			}
			top--;
			if(b[fir[j]]==0)
			{
				b[fir[j]]=1;
				for(i=0;i<hn[fir[j]];i++)
				{
					k=h[fir[j]][i];
					if(u[k]==liken[k])
					{
						st[top++]=k;
					}
					else
					{
						int flag=0;
						while(u[k]<liken[k])
						{
							if(b[like[k][u[k]]]==0)
							{
								h[like[k][u[k]]][ hn[like[k][u[k]]]++]=k;
								flag=1;
								u[k]++;
								break;
							}
							u[k]++;
						}
						if(flag==0)
						st[top++]=k;
					}
				}
			}
		}
		if(top==0)
		{
			for(i=0;i<n;i++)
				printf("%d ",b[i]);
			printf("\n");
		}
	}
}
