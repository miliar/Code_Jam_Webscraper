#include <cstdio>

const int N = 4;
char s[6][6];
char v[6];

bool ended() {
	char win = '1';
	for (int i = 0; i < N; i++) {
		if (v[i] != 'T') {
			if (v[i] == '.') {
				return false;
			}
			if (win == '1') {
				win = v[i];
			}
			if (v[i] != win) {
				return false;
			}
		}
	}
	printf("%c won\n", win);
	return true;
}

void test() {
	for (int i = 0; i < N; i++) {
		scanf("%s", s[i]);
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			v[j] = s[i][j];
		}
		if (ended()) {
			return;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			v[j] = s[j][i];
		}
		if (ended()) {
			return;
		}
	}
	for (int i = 0; i < N; i++) {
		v[i] = s[i][i];
	}
	if (ended()) {
		return;
	}
	for (int i = 0; i < N; i++) {
		v[i] = s[i][N-i-1];
	}
	if (ended()) {
		return;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (s[i][j] == '.') {
				printf("Game has not completed\n");
				return;
			}
		}
	}
	printf("Draw\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
