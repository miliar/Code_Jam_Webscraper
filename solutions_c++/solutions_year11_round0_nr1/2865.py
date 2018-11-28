#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char** args)
{
	int T;
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		int N;
		cin >> N;

		typedef vector<pair<int, int> > OrderList;
		
		vector<int>	robotPress[2];
		OrderList	order;
				
		for (int n = 0; n < N; n++)
		{
			string	robot;
			int		button;
			
			cin >> robot >> button;
			
			if (robot == "O")
			{
				robotPress[0].push_back(button);
				order.push_back(make_pair(0, button));
			}
			else
			{
				robotPress[1].push_back(button);
				order.push_back(make_pair(1, button));
			}
		}
		
		if (robotPress[0].empty())
			robotPress[0].push_back(1);
		else
			robotPress[0].push_back(robotPress[0][robotPress[0].size()-1]);
			
		if (robotPress[1].empty())
			robotPress[1].push_back(1);
		else
			robotPress[1].push_back(robotPress[1][robotPress[1].size()-1]);
	
		//string	debug[2] = {"Orange", "Blue"};
		
		int	robotPos[2] = {1, 1};
		int robotOrder[2] = {0, 0};
		int	sec = 1;
		unsigned int	orderPos = 0;
		while (true)
		{
			//cout << "-- Second " << sec << " - " << orderPos << endl; 
		
			pair<int, int>	p = order[orderPos];
			bool			succeed = false;
			//cout << "Goal: " << debug[p.first] << " press " << p.second << endl;
		
			for (int i = 0; i < 2; i++)
			{
				if ((p.first == i) && (robotPos[p.first] == p.second))
				{
					//cout << debug[p.first] << " presses button " << p.second << endl;
					robotOrder[p.first]++;
					succeed = true;
				}
				else
				{
					int target = robotPress[i][robotOrder[i]];
					if (robotPos[i] != target)
					{
						robotPos[i] += (robotPos[i] > target) ? -1 : 1;
						//cout << debug[i] << " moves to button " << robotPos[i] << endl;
					}
					else
					{
						//cout << debug[i] << " stays at button " << robotPos[i] << endl;
					}
				}
			}
			
			if (succeed) orderPos++;
			if (orderPos == order.size()) break;
			sec++;
		}
		
		cout << "Case #" << (t+1) << ": " << sec << endl;
	}
}

