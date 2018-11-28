#include <iostream>
using namespace std;

int pos[1001];	// <- v
long long val[1001];  // <- res that was before

int g[1001];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int r, k, n;
		scanf("%d %d %d", &r, &k, &n);
		for (int i =0; i < n; ++i)
		{
			scanf("%d", &g[i]);
		}

		for (int i = 0; i < 1001; ++i)
		{
			pos[i] = -1;
		}

		long long res = 0;
		int tobegin = 0;
		bool fperiod = false;
		for (int v = 0; v < r; ++v)
		{
			if ( !fperiod && pos[tobegin] != -1 )
			{
				long long val_p = res - val[tobegin];
				int length = v - pos[tobegin];
				res += val_p * (long long)((r - v) / length);
				r = (r - v) % length;
				if ( !r ) break;
				v = 0;
				fperiod = true;
			}

			pos[tobegin] = v;
			val[tobegin] = res;
			long long tmp = 0;
			bool first = true;
			for (int j = tobegin; ; j = (j+1) % n)
			{
				if ( tmp + g[j] > k || (!first && j == tobegin) )
				{
					tobegin = j;
					res += tmp;
					break;
				}
				else
				{					
					tmp += g[j];
				}
				first = false;
			}

		}

		printf("Case #%d: %lld\n", t+1, res);

	}


	return 0;
}