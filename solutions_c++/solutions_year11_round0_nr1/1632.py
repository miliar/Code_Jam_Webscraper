#include <cstdio>
#include <cstdlib>

#include <algorithm>

using namespace std;

int n, pos[100];
char C[100];

void input() {
	scanf("%d", &n);
	char buf[16];

	for(int i = 0;i < n;i ++) {
		scanf("%s", buf);
		scanf("%d", &pos[i]);
		C[i] = buf[0];
	}
}

void solve() {
	int npos[2], ans = 0;
	npos[0] = 1, npos[1] = 1;

	for(int i = 0;i < n;i ++) {
		int id = 1;
		if(C[i] == 'O') id = 0;

		int nextP = -1;
		for(int j = i;j < n;j ++) if(C[j] != C[i]) {
			nextP = j;
			break;
		}

		int step = abs(npos[id] - pos[i]) + 1;
		ans += step;
		npos[id] = pos[i];

		if(nextP != -1) {
			nextP = pos[nextP];
			if(abs(nextP - npos[1-id]) > step) {
				if(nextP > npos[1-id]) npos[1-id] += step;
				else npos[1-id] -= step;
			}
			else npos[1-id] = nextP;
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;cas <= T;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}