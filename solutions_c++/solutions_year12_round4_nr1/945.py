// Google Code Jam 2012 - Round 2
// by vdave, Hungary, 2012

#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;



// PROBLEM A - SWINGING WILD

int vinePos[10240], vineLen[10240];
int maxLen[10240];

void solve_a()
{
	int TC;

	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; tc++)
	{
		int N, D;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d %d", vinePos + i, vineLen + i);
			maxLen[i] = 0;
		}
		scanf("%d", &D);
		maxLen[0] = vinePos[0];

		for (int p = 0; p < N - 1; ++p)
		{
			for (int k = p + 1; k < N; ++k)
			{
				if (vinePos[p] + maxLen[p] >= vinePos[k])
				{
					int lenK = std::min(vineLen[k], vinePos[k]-vinePos[p]);
					if (lenK > maxLen[k])
						maxLen[k] = lenK;
				}
				else
					break;
			}
		}

		bool canReach = false;
		for (int i = 0; i < N; ++i)
		{
			if (vinePos[i] + maxLen[i] >= D)
				canReach = true;
		}

		if (canReach)
		{
			printf("Case #%d: YES\n", tc);
		}
		else
		{
			printf("Case #%d: NO\n", tc);
		}
	}
}








int main(int argc, char *argv[])
{
	solve_a();

	return 0;
}
