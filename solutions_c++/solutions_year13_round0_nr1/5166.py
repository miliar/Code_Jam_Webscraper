#include <cstdio>
#include <cstring>

char data[5][7];
char copy[5][7];

void input() {
	for (int i = 0; i < 4; ++ i) {
		scanf("%s", data[i]);
	}
}

void generate(char s, char t) {
	for (int i = 0; i < 4; ++ i) {
		for (int j = 0; j < 4; ++ j)
			copy[i][j] = data[i][j] == s ? t : data[i][j];
	}
}

bool check(char t) {
	for (int i = 0; i < 4; ++ i) {
		int cnt = 0;
		for (int j = 0; j < 4; ++ j)
			cnt += copy[i][j] == t;
		if (cnt == 4) return true;
	}
	for (int i = 0; i < 4; ++ i) {
		int cnt = 0;
		for (int j = 0; j < 4; ++ j)
			cnt += copy[j][i] == t;
		if (cnt == 4) return true;
	}
	{
		int cnt = 0;
		for (int i = 0; i < 4; ++ i)
			cnt += copy[i][i] == t;
		if (cnt == 4) return true;
	}
	{
		int cnt = 0;
		for (int i = 0; i < 4; ++ i)
			cnt += copy[i][3 - i] == t;
		if (cnt == 4) return true;
	}
	return false;
}

void solve() {
	generate('T', 'O');
	if (check('O')) {
		printf("O won\n");
		return;
	}

	generate('T', 'X');
	if (check('X')) {
		printf("X won\n");
		return;
	}

	{
		bool ok = true;
		for (int i = 0; i < 4; ++ i)
			for (int j = 0; j < 4; ++ j)
				ok = ok && data[i][j] != '.';
		if (ok) {
			printf("Draw\n");
			return;
		}
	}

	printf("Game has not completed\n");
}

int main() {
	int test_cases;
	scanf("%d", &test_cases);
	for (int t = 1; t <= test_cases; ++ t) {
		input();
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
