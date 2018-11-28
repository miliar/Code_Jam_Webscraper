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
		int N, M, A;
		gets(inp); sscanf(inp, "%d%d%d", &N, &M, &A);

		int noresult = 1;
		for (int x1 = 0; x1 <= N; x1++) {
			for (int y1 = 0; y1 <= M; y1++) {
				for (int x2 = 0; x2 <= N; x2++) {
					for (int y2 = 0; y2 <= M; y2++) {
						if (abs(x1 * y2 - x2 * y1) == A) {
							printf("Case #%d: %d %d %d %d %d %d\n", casenum,
							       0, 0, x1, y1, x2, y2);
							noresult = 0;
							break;
						}
					}
					if (!noresult) break;
				}
				if (!noresult) break;
			}
			if (!noresult) break;
		}

		if (noresult) {
			printf("Case #%d: IMPOSSIBLE\n", casenum);
		}
	}

	return 0;
}

