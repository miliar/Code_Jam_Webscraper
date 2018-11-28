#include <cstdio>

int N, M, A;

int main () {
	int tc;
	scanf ("%d", &tc);


	for (int ctc = 1; ctc <= tc; ++ctc) {
		scanf ("%d %d %d", &N, &M, &A);
	
		for (int x2 = 0; x2 <= N; ++x2)
			for (int x3 = 0; x3 <= N; ++x3)
				for (int y2 = 0; y2 <= M; ++y2)
					for (int y3 = 0; y3 <= M; ++y3)
						if (x2 * y3 - y2 * x3 == A) {
							printf ("Case #%d: 0 0 %d %d %d %d\n", ctc, x2, y2, x3, y3);
							goto nxt;
						}
		printf ("Case #%d: IMPOSSIBLE\n", ctc);
		nxt:;
	}

	return 0;
}
