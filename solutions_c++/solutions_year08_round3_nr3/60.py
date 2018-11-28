#include <cstdio>
#include <string>
#include <vector>

using namespace std;

long long dp[1001][1001];

long long doit(vector <int> &l, int beg, int last)
{
	if (dp[beg][last + 1] >= 0) {
		return dp[beg][last + 1];
	}
	if (beg == l.size()) {
		return (dp[beg][last + 1] = (last >= 0) ? 1 : 0);
	}

	long long num = 0;
	if (last == -1 || l[beg] > l[last]) {
		num += doit(l, beg + 1, beg);
	}
	num = (num + doit(l, beg + 1, last)) % 1000000007;

	//printf("%d %d %I64d\n", beg, last, num);
	return (dp[beg][last + 1] = num);
}

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		int n, m, X, Y, Z;
		gets(inp); sscanf(inp, "%d%d%d%d%d", &n, &m, &X, &Y, &Z);

		vector <int> A;
		for (int i = 0; i < m; i++) {
			int tmp;
			gets(inp); sscanf(inp, "%d", &tmp);
			A.push_back(tmp);
		}
		vector <int> l;
		for (int i = 0; i < n; i++) {
			l.push_back(A[i % m]);
			A[i % m] = ((long long)X * A[i % m] +
				    (long long)Y * (i + 1)) % Z;
		}

		memset(&(dp[0][0]), -1, sizeof(dp));
		long long num = doit(l, 0, -1);

		printf("Case #%d: %I64d\n", casenum, num);
	}

	return 0;
}

