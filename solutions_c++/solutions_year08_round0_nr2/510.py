#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

struct Node
{
	int s ,t ;
	int kind;
};
Node train[200];
int a, b;
int T;
bool compare(const Node & a , const Node & b)
{
	if(a.s == b.s)
		return a.t < b.t;
	return a.s < b.s;
}
priority_queue<int,vector<int>,greater<int> > Q[2];
int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);
	int cases ;
	scanf("%d",&cases);
	int f = 0;
	while( cases -- )
	{
		int i ,j ;
		while(!Q[0].empty()) Q[0].pop();
		while(!Q[1].empty()) Q[1].pop();
		scanf("%d %d %d",&T,&a,&b);
		int h1,m1,h2,m2;
		for(i = 0 ;i < a ; i ++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			train[i].s = h1 * 60 + m1 ;
			train[i].t = h2 * 60 + m2 ;
			train[i].kind = 0;
		}
		for(i = a ;i <a + b ; i ++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			train[i].s = h1 * 60 + m1 ;
			train[i].t = h2 * 60 + m2 ;
			train[i].kind = 1;
		}
		sort(train , train + a + b, compare);
		int cnt[2];
		cnt[0] = cnt[1] = 0;
		for( i = 0 ; i < a + b ; i ++)
		{
			if(Q[train[i].kind].empty())
			{
				cnt[train[i].kind] ++;
				Q[1 - train[i].kind].push( train[i].t + T);
			}
			else
			{
				int MM = Q[train[i].kind].top();
				if(MM <= train[i].s)
				{
					Q[train[i].kind].pop();
					Q[1-train[i].kind].push(train[i].t + T);
				}
				else
				{
					cnt[train[i].kind] ++;
					Q[1-train[i].kind].push(train[i].t + T);
				}
			}
		}
		printf("Case #%d: %d %d\n",++f,cnt[0],cnt[1]);
	}
	return 0;
}