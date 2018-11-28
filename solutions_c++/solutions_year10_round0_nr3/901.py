#include <iostream>
#include <cstdio>

using namespace std;

int a[1000];
int pos[1000];
int g[1000];

int main()
{
	int T;
	scanf("%d", &T);
	int R, k, N;
	for (int qn = 1; qn  <= T; ++qn)
	{
		scanf("%d %d %d", &R, &k, &N);
		int s = 0;
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &g[i]);
			s += g[i];
		}

		if (k > s) k = s;

		for (int i = 0; i < N; ++i)
		{
			int ss = 0;
			//int ss = (k / s) * s;
			for (int j = i; ; j = (j + 1) % N)
			{
				if (ss + g[j] > k)
				{
					pos[i] = j % N;
					a[i] = ss;
					break;
				}
				ss += g[j];
			}
		}

		int state = 0;
		long long ret = 0;
		for (int i = 0; i < R; ++i)
		{
			ret += a[state];
			state = pos[state];
		}
		printf("Case #%d: ", qn);
		cout << ret << endl;
	}
}
