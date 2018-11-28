#include <cstdio>
#include <vector>
#include <queue>
#include <utility>
#define VI vector<int>
#define LL long long
#define PB push_back
#define F first
#define S second
using namespace std;


int cases,iD=1;
int rides,limit,N,var;

pair<LL,LL> compute(queue<int>Q)
{
	LL cost=0,cnt=0;
	while(!Q.empty() && cost+Q.front()<=limit)
	{
		cost+=Q.front();
		Q.pop();
		cnt++;
	}
	return make_pair(cost,cnt);
}

vector<int> getVI(queue<int>Q)
{
	vector<int>ret;
	while(!Q.empty())
	{
		ret.PB(Q.front());
		Q.pop();
	}
	return ret;
}	

int main()
{

	for(scanf("%d",&cases);cases--;)
	{
		scanf("%d %d %d",&rides,&limit,&N);
		queue<int>Q;
		for(int i=0;i<N;i++)
		{
			scanf("%d",&var);
			Q.push(var);
		}

		pair< vector<int>,pair<LL,LL> >memo[1005];

		for(int i=0;i<N;i++)
		{
			memo[i].F=getVI(Q);
			memo[i].S=compute(Q);

			Q.push(Q.front());
			Q.pop();
		}

		VI search=memo[0].F;
		int pos;
		for(pos=0;pos<N;pos++)
			if(search==memo[pos].F) break;

		LL total=0;
		while(rides--)
		{
			total+=memo[pos].S.F;
			pos=(pos+memo[pos].S.S)%N;
		}
		printf("Case #%d: %lld\n",iD++,total);
	}

	return 0;
}

