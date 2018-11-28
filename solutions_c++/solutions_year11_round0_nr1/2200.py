#include <stdio.h>
#include <algorithm>
#include <vector>
#include <utility>
#include <deque>

using namespace std;

vector<pair<char, int> > moves;
deque<int>  movesO, movesB;

int main()
{
	int T;
	scanf("%d ",&T);

	for (int caseID = 1; caseID <= T; ++caseID)
	{
		int N;
		scanf("%d ", &N);

		moves.clear();
		movesO.clear(); movesB.clear();

		for (int i = 0; i < N; ++i){
			char robot; 
			int where;
			scanf("%c %d ", &robot, &where);
			moves.push_back(make_pair(robot, where));
			if (robot == 'O') movesO.push_back(where);
			else movesB.push_back(where);
		}

		int whereO = 1, whereB = 1;
		int ans = 0;
		for (int i = 0; i < N; ++i){
			if (moves[i].first == 'O'){
				int delta = abs(whereO - moves[i].second) + 1;
				ans += delta;
				movesO.pop_front();
				whereO = moves[i].second;
				if (!movesB.empty()){
					if (whereB < movesB.front())
						whereB += min(delta, movesB.front() - whereB);
					else
						whereB -= min(delta, whereB - movesB.front());
				}
				
			}
			if (moves[i].first == 'B'){
				int delta = abs(whereB - moves[i].second) + 1;
				ans += delta;
				movesB.pop_front();
				whereB = moves[i].second;
				if (!movesO.empty()){
					if (whereO < movesO.front())
						whereO += min(delta, movesO.front() - whereO);
					else
						whereO -= min(delta, whereO - movesO.front());
				}
				
			}		
		}	
		printf("Case #%d: %d\n", caseID, ans);

	}

	return 0;
}
