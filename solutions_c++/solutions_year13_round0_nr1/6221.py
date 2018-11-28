#include <iostream>

using namespace std;

void print(int a[][6]) {
	return;
	for(int i = 0; i < 5; i++) {
		for (int j = 0; j < 4; j++) {
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void test(int t)
{
	int a[6][6];
	char c;
	string s;
	bool flag = false;
	int sum = 0;
	string save[4];
	for (int i = 0; i < 4; i++) {
		cin >> save[i];
	}

	for (int i = 0; i < 4; i++) {
		s = save[i];
		sum = 0;
		for (int j = 0; j < 4; j++) {
			if (s[j] == 'X') {
				a[i][j] = 1;
			}
			if (s[j] == 'O') {
				a[i][j] = -1;
			}
			if (s[j] == 'T') {
				a[i][j] = 0;
			}
			if (s[j] == '.') {
				a[i][j] = 100;
				flag = true;
			}
			sum += a[i][j];
		}
		a[i][4] = sum;
		if (sum == 4 || sum == 3) {
			cout << "Case #" << t << ": X won" << endl;
			print(a);
			return;
		}
		if (sum == -4 || sum == -3) {
			cout << "Case #" << t << ": O won" << endl;
			print(a);
			return;
		}
	}

	for (int i = 0; i < 4; i++) {
		sum = 0;
		for (int j = 0; j < 4; j++) {
			sum += a[j][i];
		}
		a[4][i] = sum;
		if (sum == 4 || sum == 3) {
			cout << "Case #" << t << ": X won" << endl;
			print(a);
			return;
		}
		if (sum == -4 || sum == -3) {
			cout << "Case #" << t << ": O won" << endl;
			print(a);
			return;
		}
	}
	int sum2 = 0;
	sum = 0;
	for (int i = 0; i < 4; i++) {
		sum += a[i][i];
		sum2 += a[i][4 - i - 1];
	}
	if (sum == 4 || sum == 3) {
		cout << "Case #" << t << ": X won" << endl;
			print(a);
		return;
	}
	if (sum == -4 || sum == -3) {
		cout << "Case #" << t << ": O won" << endl;
			print(a);
		return;
	}
	if (sum2 == 4 || sum2 == 3) {
		cout << "Case #" << t << ": X won" << endl;
			print(a);
		return;
	}
	if (sum2 == -4 || sum2 == -3) {
		cout << "Case #" << t << ": O won" << endl;
			print(a);
		return;
	}

	if (flag) {
		cout << "Case #" << t << ": Game has not completed" << endl;
			print(a);
	}
	else {
		cout << "Case #" << t << ": Draw" << endl;
			print(a);
	}

	return;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		test(i);
	}
}
