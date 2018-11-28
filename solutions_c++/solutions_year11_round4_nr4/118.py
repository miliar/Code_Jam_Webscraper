#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define maxn 100
using namespace std;
struct node1
{
	int t;
	node1 *next;
}ei[2000], *e[maxn];

int n, m, ttal, brond, b2, rq;
bool v[maxn], srab[maxn];
int jsuan()
{
	memset(srab, 0, sizeof(srab));
	int s=0;
	v[1]=false;
	for(node1 *j=e[0];j;j=j -> next)
			srab[j -> t]=true;
	for(int i=2;i<=n;i++)
	if(v[i])
	{
		for(node1 *j=e[i];j;j=j -> next)
			srab[j -> t]=true;
	}
	for(int i=1;i<=n;i++)
		if(srab[i] && !v[i]) s++;
	return s;
}
void add(int s, int t)
{
	ttal++;
	ei[ttal].t=t;
	ei[ttal].next=e[s];
	e[s]=&ei[ttal];
	
	ttal++;
	ei[ttal].t=s;
	ei[ttal].next=e[t];
	e[t]=&ei[ttal];
}
void prework()
{
	ttal=0;
	memset(e, 0, sizeof(e));
	scanf("%d%d", &n, &m);
	for(int i=1;i<=m;i++)
	{
		int x, y;
		scanf("%d,%d", &x, &y);
		add(x, y);
	}
}
void dfs(int i, int s)
{
	if(s > brond) return;
	if(i==1)
	{
		if(s < brond) brond=s, b2=jsuan();
		else if(s==brond) b2=max(jsuan(), b2);
		return;
	}
	for(node1 *j=e[i];j;j=j -> next)
	{
		int k=j -> t;
		if(!v[k])
		{
			v[k]=true;
			dfs(k, s + 1);
			v[k]=false;
		}
	}
}
void work()
{
	brond=maxn;
	b2=0;
	dfs(0, 0);
	printf("Case #%d: %d %d\n", rq, brond - 1, b2);
}
int main()
{
	int rqT;
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &rqT);
	for(rq=1;rq<=rqT;rq++)
	{
		prework();
		work();
	}
	return 0;
}
