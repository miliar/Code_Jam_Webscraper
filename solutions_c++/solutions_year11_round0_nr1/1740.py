#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <bitset>
using namespace std;

typedef pair<int, int> pii;

const bool DEBAG_OUTPUT = false;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	

	for (int t = 0; t < T; ++ t)
	{
		int n;
		cin >> n;

		if (DEBAG_OUTPUT)
			cout << "Start of output of Case #" << t + 1 << '\n';

		vector<pii> orangeTask;
		vector<pii> blueTask;
		
		for (int i = 0; i < n; ++ i)
		{
			char c;
			int k;

			cin >> c >> k; 
			if (c == 'O')
				orangeTask.push_back(pii(k, i));
			else
				blueTask.push_back(pii(k, i));
		}

		int curBlueTask = 0;
		int curOrangeTask = 0;

		int blue = 1;
		int orange = 1;

		int ans = 0;

		while (curBlueTask < (int)blueTask.size() || curOrangeTask < (int)orangeTask.size())
		{
			if (DEBAG_OUTPUT)
				cout << "Step #" << ans + 1 << ":\t";
			bool incBlue = false;
			bool incOrange = false;
			if (curBlueTask != (int)blueTask.size())
			{
				if (blue == blueTask[curBlueTask].first &&
					(curOrangeTask == (int)orangeTask.size() || blueTask[curBlueTask].second < orangeTask[curOrangeTask].second))
				{
					incBlue = true;
					if (DEBAG_OUTPUT)
						cout << "Blue robor push button " << blue << '\t';
				}
				else if (blue < blueTask[curBlueTask].first)
				{
					blue ++;
					if (DEBAG_OUTPUT)
						cout << "Blue robor move to button " << blue << '\t';
				}
				else if (blue > blueTask[curBlueTask].first)
				{
					blue --;
					if (DEBAG_OUTPUT)
						cout << "Blue robor move to button " << blue << '\t';
				}
			}
			if (curOrangeTask != (int)orangeTask.size())
			{
				if (orange == orangeTask[curOrangeTask].first &&
					(curBlueTask == (int)blueTask.size() || orangeTask[curOrangeTask].second < blueTask[curBlueTask].second))
				{
					incOrange = true;
					if (DEBAG_OUTPUT)
						cout << "Orange robor push button " << orange << '\t';
				}
				else if (orange < orangeTask[curOrangeTask].first)
				{
					orange ++;
					if (DEBAG_OUTPUT)
						cout << "Orange robor move to button "  << orange << '\t';
				}
				else if (orange > orangeTask[curOrangeTask].first)
				{
					orange --;
					if (DEBAG_OUTPUT)
						cout << "Orange robor move to button " << orange << '\t';
				}
				
			}
			if (DEBAG_OUTPUT)
				cout << '\n';
			if (incBlue)
				curBlueTask ++;
			if (incOrange)
				curOrangeTask ++;
			ans ++;
		}

		cout << "Case #" << t + 1 << ": " << ans << '\n';
	}

	return 0;
}
