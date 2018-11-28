#include <iostream>
#include <fstream>
using namespace std;
#define INF (long long)1000000000


int R, k, N;
long long g[1001];
long long sum[2001];

int bs(int b, int e)
{
	long long off = sum[b];
	while (b + 1 < e)
	{
		if (sum[(b + e) / 2] - off > k)
			e = (b + e) / 2;
		else
			b = (b + e) / 2;
	}
	return b;
}

int main()
{
	ifstream fin("in");
	ofstream fout("out");
	int T;
	fin >> T;
	for (int C = 1; C <= T; C++)
	{
		fin >> R >> k >> N;
		memset(g, 0, sizeof(g));
		sum[0] = 0;
		for (int i = 0; i < N; i++)
		{
			fin >> g[i];
			g[N + i] = g[i];
			sum[i + 1] = sum[i] + g[i];
		}
		for (int i = N; i < 2 * N; i++)
			sum[i + 1] = sum[i] + g[i];
		g[2 * N] = INF;
		sum[2 * N + 1] = INF;
		long long ans = 0, cur = 0;
		for (int i = 0; i < R; i++)
		{
			int t = bs(cur, 2 * N + 1);
			if (t - cur > N)
				t = cur + N;
			ans += sum[t] - sum[cur];
            cur = t % N;
		}
		cout << "Case #" << C << ": " << ans << endl;
		fout << "Case #" << C << ": " << ans << endl;
	}
	return 0;
}