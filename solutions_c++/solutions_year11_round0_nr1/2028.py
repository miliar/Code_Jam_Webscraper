# include <iostream>
# include <deque>
# include <string>

using namespace std;

int abs(int a)
{
	return (a > 0 ? a : -a);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int tests;
	cin >> tests;

	for(int tcase = 1; tcase <= tests; ++tcase)
	{
		int n;
		cin >> n;

		deque< pair<int, int> > blue; //first - button, second - id
		deque< pair<int, int> > orange;

		for(int i = 0; i < n; ++i)
		{
			string c;
			int x;
			cin >> c >> x;
			if (c == "B")
			{
				blue.push_back(make_pair(x, i));
			}
			else
			{
				orange.push_back(make_pair(x, i));
			}
		}

		int bluepos = 1;
		int orangepos = 1;
		int res = 0;

		while (!blue.empty() && !orange.empty())
		{
			++res;
			bool pushed = false;

			if (blue.front().second < orange.front().second && blue.front().first == bluepos)
			{
				blue.pop_front();
				pushed = true;
			}
			else if (bluepos < blue.front().first)
			{
				++bluepos;
			}
			else if (bluepos > blue.front().first)
			{
				--bluepos;
			}

			if (!pushed && blue.front().second > orange.front().second && orange.front().first == orangepos)
			{
				orange.pop_front();
			}
			else if (orangepos < orange.front().first)
			{
				++orangepos;
			}
			else if (orangepos > orange.front().first)
			{
				--orangepos;	
			}
		}

		while (!blue.empty())
		{
			res += abs(blue.front().first - bluepos) + 1;
			bluepos = blue.front().first;
			blue.pop_front();
		}

		while (!orange.empty())
		{
			res += abs(orange.front().first - orangepos) + 1;
			orangepos = orange.front().first;
			orange.pop_front();
		}

		cout << "Case #" << tcase << ": " << res << endl;		
	}

	return 0;
}