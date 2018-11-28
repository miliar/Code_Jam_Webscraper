#include<cstdio>
#include<algorithm>
#include<queue>
#include<set>
#include<utility>
#include<list>
#include<vector>
using namespace std;
#define PB push_back
#define ST first
#define ND second
#define MAXN 10000
#define OO (1<<26)
#define NIL (-1)
bool dbg=0;
int steps[MAXN][2];
bool aGate[MAXN];
bool ch[MAXN];
int value[MAXN];
int m,v;
void init()
{
	for(int i=0;i<m;i++)
	{
		value[i]=NIL;
		steps[i][0]=NIL;
		steps[i][1]=NIL;
	}
}

void readCase()
{
	scanf("%d%d",&m,&v);
	init();
	for(int i=0;i<(m-1)/2;i++)
	{
		int g,c;
		scanf("%d%d",&g,&c);
		aGate[i]=g;
		ch[i]=c;
	}
	for(int i=(m-1)/2;i<m;i++)
	{
		scanf("%d",&value[i]);
		steps[i][value[i]]=0;
		steps[i][(value[i]^1)]=OO;
	}
}
void compute(int v)
{
	int a=v*2+1,b=v*2+2;
	if(steps[v][0]==NIL)
	{
		steps[v][0]=OO;
		steps[v][1]=OO;
		compute(a);
		compute(b);
		if((!aGate[v]) || ch[v])
		{
			int add=0;
			if(aGate[v])add=1;
			steps[v][0]=add+steps[a][0]+steps[b][0];
			steps[v][1]=add+min(steps[a][1]+min(steps[b][1],steps[b][0]),steps[a][0]+steps[b][1]);
		}
		if(aGate[v] || ch[v])
		{
			int add=0;
			if(!aGate[v])add=1;
			steps[v][0]=min(steps[v][0],add+min(steps[a][0]+min(steps[b][0],steps[b][1]),steps[a][1]+steps[b][0]));
			steps[v][1]=min(steps[v][1],add+steps[a][1]+steps[b][1]);
		}
		if(steps[v][0]>OO)steps[v][0]=OO;
		if(steps[v][1]>OO)steps[v][1]=OO;
	}
	if(dbg)printf("compute(%d)[%d,%d]\n",v+1,steps[v][0],steps[v][1]);
}

void computeCase(int cas)
{
	compute(0);
	if(steps[0][v]==OO)
		printf("Case #%d: IMPOSSIBLE\n",cas);
	else
		printf("Case #%d: %d\n",cas,steps[0][v]);
}


int main()
{
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		readCase();
		computeCase(i);
	}
	return 0;
}
