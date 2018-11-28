#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

inline int f(char c) {
	if(toupper(c) == 'O') return 0;
	if(toupper(c) == 'B') return 1;
	return -1;
}

int main() {
	int nt0;

	scanf(" %d", &nt0);

	for(int nt = 1; nt <= nt0 ; nt++) {
		int n, k, sum = 0;
		int k0[2] = {1,1};
		int delta[2] = {0,0};
		char c, c0 = '*';

		scanf(" %d", &n);
		while(n--) {
			scanf(" %c %d", &c, &k);
			int j = f(c);

			int time;
			if(c == c0 || c0 == '*') {
				time = abs(k - k0[j]) + 1;
			} else {
				time = max(0, abs(k - k0[j]) - delta[j]) + 1;
			}

			sum += time;
			delta[j] = 0;
			delta[1-j] += time;

			c0 = c;
			k0[j] = k;
		}

		printf("Case #%d: %d\n", nt, sum);
	}

	return 0;
}