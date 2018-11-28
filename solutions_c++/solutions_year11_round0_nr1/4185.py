#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int findgoal(int init, const vector<pair<char, int>> &g, char color)
{
	int goal;
	for (goal=init; goal!=g.size() && g[goal].first!=color; ++goal)
		;
	if (goal==g.size())
		goal=-1;
	return goal;
}

int main()
{
	int n;
	cin >> n;
	for (int casenum=1; casenum<=n; ++casenum)
	{
		int j;
		cin >> j;
		vector<pair<char,int>> goals;
		while (j--)
		{
			char c;
			int i;
			cin >> c >> i;
			goals.push_back({c,i});
		}
		int time=0;
		int orangegoalnum;
		int orangegoal=1;
		int orangepos=1;
		int bluegoalnum;
		int bluegoal=1;
		int bluepos=1;

		orangegoalnum=findgoal(0, goals, 'O');
		if (orangegoalnum!=-1)
		{
			orangegoal=goals[orangegoalnum].second;
		}
		bluegoalnum=findgoal(0, goals, 'B');
		if (bluegoalnum!=-1)
		{
			bluegoal=goals[bluegoalnum].second;
		}

		j=0;
		while (orangegoalnum!=-1 || bluegoalnum!=-1)
		{
			/*cout << "Time: " << time << " orange " << orangepos << "->" << orangegoal << " (" << orangegoalnum << ")"
			  << " blue " << bluepos << "->" << bluegoal << " (" << bluegoalnum << ")"
			  << endl;*/
			bool pushed=false;
			if (orangegoalnum!=-1)
			{
				if (orangegoal==orangepos)
				{
					if (goals[j].first=='O')
					{
						pushed=true;
					}
				}
				else if (orangegoal<orangepos)
					--orangepos;
				else if (orangegoal>orangepos)
					++orangepos;
			}
			if (bluegoalnum!=-1)
			{
				if (bluegoal==bluepos)
				{
					if (goals[j].first=='B')
					{
						pushed=true;
					}
				}
				else if (bluegoal<bluepos)
					--bluepos;
				else if (bluegoal>bluepos)
					++bluepos;
			}
			if (pushed)
			{
				if (goals[j].first=='O')
				{
					orangegoalnum=findgoal(j+1, goals, 'O');
					if (orangegoalnum!=-1)
					{
						orangegoal=goals[orangegoalnum].second;
					}
				}
				else
				{
					bluegoalnum=findgoal(j+1, goals, 'B');
					if (bluegoalnum!=-1)
					{
						bluegoal=goals[bluegoalnum].second;
					}
				}
				++j;
			}
			++time;
		}
		cout << "Case #" << casenum << ": " << time << endl;
	}
}
