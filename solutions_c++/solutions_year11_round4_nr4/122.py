//D

#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

int n,a,b;
int c,ans;
int dist[36];
int con[36][36],ncon[36];
int used[36];
bool thr[36];

void rec(int i,int d)
{
	//done
	if (d==c)
	{
		memset(thr,0,sizeof(thr));
			for (a=0; a<=d; a++)
				for (b=0; b<ncon[used[a]]; b++)
					thr[con[used[a]][b]]=1;
			for (a=0; a<=d; a++)
				thr[used[a]]=0;
			for (a=b=0; a<n; a++)
				if (thr[a])
					b++;
			if (!thr[1])
				return;
			if (b>ans)
				ans=b;
		return;
	}
	//try all neighbours
	for (int j=0; j<ncon[i]; j++)
		if (dist[con[i][j]]==d+1)
		{
			used[d+1]=con[i][j];
			rec(con[i][j],d+1);
		}
}

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("d.out","w",stdout);
	//vars
	int t,T;
	int m;
	queue <int> Q;
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//init
			memset(ncon,0,sizeof(ncon));
			memset(dist,-1,sizeof(dist));
				while (!Q.empty())
					Q.pop();
			//input
			scanf("%d%d",&n,&m);
				while (m--)
				{
					scanf("%d,%d",&a,&b);
					con[a][ncon[a]++]=b;
					con[b][ncon[b]++]=a;
				}
			//BFS for min. # of planets to conquer
			Q.push(0),dist[0]=0;
				while (!Q.empty())
				{
					a=Q.front(),Q.pop();
						//if (a==1)
						//	break;
						for (b=0; b<ncon[a]; b++)
							if (dist[con[a][b]]<0)
								Q.push(con[a][b]),dist[con[a][b]]=dist[a]+1;
				}
			//recursion for max. # of planets to threaten
			c=dist[1]-1;
			ans=-1;
			used[0]=0;
			rec(0,0);
			//output
			printf("Case #%d: %d %d\n",t,c,ans);
		}
	return(0);
}