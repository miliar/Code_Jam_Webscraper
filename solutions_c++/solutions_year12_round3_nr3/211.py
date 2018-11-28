#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int n,m;

long long A[110], B[110], a[110], b[110];

long long ans[110][110];

void solve()
{
	int i,j;

	for (i = 1; i <= n; ++i)
		for (j = 1; j <= m; ++j)
		{
			ans[i][j] = max(ans[i - 1][j], ans[i][j - 1]);
			if (A[i] == B[j])
			{				
				ans[i][j] = max(ans[i][j], ans[i - 1][j - 1] + min(a[i], b[j]));
				long long mnacord = max(a[i], b[j]) - min(a[i], b[j]);
				
				int hamar;
				if (a[i] > b[j])
					hamar = 1;
				else
					hamar = 2;

				int u = i;
				int v = j;

				long long sum = min(a[i], b[j]);

				long long answer = 0;

				while (mnacord > 0 && u > 0 && v > 0)
				{
					if (hamar == 1)
						v--;
					else
						u--;

					if (A[u] == B[v])
					{
						if (hamar == 1)
							sum += min(mnacord, b[v]);
						else
							sum += min(a[u], mnacord);
						answer = max(answer, ans[u - 1][v - 1] + sum);

						if (hamar == 1)
						{
							if (mnacord < b[v])
								hamar = 2;
							mnacord = max(mnacord, b[v]) - min(mnacord, b[v]);							
						}
						else
						{
							if (mnacord < a[u])
								hamar = 1;
							mnacord = max(a[u], mnacord) - min(a[u], mnacord);							
						}
					}
				}

				ans[i][j] = max(ans[i][j], answer);
			}
		}
}

int main()
{
	int test, t, i, j;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		in >> n >> m;
		for (i = 0; i < 110; ++i)
			for (j = 0; j < 110; ++j)
				ans[i][j] = 0;

		for (i = 1; i <= n; ++i)
			in >> a[i] >> A[i];

		for (i = 1; i <= m; ++i)
			in >> b[i] >> B[i];

		solve();

		/*for (i = 0; i <= n; ++i)
		{
			for (j = 0; j <= m; ++j)
				cout << ans[i][j] << " ";
			cout << endl;
		}

		cout << endl;*/

		out << "Case #" << t << ": " << ans[n][m] << endl;
	}
	return 0;
}