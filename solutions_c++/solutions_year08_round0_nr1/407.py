#include<iostream>
using namespace std;
char v[109][109];
char w[1009][109];
int cost[1009];
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt3.out","w",stdout);
	int ca;
	scanf("%d",&ca);
	int tca=0;
	int i,j,k;
	while(tca++<ca)
	{
		int n,m;
		scanf("%d",&n);
		for(i=0;i<=n;i++)
			gets(v[i]);
		scanf("%d",&m);
		char ch;
		for(i=0;i<=m;i++)
			gets(w[i]);
		memset(cost,0x3f,sizeof(cost));
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{	
				cost[j]=0;
				if(strcmp(v[i],w[j])==0)
				{
					break;
				}
			}
			if(j>m)cost[j]=0;
		}
		for(i=1;i<=m;i++)
		{
			//if(cost[j]>500000)continue;
			for(j=1;j<=n;j++)
			{
				for(k=i;k<=m;k++)
				{
					cost[k]=min(cost[k],cost[i]+1);
					if(strcmp(v[j],w[k])==0)
					{
						break;
					}
				}
				if(k>m)
				{
					cost[k]=min(cost[k],cost[i]+1);
				}
			}
		}
		printf("Case #%d: %d\n",tca,cost[m+1]);
	}//while(1);
}
