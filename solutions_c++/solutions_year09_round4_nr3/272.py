#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define N 202 
int useif[N];
int link[N];
int mat[N][N];
int gn,gm;
int can(int t) 
{ 
	int i; 
	for(i=1;i<=gm;i++) 
	{ 
		if(useif[i]==0 && mat[t][i]) 
		{ 
			useif[i]=1; 
			if(link[i]==-1 || can(link[i])) 
			{ 
				link[i]=t; 
				return 1; 
			}
		} 
	} 
	return 0; 
} 

int MaxMatch() 
{ 
	int i,num; 
	num=0; 
	memset(link,0xff,sizeof(link)); 
	for(i=1;i<=gn;i++) 
	{
		memset(useif,0,sizeof(useif)); 
		if(can(i)) num++; 
	} 
	return num; 
} 

int prices[201][100];


int main()
{
	int i,j;
	int cases;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cases);
	for(int t=1;t<=cases;t++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		gn=gm=n*2;
		for(i=1;i<=n;i++)
		{
			for(j=0;j<k;j++)
				scanf("%d",&prices[i][j]);
		}
		memset(mat,0,sizeof(mat));
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				int s;
				for(s=0;s<k;s++)
				{
					if(prices[i][s]<prices[j][s])
						continue;
					else
						break;
				}
				if(s==k)
					mat[i][n+j]=1;
				else
					mat[i][n+j]=0;
			}
		}
		int ans=MaxMatch();
		printf("Case #%d: %d\n",t,n-ans);
	}
	return 0;
}