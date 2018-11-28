#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cassert>
#define pow2(a) ((a)*(a))
using namespace std;

struct pos {
	double r;
	double x, y;
} t[1000 + 3];

int N, W, L;

bool interesect(int a, int b) {
	//double p1 = pow2(t[a].r - t[b].r);
	return pow2(t[a].x - t[b].x) + pow2(t[a].y - t[b].y)
			<= pow2(t[a].r + t[b].r) + 1e-5;
	//return /*p1 <= p2 &&*/p2 <= p3 + 1e-5;
}

bool found() {
	for (int i = 0; i < N; i++) {
		t[i].x = double(1 + rand() % (W - 1));
		t[i].y = double(1 + rand() % (L - 1));
		for (int j = 0; j < i; j++)
			if (interesect(j, i) == true)
				return false;
	}
	return true;
}

void solve() {
	scanf("%d%d%d", &N, &W, &L);
	for (int i = 0, r; i < N; i++) {
		scanf("%d", &r);
		t[i].r = double(r);
	}

	srand((unsigned) time(NULL));

	while (1) {
		if (found())
			break;
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (i != j)
				assert(interesect(i,j) == false);

	for (int i = 0; i < N; i++) {
		printf(" %lf %lf", t[i].x, t[i].y);
		assert(t[i].x >= 0);
		assert(t[i].x + 1e-6 <= double(W));
		assert(t[i].y >= 0);
		assert(t[i].y + 1e-6 <= double(L));
	}

	/*
	 for (int i = 0; i < N; i++) {

	 }

	 sort(t, t + N);

	 t[0].x = 0;
	 t[0].y = 0;
	 if (N == 1)
	 return;
	 t[1].x = 0;
	 t[1].y = L;
	 if (N == 2)
	 return;
	 t[2].x = W;
	 t[2].y = 0;
	 if (N == 3)
	 return;
	 t[3].x = W;
	 t[3].y = L;
	 if (N == 4)
	 return;

	 posX[N-1] =

	 for (int i = N - 1; i >= max(0, N - 4);
	 i--
	 )

	 for (int i = 0; i <= W;
	 i++
	 )
	 for (int j = 0; j <= L;
	 j++
	 )
	 t[i][j] = 0;

	 int minw = 0;
	 int minl = 0;
	 for (int i = N - 1; i >= 0; i--) {

	 for			(int w=0; w<=W; w++)
	 for(int l=0; l<=L; l++)

	 }
	 */
}

int main() {
	int ilz;
	scanf("%d", &ilz);
	for (int xz = 1; xz <= ilz; xz++) {
		printf("Case #%d:", xz);
		solve();
		printf("\n");
	}
	return 0;
}
