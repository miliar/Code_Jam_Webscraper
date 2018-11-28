#include <iostream>
#include <cmath>

using namespace std;

void main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int n, m, posO, posB, timeO, timeB, button, time, temp;
	char robot;
	cin >> n;

	for (int i = 0; i < n; i++) {
		posO = 1;
		posB = 1;
		timeO = 0;
		timeB = 0;
		time = 0;
		cin >> m;
		for (int j = 0; j < m; j++) {
			cin >> robot >> button;
			if (robot == 'O') {
				temp = abs(button - posO);
				temp -= (time - timeO);
				time += max(temp, 0) + 1;
				timeO = time;
				posO = button;
			}
			else if (robot == 'B') {
				temp = abs(button - posB);
				temp -= (time - timeB);
				time += max(temp, 0) + 1;
				timeB = time;
				posB = button;
			}
			else ; //There is bad day...
		}
		cout << "Case #" << (i + 1) << ": " << time << endl;
	}
}