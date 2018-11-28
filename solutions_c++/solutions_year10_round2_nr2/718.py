#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("out.txt", "w");
	int ts, tc;
	int N, K, B, T;
	int i, j;
	int pos[55], spd[55];
	vector <int> res;
	fscanf(in, "%d", &ts); fgetc(in);
	for (tc = 1; tc <= ts; ++tc)
	{
		res.clear();
		fscanf(in, "%d %d %d %d", &N, &K, &B, &T);
		for (i = 0; i < N; ++i)
			fscanf(in, "%d", &pos[i]);
		for (i = 0; i < N; ++i)
		{
			fscanf(in, "%d", &spd[i]);
		}
		for (i = N - 1; i >= 0; --i)
		{
			if ((double)(B - pos[i]) / spd[i] <= T)
			{
				int temp = 0;
				for (j = i + 1; j < N; ++j)
				{
					if ((double)(B - pos[j]) / spd[j] > T)
					{
						++temp;
					}
				}
				res.push_back(temp);
			}
		}
		if (res.size() < K)
		{
			fprintf(out, "Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		sort(res.begin(), res.end());
		for (i = j = 0; i < K; ++i)
		{
			j += res[i];
		}
		fprintf(out, "Case #%d: %d\n", tc, j);
	}
	fclose(in);
	fclose(out);
	return 0;
}

