#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int maxn = 110;
const string msg[] = {"X won","O won","Draw","Game has not completed"};
char buf[10][10];

bool win(char ch) {
	for (int i = 0; i < 4; i++) {
		int cnt = 0;
		for (int j = 0; j < 4; j++) {
			if (buf[i][j] == 'T' || buf[i][j] == ch) {
				cnt++;
			}
		}
		if (cnt == 4)
			return true;
	}
	for (int i = 0; i < 4; i++) {
		int cnt = 0;
		for (int j = 0; j < 4; j++) {
			if (buf[j][i] == 'T' || buf[j][i] == ch) {
				cnt++;
			}
		}
		if (cnt == 4)
			return true;
	}
	int cnt = 0;
	for (int i = 0; i < 4; i++) {
		if (buf[i][i] == 'T' || buf[i][i] == ch) {
			cnt++;
		}
	}
	if (cnt == 4)
		return true;
	cnt = 0;
	for (int i = 0; i < 4; i++) {
		int j = 3 - i;
		if (buf[i][j] == 'T' || buf[i][j] == ch) {
			cnt++;
		}
	}
	if (cnt == 4)
		return true;
	return false;
}

bool draw() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (buf[i][j] == '.')
				return false;
		}
	}
	return true;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	int nc = 0;
	scanf("%d", &T);
	while (T--) {
		for (int i = 0; i < 4; i++)
			scanf("%s", buf[i]);
		printf("Case #%d: ", ++nc);
		if (win('X') && win('O'))
			printf("%s\n",  msg[3].c_str());
		else if (win('X'))
			printf("%s\n",  msg[0].c_str());
		else if (win('O'))
			printf("%s\n",  msg[1].c_str());
		else if (draw())
			printf("%s\n",  msg[2].c_str());
		else
			printf("%s\n",  msg[3].c_str());
	}
	return 0;
}
