#include <iostream>

using namespace std;

int main()
{
	int T, N, C;
	int i, j;
	int AC, XC, min;

	cin >> T;
	for(i = 1; i <= T; i++) {
		cin >> N;
		AC = XC = 0;
		min = 10E7;
		for (j = 0; j < N; j++) {
			cin >> C;
			AC += C;
			XC ^= C;
			if (C < min) {
				min = C;
			}
		}
		cout << "Case #" << i << ": ";
		if (XC == 0) {
			cout << AC - min;
		} else  {
			cout << "NO";
		}
		cout << endl;

	}
}