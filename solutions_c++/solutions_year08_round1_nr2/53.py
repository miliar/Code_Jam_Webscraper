#include <iostream>
using namespace std;

int w[105][105];

int cnt(int x)
{
	int ret = 0;
	while (x)
	{
		ret += (x % 2);
		x /= 2;
	}
	return ret;
}

int tst(int x, int p)
{
	if (x & (1 << p)) return 1; else return 0;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
	{
		int N, M;
		cin >> N >> M;
		for (int i = 0; i < M; i ++)
			for (int j = 0; j < N; j ++)
				w[i][j] = -1;
		for (int i = 0; i < M; i ++)
		{
			int C;
			cin >> C;
			while (C --)
			{
				int p, q;
				cin >> p >> q;
				p --;
				w[i][p] = q;
			}
		}
		int best = -1;
		int ans = N + 1;
		for (int i = 0; i < (1 << N); i ++)
		{
			bool f = true;
			for (int j = 0; j < M; j ++)
			{
				bool ff = false;
				for (int k = 0; k < N; k ++)
				{
					if (w[j][k] >= 0 && tst(i, k) == w[j][k]) ff = true;
				}
				if (!ff) f = false;
			}
			if (f && cnt(i) < ans) 
			{
				ans = cnt(i);
				best = i;
			}
		}
		cout << "Case #" << t << ":";
		if (best >= 0) 
		{
			for (int i = 0; i < N; i ++)
				cout << " " << tst(best, i);
		}
		else
			cout << " IMPOSSIBLE";
		cout << endl;
	}
}
