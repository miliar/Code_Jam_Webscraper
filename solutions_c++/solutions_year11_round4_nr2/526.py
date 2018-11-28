#include <stdio.h>
#include <stdint.h>
#include <algorithm>
#include <string.h>

unsigned w[512][512];
unsigned ws[512][512];
unsigned wsi[512][512];
unsigned wsj[512][512];

static void dump (unsigned (&x)[512][512], unsigned R, unsigned C)
{
	putchar ('\n');
	for (unsigned i=0; i<R; ++i) {
		for (unsigned j=0; j<C; ++j)
			printf ("%u ", x[i][j]);
		putchar ('\n');
	}
}

static void work ()
{
	unsigned R, C;

	scanf ("%u%u%*u", &R, &C);

	for (unsigned i=0; i<R; ++i)
		for (unsigned j=0; j<C; ++j) {
			char c;
			scanf (" %c", &c);
			w[i][j] = c - '0';
		}

	memset (ws, 0, sizeof ws);
	memset (wsi, 0, sizeof wsi);
	memset (wsj, 0, sizeof wsj);
	for (unsigned i=0; i<R; ++i) {
		for (unsigned j=0; j<C; ++j) {
			ws[i+1][j+1] = ws[i+1][j] + w[i][j];
			wsi[i+1][j+1] = wsi[i+1][j] + i * w[i][j];
			wsj[i+1][j+1] = wsj[i+1][j] + j * w[i][j];
		}
		for (unsigned j=0; j<=C; ++j) {
			ws[i+1][j] += ws[i][j];
			wsi[i+1][j] += wsi[i][j];
			wsj[i+1][j] += wsj[i][j];
		}
	}

//	dump(w,R,C);
//	dump(ws,R+1,C+1);
//	dump(wsi,R+1,C+1);
//	dump(wsj,R+1,C+1);

	for (unsigned K = std::min(R,C); K>=3; --K) {
		for (unsigned i=0; i<=R-K; ++i) {
			unsigned ic2 = i * 2 + K - 1;
			for (unsigned j=0; j<=C-K; ++j) {
				unsigned jc2 = j * 2 + K - 1;

				int Sj = wsj[i+K][j+K] - wsj[i][j+K] - wsj[i+K][j] + wsj[i][j];
				int Si = wsi[i+K][j+K] - wsi[i][j+K] - wsi[i+K][j] + wsi[i][j];
				int S  = ws [i+K][j+K] - ws [i][j+K] - ws [i+K][j] + ws [i][j];

				int X2 = 2 * Sj - jc2 * S;
				int Y2 = 2 * Si - ic2 * S;

				X2 -= -(K - 1) * w[i][j];
				X2 -= (K - 1) * w[i][j+K-1];
				X2 -= -(K - 1) * w[i+K-1][j];
				X2 -= (K - 1) * w[i+K-1][j+K-1];

				Y2 -= -(K - 1) * w[i][j];
				Y2 -= -(K - 1) * w[i][j+K-1];
				Y2 -= (K - 1) * w[i+K-1][j];
				Y2 -= (K - 1) * w[i+K-1][j+K-1];

//				printf ("K=%u, i=%u, j=%u, X2=%d, Y2=%d\n", K, i, j, X2, Y2);

				if (X2==0 && Y2==0) {
					printf ("%u\n", K);
					return;
				}
			}
		}
	}

	puts ("IMPOSSIBLE");
}

int main ()
{
	int T;
	scanf("%d", &T);
	for (int i=1; i<=T; ++i) {
		printf ("Case #%d: ", i);
		work ();
	}
}
