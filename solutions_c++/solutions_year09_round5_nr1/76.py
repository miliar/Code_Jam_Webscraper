#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
#include <vector>
using namespace std;

#define	sz(v)	(int)v.size()
#define	rep(i,n)	for((i)=0;(i) < (n); (i)++)
#define	rab(i,a,b)	for((i)=(a);(i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)

typedef pair<int,int>	PII;

int	dr[] = {-1,0,1,0};
int	dc[] = {0,-1,0,1};

char	grid[20][20];
int	R,C;
int	boxes;

struct State
{
	PII	position[5];

	void process()
	{
		sort(position,position + boxes);
	}

	bool operator == (const State &s) const
	{
		int	i;

		Fi(boxes) if(position[i] != s.position[i]) return false;
		return true;
	}

	bool operator < (const State &s) const
	{
		int	i;

		Fi(boxes) if(position[i] != s.position[i]) return position[i] < s.position[i]; 

		return false;
	}

	bool valid()
	{
		int	i;

		Fi(boxes - 1) if(position[i] == position[i-1]) return false;
		return true;
	}

	bool has(PII p)
	{
		int	i;

		Fi(boxes) if(position[i] == p) return true;
		return false;
	}
};

map <State,int>	M;

State	danger;
set <PII>	temp;

void dfs(PII curr)
{
	int	i;
	PII	n;

	//printf("%d %d\n",curr.first,curr.second);
	if(temp.find(curr) != temp.end()) return;
	temp.insert(curr);

	Fi(4)
	{
		n.first = curr.first + dr[i];
		n.second = curr.second + dc[i];
		if(danger.has(n)) dfs(n);
	}
}

bool isDangerous(State s)
{
	danger = s;
	temp.clear();

	dfs(s.position[0]);
	//printf("------\n");

	return (sz(temp) != boxes);
}


int bfs()
{
	State	curr,next,final;
	PII	push,npos;
	int	i,j,k,l;
	bool	d1,d2;
	queue <State>	Q;

	boxes = 0;
	Fi(R) Fj(C) if(grid[i][j] == 'x' || grid[i][j] == 'w') boxes++;

	k = 0;
	Fi(R) Fj(C) if(grid[i][j] == 'o' || grid[i][j] == 'w') curr.position[k++] = make_pair(i,j);
	k = 0;
	Fi(R) Fj(C) if(grid[i][j] == 'x' || grid[i][j] == 'w') final.position[k++] = make_pair(i,j);

	M.clear();
	M[curr] = 0;
	Q.push(curr);

	while(!Q.empty())
	{
		curr = Q.front();
		Q.pop();

		if(curr == final) return M[curr];
		//printf("%d\n",M[curr]);
		//
		//Fi(boxes) printf("(%d %d) ",curr.position[i].first, curr.position[i].second);
		//printf("\n");

		d1 = isDangerous(curr);
		//printf("danger = %d\n",d1 ? 1 : 0);

		Fk(boxes)
		{
			Fi(4)
			{
				npos.first = curr.position[k].first + dr[i];
				npos.second = curr.position[k].second + dc[i];
				push.first = curr.position[k].first - dr[i];
				push.second = curr.position[k].second - dc[i];

				if(npos.first < 0 || npos.first >= R || npos.second < 0 || npos.second >= C) continue;
				if(push.first < 0 || push.first >= R || push.second < 0 || push.second >= C) continue;
				if(grid[npos.first][npos.second] == '#') continue;
				if(grid[push.first][push.second] == '#') continue;
				if(curr.has(npos) || curr.has(push)) continue;

				next = curr;
				next.position[k] = npos;
				next.process();

				if(M.find(next) == M.end())
				{
					d2 = isDangerous(next);

					if(d1 != true || d2 != true)
					{
						M[next] = (M[curr] + 1);
						Q.push(next);

						if(next == final) return M[next];
					}
				}
			}
		}
	}

	return -1;
}

int main()
{
	int	T,cs;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d %d",&R,&C);
		int	i;

		Fi(R) scanf("%s",grid[i]);

		printf("Case #%d: %d\n",cs,bfs());
	}
	return 0;
}
