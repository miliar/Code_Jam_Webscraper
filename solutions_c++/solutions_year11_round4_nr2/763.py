#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 

using namespace std; 
 
const double pi = acos (-1.0); 
const double eps = 1.0e-10;

void small(char *problem, int try_time)
{
	char inFile[1024], outFile[1024];
	sprintf(inFile, "C:\\Users\\Lee\\Desktop\\%s-small-attempt%d.in", problem, try_time);
	sprintf(outFile, "C:\\Users\\Lee\\Desktop\\%s-small-attempt%d.out", problem, try_time);
	freopen (inFile, "r", stdin);
	freopen (outFile, "w", stdout);
}

void large(char *problem)
{
	char inFile[1024], outFile[1024];
	sprintf(inFile, "C:\\Users\\Lee\\Desktop\\%s-large.in", problem);
	sprintf(outFile, "C:\\Users\\Lee\\Desktop\\%s-large.out", problem);
	freopen (inFile, "r", stdin);
	freopen (outFile, "w", stdout);
}

void solve()
{
	int R, C, D, K;
	char g[510][510];
	scanf("%d%d%d", &R, &C, &D);
	for (int i = 0; i < R; ++i)
		scanf("%s", g[i]);
	K = min (R, C);
	while (K >= 3)
	{
		for (int i = 0; i + K <= R; ++i)
		{
			for (int j = 0; j + K <= C; ++j)
			{
				double ci = 0, cj = 0;
				for (int ii = 0; ii < K; ++ii)
					for (int jj = 0; jj < K; ++jj)
					{
						if (!(ii == 0 && jj == 0)
							&& !(ii == 0 && jj == K - 1)
							&& !(ii == K - 1 && jj == 0)
							&& !(ii == K - 1 && jj == K - 1))
						{
							ci += (ii - (K - 1) / 2.0) * (g[i + ii][j + jj] - '0');
							cj += (jj - (K - 1) / 2.0) * (g[i + ii][j + jj] - '0');
						}
					}
				if (ci == 0 && cj == 0)
				{
					printf("%d\n", K);
					goto lee;
				}
			}
		}
		--K;
	}
	printf("IMPOSSIBLE\n");
lee:
	;
}

int main()
{
	small("B", 0);
	//large("A");
	//freopen ("C:\\Users\\Lee\\Desktop\\A-large-practice.in", "r", stdin);
	//freopen ("C:\\Users\\Lee\\Desktop\\A-large-practice.out", "w", stdout);
	int ncase = 0;
	scanf("%d", &ncase);
	for (int icase = 1; icase <= ncase; ++icase)
	{
		printf("Case #%d: ", icase);
		solve();
	}
}