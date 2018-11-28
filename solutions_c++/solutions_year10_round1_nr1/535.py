#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 55

using namespace std;

int main () {
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N, K;
		scanf ("%d%d", &N, &K);
		char m[MAX][MAX];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				scanf (" %c", &m[i][j]);
		for (int i = 0; i < N; i++)
			for (int j = N-2; j >= 0; j--)
				if (m[i][j] == 'R' || m[i][j] == 'B') {
					for (int k = j+1; k < N; k++) {
						if (m[i][k] == '.') {
							m[i][k] = m[i][k-1];
							m[i][k-1] = '.';
						}
						else
							break;
					}
				}
		/*for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++)
				printf ("%c", m[i][j]);
			printf ("\n");
		}*/
		int v = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (m[i][j] != '.') {
					int k, deu = 0;
					for (k = 1; k < K; k++)
						if (j+k >= N || m[i][j+k] != m[i][j])
							break;
					if (k == K)
						deu = 1;
					for (k = 1; k < K; k++)
						if (i+k >= N || m[i+k][j] != m[i][j])
							break;
					if (k == K)
						deu = 1;
					for (k = 1; k < K; k++)
						if (i+k >= N || j+k >= N || m[i+k][j+k] != m[i][j])
							break;
					if (k == K)
						deu = 1;
					for (k = 1; k < K; k++)
						if (i + k >= N || j - k < 0 || m[i+k][j-k] != m[i][j])
							break;
					if (k == K)
						deu = 1;
					if (deu && m[i][j] == 'R')
						v |= 1;
					if (deu && m[i][j] == 'B')
						v |= 2;
				}
		printf ("Case #%d: ", t);
		if (v == 0)
			printf ("Neither\n");
		if (v == 1)
			printf ("Red\n");
		if (v == 2)
			printf ("Blue\n");
		if (v == 3)
			printf ("Both\n");
	}
	return 0;
}

