/*
 *  Google Code Jam 2008
 *  Round 2 - Problem B - Triangle Areas
 */


#include <stdio.h>
#include <vector>
#include <list>

#define INPUT_FILE	"input.txt"
#define OUTPUT_FILE	"output.txt"

using namespace std;

int T, M, N;
int X0, Y0, X1, Y1, X2, Y2;
long A;



void Solve(int tst)
{
	X0 = 0;
	Y0 = 0;

	for (X1 = 0; X1 <= N; X1++)
		for (Y1 = 0; Y1 <= M; Y1++)
			for (X2 = 0; X2 <= N; X2++)
				for (Y2 = 0; Y2 <= M; Y2++)
				{
					long a = X1 * Y2 - X2 * Y1;

					if (a == A)
					{
						printf("Case #%d: %d %d %d %d %d %d\n", tst, X0, Y0, X1, Y1, X2, Y2);
						return;
					}
				};

	printf("Case #%d: IMPOSSIBLE\n", tst);
}


int main()
{
	int i;


	freopen(INPUT_FILE, "rt", stdin);
	freopen(OUTPUT_FILE, "wt", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		scanf("%d %d %ld", &N, &M, &A);

		Solve(i);
	}

	fclose(stdout);
	fclose(stdin);


	return 0;
}
