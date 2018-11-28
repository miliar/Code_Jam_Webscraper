#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

string toString(int val)
{
    ostringstream oss;
    oss << val;
    return oss.str();
}

int fromString(const std::string& s) 
{
  istringstream iss(s);
  int res;
  iss >> res;
  return res;
}

int main() 
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";
		int n;
		cin >> n;
		vector <pair <char, int> > movies(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> movies[i].first >> movies[i].second;
		}
		int time = 0;
		int timeOrange = 0, timeBlue = 0;
		int buttonOrange = 1, buttonBlue = 1;
		for (int i = 0; i < n; ++i)
		{
			if (movies[i].first == 'O')
			{
				int dis = abs(movies[i].second - buttonOrange);
				buttonOrange = movies[i].second;
				if (time >= timeOrange + dis)
				{
					++time;
					timeOrange = time;
				}
				else
				{
					time = timeOrange + dis + 1;
					timeOrange = time;
				}
			}
			else
			{
				int dis = abs(movies[i].second - buttonBlue);
				buttonBlue = movies[i].second;
				if (time >= timeBlue + dis)
				{
					++time;
					timeBlue = time;
				}
				else
				{
					time = timeBlue + dis + 1;
					timeBlue = time;
				}
			}
		}
		cout << time << endl;
	}
	
	
	return 0;
}







