#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int p[1024];

int main()
{
	freopen("f:\\D-small-attempt0.in", "r", stdin);
	freopen("f:\\D-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &p[i]);
			p[i]--;
		}
		bool vst[1024];
		memset(vst, 0, sizeof(vst));
		double res = 0.0;
		for (int k = 0; k < N; k++)
		{
			int ct;
			if (!vst[k])
			{
				vst[k] = true;
				ct = 1;
				int t = p[k];
				while (!vst[t])
				{
					vst[t] = true;
					t = p[t];
					ct++;
				}
				if (ct >= 2)
					res += ct;
			}
		}
		printf("Case #%d: %.6f\n", t_case, res);
	}
	return 0;
}
