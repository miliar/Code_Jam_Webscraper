#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

#define MAX 20

typedef pair<int,int> pii;

int geti() { int n; scanf("%d", &n); return n; }
double getd() { double n; scanf("%L", &n); return n; }

#define i(n) for (int i = 0; i < (n); i++)
#define j(n) for (int j = 0; j < (n); j++)

char line[100];

int N, P, Q;
int R[102];
int C[102][102];

void setup() {
	P = geti();
	Q = geti();
	i(Q) {
		R[i+1] = geti();
	}
	R[0] = 0;
	R[Q+1] = P+1;
	memset(C, -1, 102*102 * sizeof(int));
}

int doIt(int lower, int upper) {
	if (upper - lower == 1) {
		C[lower][upper] = 0;
	} else if (upper - lower == 2) {
		C[lower][upper] = R[upper] - R[lower] - 2;
	} else if (C[lower][upper] == -1) {
		int bribe = 1000000000;
		for (int i = lower + 1; i < upper; i++) {
			bribe = min(bribe, doIt(lower, i) + doIt(i, upper));
		}
		bribe += R[upper] - R[lower] - 2;
		C[lower][upper] = bribe;
	}
	return C[lower][upper];
}

int Case;

void print() {
	printf("Case #%d: %d\n", Case, C[0][Q+1]);
}

int main() {

	//freopen("C-test.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	N = geti();

	getc(stdin);

	for (Case = 1; Case <= N; Case++) {
		setup();
		doIt(0, Q+1);
		print();
	}
}