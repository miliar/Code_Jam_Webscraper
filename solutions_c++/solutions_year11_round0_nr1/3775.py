#include <iostream>
using namespace std;

int main()
{
	int cases;

	cin >> cases;

	int n;

	int op[100][2];

	char o;
	int p;

	for(int c = 0; c < cases; c++)
	{
		cin >> n;

		int time[2];
		int pos[2];

		for(int i = 0; i < n; i++)
		{
			cin >> o >> p;

			if (o == 'O')
				op[i][0] = 0;
			else
				op[i][0] = 1;

			op[i][1] = p;
		}

		time[0] = time[1] = 0;
		pos[0] = pos[1] = 1;


		for(int i = 0; i < n; i++)
		{
			int player = op[i][0];
			int playerPos = op[i][1];
			time[player] += abs(playerPos - pos[player]) + 1;
			pos[player] = playerPos;

			if (time[player] <= time[1 - player])
				time[player] = time[1 - player] + 1;
		}

		cout << "Case " << "#" << c + 1 << ": " << max(time[0], time[1]) << endl;
	}

	return 0;
}
