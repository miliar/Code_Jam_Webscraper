#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
using namespace std;

int T, N;
int pos[2];
int lastact[2];

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d ", &N);
		pos[0] = pos[1] = 1;
		lastact[0] = lastact[1] = 0;
		int time = 0;
		for (int i = 0; i < N; i++) {
			char c; int p;
			scanf("%c %d ", &c, &p);
			int r = c == 'O' ? 0 : 1;
			time = max(abs(p-pos[r])+lastact[r],time)+1;
			lastact[r] = time;
			pos[r] = p;
		}
		printf("%d\n", time);
	}
	return 0;
}
