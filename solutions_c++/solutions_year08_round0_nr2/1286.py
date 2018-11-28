
#include <stdio.h>
#include <algorithm>

using namespace std;

int prob, nprob;
int T, NA, NB;
struct TRIP {
	int S, T;
} A[110], B[110];
int X, Y;

struct EVENT {
	int t, d;
} lst[300];


bool cmp(const EVENT &a, const EVENT &b) {
	if (a.t == b.t)
		return a.d > b.d;

	return a.t < b.t;
}

int main() {
//	freopen("b.in", "r", stdin);
//	freopen("b.out", "w", stdout);

	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d%d%d", &T, &NA, &NB);
		for (int i = 0; i < NA; i++) {
			int m1, s1, m2, s2;
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			A[i].S = m1*60+s1; A[i].T = m2*60+s2;
		}
		for (int i = 0; i < NB; i++) {
			int m1, s1, m2, s2;
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			B[i].S = m1*60+s1; B[i].T = m2*60+s2;
		}

		for (int i = 0; i < NA; i++) { lst[i].t = A[i].S; lst[i].d = -1; }
		for (int i = 0; i < NB; i++) { lst[i+NA].t = B[i].T + T; lst[i+NA].d = 1; }
		sort(lst, lst + NA + NB, cmp);
		X = 0; 
		for (int k = 0, i = 0; i < NA + NB; i++) {
			k += lst[i].d;
			if (k < 0) { X += -k; k = 0; }
		}

		for (int i = 0; i < NB; i++) { lst[i].t = B[i].S; lst[i].d = -1; }
		for (int i = 0; i < NA; i++) { lst[i+NB].t = A[i].T + T; lst[i+NB].d = 1; }
		sort(lst, lst + NA + NB, cmp);
		Y = 0;
		for (int k = 0, i = 0; i < NA + NB; i++) {
			k += lst[i].d;
			if (k < 0) { Y += -k; k = 0; }
		}

		printf("Case #%d: %d %d\n", prob, X, Y);
	}

	return 0;
}
