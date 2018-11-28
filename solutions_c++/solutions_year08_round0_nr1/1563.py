#include <cstdio>
#include <vector>
#include <string>
using namespace std;

#define MAXQ 1024
#define MAXS 128
#define INF 999999999
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int minv[MAXQ][MAXS];
vector<string> V;

void readAndSolve()
{
	int N, nr = 0;

	for (scanf("%d", &N); N; N--, nr++)
	{
		int S, Q;

		for (int i = 0; i < MAXQ; i++)
			for (int j = 0; j < MAXS; j++)
				minv[i][j] = INF;

		V.clear();
		scanf("%d\n", &S);
		for (int i = 0; i < S; i++)
		{
			char str[512];
			fgets(str, 500, stdin);
			V.push_back(str);
		}

		for (int i = 0; i < S; i++)
			minv[0][i] = 0;
		scanf("%d\n", &Q);
		for (int i = 0; i < Q; i++)
		{
			char str[512];
			fgets(str, 500, stdin);
			for (int j = 0; j < S; j++)
				if (str == V[j])
					minv[i][j] = INF;
			if (i == Q - 1)
				break;

			for (int j = 0; j < S; j++)
				minv[i + 1][j] = minv[i][j];
			int minc = INF;
			for (int j = 0; j < S; j++)
				minc = MIN(minc, minv[i][j]);
			for (int j = 0; j < S; j++)
				minv[i + 1][j] = MIN(minv[i + 1][j], minc + 1);
		}

		int minc = INF;
		for (int j = 0; j < S; j++)
			minc = MIN(minc, minv[Q - 1][j]);
		printf("Case #%d: %d\n", nr + 1, minc);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	readAndSolve();

	return 0;
}