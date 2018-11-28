#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		int N, xp[1000], yp[1000], zp[1000], pp[1000];
		gets(inp); sscanf(inp, "%d", &N);
		for (int i = 0; i < N; i++) {
			gets(inp); sscanf(inp, "%d%d%d%d", &(xp[i]), &(yp[i]), &(zp[i]), &(pp[i]));
		}

		double maxd = 0;
		for (int a = 0; a < N; a++) {
			for (int b = a + 1; b < N; b++) {
				maxd = max(maxd, (abs(xp[a] - xp[b]) +
						  abs(yp[a] - yp[b]) +
						  abs(zp[a] - zp[b])) /
					   (double)(pp[a] + pp[b]));
			}
		}

		printf("Case #%d: %lf\n", casenum, maxd);
	}

	return 0;
}

