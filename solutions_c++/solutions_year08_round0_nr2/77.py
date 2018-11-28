#include <stdio.h>
#include <string.h>
typedef struct Edge
{
	int v;
	Edge *next; 
}Edge;

Edge edge_stack[40010];
Edge *linklist[210];
int used_edge_stack;
int NP;
int A[101][2];
int B[101][2];
int pre[210];
bool vis[210];

Edge *addEdge(int v,Edge *next)
{
	Edge *ret = &edge_stack[used_edge_stack++];
	ret->next=next;
	ret->v=v;
	return ret;
}

bool dfs(int w)
{
	Edge *index;
	int temp;
	for (index=linklist[w];index;index=index->next)
	{
		if (!vis[index->v])
		{
			vis[index->v]=true;
			temp = pre[index->v];
			pre[index->v] = w;
			if (temp==-1 || dfs(temp)) return true;
			pre[index->v] = temp;
		}
	}
	return false;
}
void MBM()
{
	int i;
	memset(pre,-1,sizeof(pre));
	for (i=0;i<NP;++i)
	{
		memset(vis,0,sizeof(vis));
		dfs(i);
	}
}
int main()
{
	freopen("Ba.out","w",stdout);
	int t,st;
	int exct,i,j,na,nb,hour,minute;
	int aa,bb;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d",&exct);
		scanf("%d%d",&na,&nb);
		NP=na+nb;
		for (i=0;i<na;++i)
		{
			scanf("%d:%d",&hour,&minute);
			A[i][0] = hour*60 + minute;
			scanf("%d:%d",&hour,&minute);
			A[i][1] = hour*60 + minute;
		}
		for (i=0;i<nb;++i)
		{
			scanf("%d:%d",&hour,&minute);
			B[i][0] = hour * 60 +minute;
			scanf("%d:%d",&hour,&minute);
			B[i][1] = hour * 60 +minute;
		}
		memset(linklist,0,sizeof(linklist));
		used_edge_stack=0;
		for (i=0;i<na;++i)
		{
			for (j=0;j<nb;++j)
			{
				if (A[i][0] >= B[j][1] + exct )
				{
					linklist[j+na] = addEdge(i,linklist[j+na]);
				}
				if (B[j][0] >= A[i][1] + exct )
				{
					linklist[i] = addEdge(j+na,linklist[i]);
				}
			}
		}
		/*
		for (i=0;i<NP;++i)
		{
			printf("%d->:",i);
			for (Edge * index=linklist[i];index;index=index->next)
			{
				printf(" %d",index->v);
			}
			printf("\n");
		}*/
		MBM();
		aa=bb=0;
		for (i=0;i<na;++i)
		{
			if (pre[i]==-1) aa++;
		}
		for (;i<NP;++i)
		{
			if (pre[i]==-1) bb++;
		}
		printf("Case #%d: %d %d\n",t+1,aa,bb);
	}
	return 0;
}





