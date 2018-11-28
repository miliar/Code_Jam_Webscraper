#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;

int N, C;
double Combi[50][50];
double E[50];

void input()
{
	int i, j;
	scanf("%d%d", &C, &N);
	
	for (i = 0; i <= C; i++) {
		Combi[i][0] = Combi[i][i] = 1;
		for (j = 1; j < i; j++) Combi[i][j] = Combi[i-1][j] + Combi[i-1][j-1];
	}
}

void process()
{
	int i, j;
	E[0] = 0;

	for (i = 1; i <= C; i++) {
		double p, e = 0;

		for (j = i - N; j < i; j++) if (j >= 0) {
			int fix = i - j;
			if (N - fix > C - i) continue;
			e += (1 + E[j]) * Combi[i][fix] * Combi[C-i][N-fix] / Combi[C][N];
		}

		if (N <= C - i)
			p = Combi[C-i][N]/Combi[C][N];
		else p = 0;
		E[i] = (e+p) / (1-p);
	}

	printf("%.9lf\n", E[C]);
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}

