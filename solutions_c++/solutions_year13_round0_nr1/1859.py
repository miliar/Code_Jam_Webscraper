#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int N = 4;
char table[N][N];
string str[4] = {"X won", "O won", "Draw", "Game has not completed"};

inline int toint(const char ch) {
	if (ch == 'X')
		return 0;
	if (ch == 'O')
		return 1;
	if (ch == 'T')
		return 2;
	if (ch == '.')
		return 3;
	return -1;
}

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; t ++) {
		bool end = true;
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < N; j ++) {
				cin >> table[i][j];
				end &= (table[i][j] != '.');
			}

		int ans = 2;
		
		for (int i = 0; i < N; i ++) {
			// Row from table[i][0]
			int cnt[4] = {0};
			for (int j = 0; j < N; j ++)
				cnt[toint(table[i][j])] ++;
			
			if (cnt[0] + cnt[2] == 4)
				ans = 0;
			if (cnt[1] + cnt[2] == 4)
				ans = 1;
		}

		for (int i = 0; i < N; i ++) {
			// Column from table[0][i]
			int cnt[4] = {0};
			for (int j = 0; j < N; j ++)
				cnt[toint(table[j][i])] ++;
			
			if (cnt[0] + cnt[2] == 4)
				ans = 0;
			if (cnt[1] + cnt[2] == 4)
				ans = 1;
		}

		// table[i][i] diagonal
		int cnt[4] = {0};
		for (int i = 0; i < N; i ++)
			cnt[toint(table[i][i])] ++;
		if (cnt[0] + cnt[2] == 4)
			ans = 0;
		if (cnt[1] + cnt[2] == 4)
			ans = 1;

		// table[i][N - i - 1] diagonal
		cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
		for (int i = 0; i < N; i ++)
			cnt[toint(table[i][N - i - 1])] ++;
		if (cnt[0] + cnt[2] == 4)
			ans = 0;
		if (cnt[1] + cnt[2] == 4)
			ans = 1;

		if (ans == 2 && !end)
			ans = 3;

		cout << "Case #" << t + 1 << ": " << str[ans] << endl;
	}

	return 0;
}

