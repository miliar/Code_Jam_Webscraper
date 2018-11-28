#include <cstdio>

#define p(R) (R=='O'?pO:pB)
#define f(R) (R=='O'?fO:fB)
#define nf(R) (R!='O'?fO:fB)
#define dist(x, y) (x<y?y-x:x-y)

int T;


int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int N, P;
		char R;
		int pO = 1, pB = 1;
		int fO = 0, fB = 0;
		int steps = 0;
		scanf("%d", &N);
		for (int j = 0; j < N; j++)
		{
			scanf(" %c %d", &R, &P);
			int dist = dist(p(R), P);
			int step;
			if (dist < f(R)) step = 1;
			else step = dist-f(R)+1;
			steps += step;
			f(R) = 0;
			p(R) = P;
			nf(R) += step;
			/*printf("Round %d: %c %d; Steps: %d fO %d fB %d\n",
				j, R, P, step, fO, fB);*/
		}
		printf("Case #%d: %d\n", i, steps);
	}
	return 0;
}
