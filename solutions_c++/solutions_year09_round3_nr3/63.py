#include <stdio.h>
#include <algorithm>

using namespace std;

int F[110][110];
int Q[110];
int q_num;
int P;

void cal(int, int);

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int testcases;
	scanf("%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++)
	{
		scanf("%d %d", &P, &q_num);
		for (int i = 1; i <= q_num; i++) scanf("%d", &Q[i]);
		Q[0] = 0;
		Q[q_num + 1] = P + 1;

		memset(F, 255, sizeof F);

		cal(0, q_num + 1);
		printf("Case #%d: %d\n", cases, F[0][q_num + 1]);
	}
	
	return 0;
}

void cal(int p, int q) 
{
	if (F[p][q] != -1) return;

	if (p + 1 == q)
	{
		F[p][q] = 0;
		return;
	}

	int ans = -1;

	for (int r = p + 1; r < q; r++)
	{
		cal(p, r);
		cal(r, q);
		int tmp = F[p][r] + F[r][q];
		if (ans == -1 || tmp < ans) ans = tmp;
	}

	ans += Q[q] -1 - Q[p] - 1;
	F[p][q] = ans;
	return;
}
