#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

int P, W, i, j, k, a, b;
int d[401][401];
bool t[401][401];
int ms, mt, depth;
bool was[401];
int threat[401];

void go(int kam) {
	int i, j;
	if (was[kam]) return;
	was[kam] = true;
	for (i = 0; i < P; i++) {
		if (t[i][kam]) threat[i]++;
	}

	if (depth == ms && t[kam][1]) {
		j = 0;
		for (i = 0; i < P; i++) {
			if (threat[i] > 0 && !was[i]) j++;
		}
		if (mt < j) mt = j;
		for (i = 0; i < P; i++) {
			if (t[i][kam]) threat[i]--;
		}
		was[kam] = false;
		return;
	}
	if (depth >= ms) {
		for (i = 0; i < P; i++) {
			if (t[i][kam]) threat[i]--;
		}
		was[kam] = false;

		return;
	}

	for (i = 0; i < P; i++) {
		if (threat[i] > 0) {
			depth++;
			go(i);
			depth--;
		}
	}
	for (i = 0; i < P; i++) {
		if (t[i][kam]) threat[i]--;
	}
	was[kam] = false;
}

int main() {
	int kejs, kejsis;
	scanf("%d", &kejsis);
	for (kejs = 1; kejs <= kejsis; kejs++) {
		scanf("%d%d", &P, &W);
		for (i = 0; i < P; i++) {
			for (j = 0; j < P; j++) {
				d[i][j] = 987654321;
				t[i][j] = false;
			}
			d[i][i] = 0;
			was[i] = false;
			threat[i] = false;
		}
		for (i = 0; i < W; i++) {
			scanf("%d,%d", &a, &b);
			if (a==b) printf("ASDASDSA");
			d[a][b] = d[b][a] = 1;
			t[a][b] = t[b][a] = 1;
		}
		for (k = 0; k < P; k++) {
			for (i = 0; i < P; i++) {
				for (j = 0; j < P; j++) {
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}
		/*
		for (i = 0; i < P; i++) {
			for (j = 0; j < P; j++) {
				printf("%d ", d[i][j]);
			}
			printf("\n");
		}
*/
		ms = 987654321;
		for (i = 0; i < P; i++) {
			if (t[i][1] == true && ms > d[i][0]) ms = d[i][0];
		}
		mt = 0; depth = 0;
		go(0);
		printf("Case #%d: ", kejs);
		printf("%d %d\n", ms, mt);
	}
	return 0;
}


