#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
	int testCases, n, pos;
	char color[5];

	ios::sync_with_stdio(false);

	cin >> testCases;
	for (int k = 1; k <= testCases; ++ k) {
		int posRobotO = 1, posRobotB = 1;
		int timeRobotO = 0, timeRobotB = 0;

		cin >> n;
		while (n --) {
			cin >> color >> pos;
			if (color[0] == 'O') {
				timeRobotO = max(timeRobotO + abs(posRobotO - pos), timeRobotB) + 1;
				posRobotO = pos;
			} else {
				timeRobotB = max(timeRobotB + abs(posRobotB - pos), timeRobotO) + 1;
				posRobotB = pos;
			}
		}

		cout << "Case #" << k << ": " << max(timeRobotO, timeRobotB) << endl;
	}

	return 0;
}
