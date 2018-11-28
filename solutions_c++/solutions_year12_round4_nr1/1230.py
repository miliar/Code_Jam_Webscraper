#include<set>
#include<map>
#include<ctime>
#include<cmath>
#include<queue>
#include<vector>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>

#define F first
#define S second
#define MP make_pair
#define SZ size()
#define PB push_back
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define M 10005

using namespace std;
typedef pair<int,int> P;
P in[M];
int n,d,t,dis[M];
bool inq[M];
queue<int> q;
bool spfa()
{
	q=queue<int> ();
	int cur;
	MSET(dis,0);
	MSET(inq,false);
	q.push(1);
	dis[1]=in[1].F;
	
	while(!q.empty())
	{
		cur=q.front();
		q.pop();
		inq[cur]=false;
		if(abs(d-in[cur].F) <= dis[cur])
			return true;
		
		
		REP(i,1,n)
			if(dis[i]<min(in[i].S,abs(in[cur].F-in[i].F)) && abs(in[cur].F-in[i].F)<=dis[cur])
			{
				dis[i]=abs(in[cur].F-in[i].F);
				dis[i]=min(dis[i],in[i].S);
				if(!inq[i])
				{
					q.push(i);
					inq[i]=true;
				}
			}
	}
	
	return false;
}
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		scanf("%d",&n);
		REP(i,1,n)scanf("%d %d",&in[i].F,&in[i].S);
		scanf("%d",&d);
		
		if(spfa())printf("Case #%d: YES\n",tt);
		else printf("Case #%d: NO\n",tt);
	}
	return 0;
}
