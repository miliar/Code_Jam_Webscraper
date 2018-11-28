#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

//#define TC_DEBUG

int scores[1024];

int main(int argc, char* argv[])
{
	int T;

	scanf("%d", &T);

	for (int tc = 1; tc <= T; ++tc)
	{
		int N, S, P;
		scanf("%d %d %d", &N, &S, &P);

		for (int i = 0; i < N; ++i)
		{
			scanf("%d", scores + i);
		}
		std::sort(scores, scores + N);

		int countMaxP = 0;
		int PMin = (P == 0) ? (0) : (3 * P - 2);
		int PMin_S = (P == 0) ? (0) : ((P == 1) ? (1) : (3 * P - 4));
		for (int i = N - 1; i >= 0; --i)
		{
			int s = scores[i];
			if (s >= PMin)
			{
				countMaxP++;
			}
			else if (s >= PMin_S && S > 0)
			{
				countMaxP++;
				S--;
			}
		}

		printf("Case #%d: %d\n", tc, countMaxP);
	}

	return 0;
}
