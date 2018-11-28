#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>

#define MAXN 2048
#define MAXM 2048

using namespace std;

typedef pair<int,int> E;


int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		int n,m,c,x,y;
		scanf("%d%d",&n,&m);

		vector< set<E> > g(m);
		vector< int > malt(m,-1);
		vector< int > good(m,0);
		vector< int > bad(m,0);
		vector< bool > happy(m,false);
		vector<int> res(n+1,0);
		set<int> q;
		int cnt=0;

		for(int i=0;i<m;i++)
		{
			scanf("%d",&c);
			for(int j=0;j<c;j++)
			{
				scanf("%d%d",&x,&y);
				g[i].insert(E(x,y));
				if(y==1)
				{
					malt[i] = x;
					bad[i] += 1;
				}
				else
					good[i] += 1;
			}
		}

		for(int i=0;i<m;i++)
			if( good[i] == 0 )
				q.insert(i);

		while( ! q.empty() )
		{
			x = *q.begin();
			q.erase(x);

			cnt++;
			happy[x] = true;

			y = malt[x];

			res[y] = 1;

			for(int i=0;i<m;i++)
				if( !happy[i] )
				{
					if( g[i].count( E(y,0) ) )
					{
						g[i].erase( E(y,0) );
						good[i] --;
						if( good[i] == 0 )
						{
							if( bad[i] == 0 )
							{
								cnt = -1;
								goto out;
							}
							else
							{
								q.insert(i);
							}
						}
					}
					if( g[i].count( E(y,1) ) )
					{
						happy[i] = true;
						q.erase(i);
					}

				}
		}
out:
		if( cnt != -1 )
		{
			printf("Case #%d:",z);
			for(int i=1;i<=n;i++)
				printf(" %d",res[i]);
			printf("\n");
		}
		else
			printf("Case #%d: IMPOSSIBLE\n",z);
	}

	return 0;
}
