#include <iostream>
#include <fstream>
#include <cstdlib>
#include <memory>

using namespace std;

ifstream fin("c-large.in");
ofstream fout("c.out");

int g[2000];
long long c[2000];
int next[2000];
int used[2000];

int main()
{
	int T;
	int R, k, N;
	int cases = 0;
	long long ans;
	fin >> T;
	while (T--)
	{
		fin >> R >> k >> N;
		memset(g, 0, sizeof g);
		memset(c, 0, sizeof c);
		for (int i=0; i<N; i++) fin >> g[i];

		long long tot = 0;
		for( int i=0; i<N;i ++) tot+=g[i];
		if (tot <= k)
		{
			ans = tot * R;
		}
		else
		{
			memset(next, 0, sizeof next);
			memset(used, 0, sizeof used);
			for (int i=0; i<N; i++)
			{
				int p = i;
				tot = 0;
				while (tot <= k)
				{
					tot += g[p];
					p=(p+1)%N;
				}
				p--;
				if (p< 0) p=N-1;
				tot -= g[p];
				next[i] = p;
				c[i] = tot;
			}
			used[0] = 1;
			int idx = 2;
			int p = next[0];
			while (!used[p])
			{
				used[p] = idx++;
				p = next[p];
			}

			int rounds = idx - used[p];
			int st = used[p]-1;
			int q= p;

			if (R <= st)
			{
				p = 0;
				ans = 0;
				for (int i=0; i<R; i++)
				{
					ans += c[p];
					p = next[p];
				}
			}
			else
			{
				p = 0;
				ans = 0;
				for (int i=0; i<st; i++)
				{
					ans += c[p];
					p = next[p];
				}
				int rr = (R-st)/rounds;
				p = q;
				tot = 0;
				for (int i=0; i<rounds; i++)
				{
					tot += c[p];
					p = next[p];
				}
				ans += rr * tot;
				p = q;
				for (int i=0; i<((R-st)%rounds); i++)
				{
					ans += c[p];
					p = next[p];
				}
			}
		}

		fout << "Case #" << ++cases << ": "	<< ans << endl;
	}
	return 0;
}