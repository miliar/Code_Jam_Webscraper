// Google Code Jam 2011 - Mateusz Kurek (Matthew23) - Qualification Round - A. Bot Trust

#include <iostream>
#include <cstdio>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

int ab(int a)
{
	return a > 0 ? a : (-1)*a;
}

int main()
{
	//ios_base::sync_with_stdio(false);

	pair<int, int> act;
	
	int t, n, p;
	int lm, mtd; // last moves, moves to do
	int pos[2], moves; // pos[orange position, blue position], total moves
	int act_type;

	char r;

	scanf("%d", &t);

	for(int i=1;i<=t;i++)
	{
		scanf("%d", &n);
		queue<pair<int, int> > q;
		
		lm = 0;
		pos[0] = 1;
		pos[1] = 1;
		moves = 0;

		for(int j=0;j<n;j++)
		{
			cin>>r>>p;
			//scanf("%c%d", &r, &p);
			//printf("%c -> %d\n", r, p);
			q.push(make_pair(r == 'O' ? 0 : 1, p)); // 0 - orange, 1 - blue		
		}

		while(!q.empty())
		{
			lm = 0;
			// act group
			act_type = q.front().first;
			//printf("=================\nact_type = %d\n", act_type);
			while(!q.empty() && q.front().first == act_type)
			{
				act = q.front();
				q.pop();
				//printf("Dodaje do grupy: (%d, %d)\n", act.first, act.second);
				moves += ab(pos[act_type] - act.second) + 1;
				lm += ab(pos[act_type] - act.second) + 1;
				pos[act_type] = act.second;
				//printf("moves = %d, lm = %d, pos[%d] = %d\n", moves, lm, act_type, pos[act_type]);
			}

			if(!q.empty())
			{
				//printf("Kolejka jeszcze nie pusta\n");
				// first of opposite group
				act = q.front();
				mtd = ab(pos[act.first] - act.second);
				
				//printf("Opposite postion: %d\n", pos[act.first]);

				// adding moves to opposite group
				if(act.second < pos[act.first])
				{
					pos[act.first] = max(pos[act.first]-lm, act.second);
				}
				else if(act.second > pos[act.first])
				{
					pos[act.first] = min(pos[act.first]+lm, act.second);
				}
				
				//printf("Opposite postion after: %d\n", pos[act.first]);
			}

			//printf("==========================\n");
		}

		printf("Case #%d: %d\n", i, moves);
	}
}
