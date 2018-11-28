#include <cstdio>
#include <algorithm>

#define LENGTH 19
#define MOD 10000

using namespace std;

int main() {
	char pattern[30] = "welcome to code jam";
	char input[500];
	int N; scanf("%d\n",&N);
	for (int caseid = 1; caseid <= N; caseid++) {
		int ans[LENGTH+1];
		for (int i = 0; i <= LENGTH; i++) {ans[i] = 0;}
		ans[0] = 1;
		while (1) {
			char c; scanf("%c",&c);
			if (c == '\n') break;
			//In a vaguely cheaty fashion, observe no two
			//adjacent characters are equal.
			for (int j = 0; j < LENGTH; j++) {
				if (c == pattern[j]) {
					ans[j+1] = (ans[j+1] + ans[j]) % MOD;
				}
			}
		}
		printf("Case #%d: %04d\n",caseid,ans[LENGTH]);
	}
}