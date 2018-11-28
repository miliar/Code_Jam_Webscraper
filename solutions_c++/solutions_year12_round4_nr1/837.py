#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<cmath>
using namespace std;
#define maxn 10010
int d[maxn],l[maxn];
int N,option;
struct node
{
	int l,id;
};
queue <node> que;
int visited[maxn];
bool search()
{
	int i,plen,templ;
	memset(visited,0,sizeof(visited));
	while(!que.empty())que.pop();
	node s,t,temp;
	s.l=min(d[0],l[0]);
	s.id=0;
	visited[0]=s.l;
	que.push(s);
	while(!que.empty())
	{
		s=que.front();
		que.pop();
		plen=d[s.id]+s.l;
		if(plen>=option)
			return true;
		for(i=s.id+1;i<N;i++)
		{
			if(plen<d[i])
				break;
			templ=min(d[i]-d[s.id],l[i]);
			if(templ>visited[i])
			{
				temp.l=templ;
				temp.id=i;
				visited[i]=templ;
				que.push(temp);
			}
		}
	}
	return false;
}
int main()
{
	int i,tcase,casenum=0;
	freopen("AA.in","r",stdin);
	freopen("AA.out","w",stdout);
	scanf("%d",&tcase);
	while(tcase--)
	{
		printf("Case #%d: ",++casenum);
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%d %d",&d[i],&l[i]);
		scanf("%d",&option);
		if(search())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
