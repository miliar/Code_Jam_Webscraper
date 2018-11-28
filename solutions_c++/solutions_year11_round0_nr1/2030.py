#include <iostream>
#include <queue>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		cin >> n;
		queue<int> q;
		queue<int> qrob[2];
		for (int j = 0; j < n; ++j)
		{
			char robot[2];
			int pos;
			cin >> robot >> pos;
			q.push(robot[0] == 'O' ? 0 : 1);
			if (robot[0] == 'O') qrob[0].push(pos);
			else qrob[1].push(pos);
		}
		int tm = 0;
		int pos[2] = {1, 1};
		while (!q.empty())
		{
			bool moved = false;
			for (int r = 0; r < 2; r++) {
				if (qrob[r].empty()) continue;
				if (qrob[r].front() == pos[r])
				{
					if (!moved && q.front() == r)
					{
						moved = true;
						q.pop();
						qrob[r].pop();
					}
				}
				else if (qrob[r].front() > pos[r])
					++pos[r];
				else
					--pos[r];
			}
			++tm;
		}
		cout << "Case #" << i << ": " << tm << endl;
	}
	return 0;
}