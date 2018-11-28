#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 110;

int t, n;
char c[MAX];
int pos[MAX];
int next[MAX];

int abs(int a)
{
	return a < 0 ? -a : a;
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> c[i] >> pos[i];

		int goal1 = -1, goal2 = -1;

		memset(next, -1, sizeof(next));
		for (int i = 0; i < n; ++i)
		{
			if (c[i] == 'O' && goal1 == -1) goal1 = pos[i];
			if (c[i] == 'B' && goal2 == -1) goal2 = pos[i];

			for (int j = i + 1; j < n; ++j)
				if (c[j] == c[i])
				{
					next[i] = j;
					break;
				}
		}


		int x1 = 0, x2 = 0, t = 0;
		for (int i = 0; i < n; ++i)
		{
			#ifdef DEBUG
			cerr << x1 << ' ' << x2 << endl;
			#endif
			int moves = 0, delta = 1;
			if (c[i] == 'O')
			{
				moves = abs(x1 - goal1) + 1;
				x1 = goal1;
                goal1 = next[i];
                if (goal1 != -1) goal1 = pos[goal1];
                t += moves;
                delta = 1;
                if (goal2 < x2) delta = -1;
                while (goal2 != -1 && x2 != goal2 && moves)
                	x2 += delta, --moves;
			}
			else
			{
				moves = abs(x2 - goal2) + 1;
				x2 = goal2;
                goal2 = next[i];
                if (goal2 != -1) goal2 = pos[goal2];
                t += moves;
                delta = 1;
                if (goal1 < x1) delta = -1;
                while (goal1 != -1 && x1 != goal1 && moves)
                	x1 += delta, --moves;
			}
		}
					
		cout << "Case #" << test << ": " << t - 1 << '\n';
	}

	return 0;
}
