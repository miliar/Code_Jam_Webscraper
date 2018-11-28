#include <stdio.h>
#include <string>
using namespace std;

string solve() {
	int c[36], o[28]; char co[36];
	int C, D, N;
	scanf("%d", &C);
	for (int i = 0; i < C; i++) {
		char spell[4]; scanf("%s", spell);
		c[i] = (1 << (spell[0] - 'A')) | (1 << (spell[1] - 'A'));
		co[i] = spell[2];
	}
	scanf("%d", &D);
	for (int i = 0; i < D; i++) {
		char spell[4]; scanf("%s", spell);
		o[i] = (1 << (spell[0] - 'A')) | (1 << (spell[1] - 'A'));
	}
	scanf("%d ", &N);
	string result = "";
	int all_mask = 0;
	for (int i = 0; i < N; i++) {
		char s; scanf("%c", &s); s -= 'A';
		int mask = 1 << s;
		if (result.size()) {
			mask |= 1 << (result[result.size() - 1] - 'A');
		} else mask = 0;
		for (int j = 0; j < C; j++) {
			if (mask == c[j]) {
				result[result.size() - 1] = co[j];
				mask = -1;
				break;
			}
		}
		if (mask == -1) {
			all_mask = 0;
			for (int j = 0; j < result.size(); j++) {
				all_mask |= 1 << (result[j] - 'A');
			}
		} else {
			result += string(1, s + 'A');
			all_mask |= 1 << s;
		}
		for (int j = 0; j < D; j++) {
			if ((all_mask & o[j]) == o[j]) {
				result = "";
				all_mask = 0;
				break;
			}
		}
		//printf("%d: %s\n", i, result.c_str());
	}
	return result;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: [", i);
		string result = solve();
		for (int j = 0; j < result.size();
		     printf(++j == result.size() ? "" : ", ")) {
			printf("%c", result[j]);
		}
		puts("]");
	}
	return 0;
}
