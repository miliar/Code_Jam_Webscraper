#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int n,N;
	scanf("%d",&N);
	int G[10001];
	int C[10001];
	int val[2][10001];
	int m,v,g,c,top,i,l;
	int INFINITY=999999;
	int temp;
	for (n=1;n<=N;n++)
	{
		scanf("%d %d",&m,&v);
		top=(m-1)/2;
		for (i=1;i<=top;i++)
		{
			scanf("%d %d",&G[i],&C[i]);
			val[0][i]=INFINITY;
			val[1][i]=INFINITY;
		}
		for (i=top+1;i<=m;i++)
		{
			scanf("%d",&l);
			val[l][i]=0;
			val[1-l][i]=INFINITY;
		}
		for (i=top;i>=1;i--)
		{
			//if (C[i]==0)//not changeable
			{
				if (G[i]==0)// or gate
				{
					val[0][i]=min(val[0][i],val[0][2*i]+val[0][2*i+1]);
					val[1][i]=min(val[1][2*i],val[1][2*i+1]);
				}
				else //and gate
				{
					val[1][i]=min(val[1][i],val[1][2*i]+val[1][2*i+1]);
					val[0][i]=min(val[0][2*i],val[0][2*i+1]);
				}
			}
			//else
			if (C[i]==1)
			{
				if (G[i]==0)//and
				{
					val[1][i]=min(val[1][i],val[1][2*i]+val[1][2*i+1]+1);
					val[0][i]=min(val[0][i],val[0][2*i]+1);
					val[0][i]=min(val[0][i],val[0][2*i+1]+1);
				}
				else //or
				{
					val[0][i]=min(val[0][i],val[0][2*i]+val[0][2*i+1]+1);
					val[1][i]=min(val[1][i],val[1][2*i]+1);
					val[1][i]=min(val[1][i],val[1][2*i+1]+1);
				}
			}
		}
		if (val[v][1]>=INFINITY)
			printf("Case #%d: IMPOSSIBLE\n",n);
		else
			printf("Case #%d: %d\n",n,val[v][1]);
	}
  	return 0;
}
