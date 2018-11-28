#include <stdio.h>
#include <queue>

using namespace std;

#define MAX 40
#define inf 500100100
int d[MAX];
int g[MAX][MAX];

int ligado[MAX];
int n;

int maxthr;

void bfs()
{
		int i;
		for(i=0;i<n;++i)
				d[i]=inf;

		queue<int> q;

		q.push(0);
		d[0]=0;

		while(!q.empty())
		{
				int now = q.front();
				q.pop();
				for(i=0;i<n;++i)
						if(g[now][i] && d[i]>=inf)
						{
								q.push(i);
								d[i]=d[now]+1;
						}
		}
}

int thr[MAX];
void calcula()
{
		int i,j;
		int tmp=0;
		ligado[1]=0;
		for(i=0;i<n;++i)
				thr[i]=0;
		for(i=0;i<n;++i) if(ligado[i]) for(j=0;j<n;++j)
				if(g[i][j]) thr[j]=1;

		for(i=0;i<n;++i)
				if(thr[i] && !ligado[i])
						++tmp;

		if(tmp>maxthr)
				maxthr=tmp;
}


void rebuild(int now)
{
		int i;
		ligado[now]=1;
		if(now==0)
				calcula();
		for(i=0;i<n;++i)
				if(g[i][now] && d[i]<d[now])
						rebuild(i);
		ligado[now]=0;
}

int main()
{
		int i,j;
		int m;
		int t,ccnt;
		scanf("%d",&t);

		for(ccnt=1;ccnt<=t;++ccnt)
		{
				scanf("%d %d",&n,&m);

				for(i=0;i<n;++i)
						for(j=0;j<n;++j)
								g[i][j]=0;

				for(i=0;i<m;++i)
				{
						int t1,t2;
						scanf("%d,%d",&t1,&t2);
						g[t1][t2]=g[t2][t1]=1;
				}

				maxthr=-1;

				bfs();
				rebuild(1);

				printf("Case #%d: %d %d\n",ccnt,d[1]-1,maxthr);
		}
		return 0;
}



