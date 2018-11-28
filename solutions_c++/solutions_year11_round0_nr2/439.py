#include <cstdio>
#include <cstring>

using namespace std;

int comb[100][100];
bool oppo[100][100];

int stack[100];
int top;

void solve() {
	int C; scanf("%d", &C);
	memset(comb, -1, sizeof comb);
	for (int i = 0; i < C; i++) {
		char buf[5]; scanf("%s", buf);
		buf[0] -= 'A'; buf[1] -= 'A'; buf[2] -= 'A';

		comb[buf[0]][buf[1]] = comb[buf[1]][buf[0]] = buf[2];
	}

	int D; scanf("%d", &D);
	memset(oppo, 0, sizeof oppo);
	for (int i = 0; i < D; i++) {
		char buf[5]; scanf("%s", buf);
		buf[0] -= 'A'; buf[1] -= 'A';

		oppo[buf[0]][buf[1]] = oppo[buf[1]][buf[0]] = true;
	}

	int N; scanf("%d", &N);
	static char buf[200]; scanf("%s", buf);

	top = 0;
	for (int i = 0; i < N; i++) {
		int x = buf[i] - 'A';
		while (top && comb[stack[top - 1]][x] != -1) {
			x = comb[stack[top - 1]][x];
			top--;
		}

		bool opp = false;
		for (int i = 0; i < top && !opp; i++)
			if (oppo[stack[i]][x])
				opp = true;

		if (opp) top = 0;
		else stack[top++] = x;
	}

	printf("[");
	if (top) printf("%c", stack[0] + 'A');
	for (int i = 1; i < top; i++)
		printf(", %c", stack[i] + 'A');
	printf("]\n");
}


int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
