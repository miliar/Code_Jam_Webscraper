#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int ans[200][2];
int N;

int main() {
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		scanf("%d", &N);

		char ch[10];
		int pos;
		for (int i=0; i<N; ++i) {
			scanf("%s%d", ch, &pos);
			//printf("%c\n", ch);
			if (ch[0] == 'O') {
				ans[i][0] = 0;
			}
			else {
				ans[i][0] = 1;
			}
			ans[i][1] = pos;
		}

		int x = 1, y = 1, ret = 0;
		int tx = 0, ty = 0;

		for (int i=0; i<N; ++i) {
			if (ans[i][0] == 0) {
				int t = max(0, abs(x - ans[i][1]) - tx) + 1;
				ret += t;
				ty += t;
				tx = 0;
				x = ans[i][1];
			}
			else {
				int t = max(0, abs(y - ans[i][1]) - ty) + 1;
				ret += t;
				tx += t;
				ty = 0;
				y = ans[i][1];
			}
		}
		printf("Case #%d: %d\n", t+1, ret);
	}
	return 0;
}
