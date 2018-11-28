#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt)
	{
		int N; scanf("%d", &N);

		char t[64];
		vector <int> X;
		X.clear();
		for (int i = 0; i < N; ++i)
		{
			scanf("%s", t);
			int najdalje = 0;
			for (int k = 0; t[k]; ++k)
			{
				if (t[k] == '1') najdalje = k;
			}
			X.push_back(najdalje);
		}

		int sum = 0;
		for (int i = 0; i < X.size(); ++i)
		{
			int moves = 0;
			for (int j = 0; j < X.size(); ++j)
			{
				if (X[j] == -1) continue;
				if (X[j] <= i)
				{
					X[j] = -1;
					sum += moves;
					break;
				}else{
					++moves;
				}
			}
		}
		printf("Case #%d: %d\n", tt, sum);
	}

	return 0;
}
