#include <cstdio>
#include <queue>

using namespace std;

struct event
{
	int t;
	bool d;
	int w;

	bool operator<(const event& e) const
	{
		if( this->t == e.t )
		{
			if( e.d == false )
				return true;
			else
				return false;
		}
		return this->t > e.t;
	};
};

int main()
{
	int n,na,nb,t;

//	freopen("B-small-attempt0.in","r",stdin);
	scanf("%d",&n);

	for(int z=1;z<=n;z++)
	{
		priority_queue<event> pq;
		event e;

		scanf("%d%d%d\n",&t,&na,&nb);

		for(int i=0;i<na;i++)
		{
			int dh,dm,ah,am;
			scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
			e.t = dh*60 + dm;
			e.d = true;
			e.w = 0;

			pq.push(e);

			e.t = ah*60 + am + t;
			e.d = false;
			e.w = 1;

			pq.push(e);
		}

		for(int i=0;i<nb;i++)
		{
			int dh,dm,ah,am;
			scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
			e.t = dh*60 + dm;
			e.d = true;
			e.w = 1;

			pq.push(e);

			e.t = ah*60 + am + t;
			e.d = false;
			e.w = 0;

			pq.push(e);
		}

		int cnt[2]={0,0};
		int s[2] = {0,0};


		while( !pq.empty() )
		{
			event e = pq.top();
			pq.pop();

			//printf("%d %d %d\n",e.t,e.w,(int)e.d);

			if( e.d )
			{
				if( cnt[e.w] == 0 )
				{
					s[e.w] ++;
					cnt[e.w] ++;
				}

				cnt[e.w] --;
			}
			else
				cnt[e.w] +=1;
		}

		printf("Case #%d: %d %d\n", z, s[0], s[1]);
	}
	return 0;
}
