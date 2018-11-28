#include <cstdio>
#include <vector>

using namespace std;


int main()
{
	int C;
	scanf("%d", &C);
	for (int h = 1; h <= C; h++)
	{
		vector<int> grps;
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for (int i = 0; i < N; i++)
		{
			int tmp;
			scanf("%d", &tmp);
			grps.push_back(tmp);
		}
		int earned = 0;
		int pos = 0;
		int rmn, stpos;
		for (int i = 0; i < R; i++)
		{
			rmn = k;
			stpos = pos;
			while (rmn >= grps[pos])
			{
				rmn -= grps[pos++];
				if (pos >= N)
					pos = 0;
				if (pos == stpos)
					break;
			}
			earned += k-rmn;
		}
		printf("Case #%d: %d\n", h, earned);
	}
	return 0;
}
