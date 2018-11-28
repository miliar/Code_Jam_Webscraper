#include <cstdio>
#include <map>
#include <cstring>
#include <cassert>


#define sz(c) (int)c.size()
using namespace std;

const int n = 4;
char str[n + 1][n + 1];

int full() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (str[i][j] == '.') 
				return 0;
	return 1;
}

int win(char c) {
	int cnt = 0;
	for (int i = 0; i < n; i++)
		cnt += str[i][i] == c || str[i][i] == 'T';
	if (cnt == 4) return 1;
	cnt = 0;
	for (int i = 0; i < n; i++)
		cnt += str[i][n - i - 1] == c || str[i][n - i - 1] == 'T';
	if (cnt == 4) return 1;
	for (int i = 0; i < n; i++) {
		cnt = 0;
		for (int j = 0; j < n; j++) 
			cnt += str[i][j] == c || str[i][j] == 'T';
		if (cnt == 4) return 1;
	}
	for (int j = 0; j < n; j++) {
		cnt = 0;
		for (int i = 0; i < n; i++) 
			cnt += str[i][j] == c || str[i][j] == 'T';
		if (cnt == 4) return 1;
	}
	return 0;
}

int go(int turn, int a, int b) {
  /*  fprintf(stderr, "[%d,%d] %c\n", a, b, "XO"[turn]);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			fprintf(stderr ,"%c", str[i][j]);
		fprintf(stderr, "\n");
	}*/
//	fprintf(stderr, "####\n");
	if (win("XO"[turn ^ 1])) return -1;
	if (full()) return 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (str[i][j] == '.') {
				str[i][j] = "XO"[turn];
				int res = -go(turn ^ 1, -b, -a);
				a = max(a, res);
				str[i][j] = '.';
				if (a >= b) return a;
			}
		} 
	}
	return a;
}

int main() {
	int _; scanf("%d\n", &_);
	for (int test = 1; test <= _; test++) {
		for (int i = 0; i < n; i++) {
			scanf("%s", str[i]);
		}
		int cnt = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cnt ^= (str[i][j] == 'X') || (str[i][j] == 'O');
		if (win('X')) {
			printf("Case #%d: X won\n", test);
		}else if(win('Y')){
			printf("Case #%d: O won\n", test);
		}else if(full()) {
			printf("Case #%d: Draw\n", test);
		} else {
			int val = go(cnt, -2, 2);
			if (val != 0) {
				printf("Case #%d: %c won\n", 
						test, "XO"[cnt ^ (val == -1)]);
			} else {
				printf("Case #%d: Game has not completed\n", test);
			}
		}
	}
	return 0;
}
