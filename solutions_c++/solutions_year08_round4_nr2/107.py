#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <set>
#include <math.h>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int MAX = 100000000;
int MAXDIM = 10000;

set<int> factorable;

int main()
{
	int numCase;
	scanf("%d", &numCase);
	int i, j, N, M, A;

	for (i = 0; i < numCase; i++)
	{
		scanf("%d %d %d", &N, &M, &A);
		int x1, x2, y1, y2;
		printf("Case #%d: ", i+1);
		bool found = false;
		for (y1 = -M; y1 <= M; y1++)
			for (y2 = -M; y2 <= M; y2++)
			{
				int minY = y1, maxY = y1;
				if (y2 < minY) minY = y2;
				if (0 < minY) minY = 0;
				if (y2 > maxY) maxY = y2;
				if (0 > maxY) maxY = 0;
				if (maxY - minY > M) continue;
				for (x1 = 0; x1 <= N; x1++)
					for (x2 = 0; x2 <= N; x2++)
					{
						if (abs(x1 * y2 - x2 * y1) == A && !found)
						{
							y2 -= minY;
							y1 -= minY;
							printf("%d %d %d %d %d %d\n", 0, -minY, x1, y1, x2, y2);
							found = true;
						}
					}
				}
		if (!found)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}

