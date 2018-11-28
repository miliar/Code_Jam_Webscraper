#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {
	int _43;
	scanf("%d", &_43);
	for (int _ = 0; _ < _43; _++) {
		printf("Case #%d: ", _+1);
		int N;
		scanf("%d", &N);
		int po = 1;
		int pb = 1;
		int to = 0;
		int tb = 0;
		for (int i = 0; i < N; i++) {
			char a;
			int b;
			scanf(" %c %d", &a, &b);
			if (a == 'O') {
				to += abs(po - b);
				po = b;
				to = max(to, tb);
				to++;
			} else {
				tb += abs(pb - b);
				pb = b;
				tb = max(tb, to);
				tb++;
			}
		}
		printf("%d\n", max(tb, to));
	}
	return 0;
}
