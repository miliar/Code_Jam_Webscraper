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
	int X, S, R, tt, N;
	int w[1010][3], c = 0;
	double t, ans = 0;
	priority_queue <pair <int, int> > Q;
	scanf("%d%d%d%d%d", &X, &S, &R, &tt, &N);
	t = tt;
	for (int i = 0; i < N; ++i)
	{
		scanf("%d%d%d", &w[i][0], &w[i][1], &w[i][2]);
		c += w[i][1] - w[i][0];
		Q.push(make_pair(-w[i][2], w[i][1] - w[i][0]));
	}
	c = X - c;
	if (R * t <= c)
	{
		ans = t + (c - R * t) / S;
		for (int i = 0; i < N; ++i)
			ans += 1.0 * (w[i][1] - w[i][0]) / (w[i][2] + S);
	}
	else
	{
		ans = 1.0 * c / R;
		t -= 1.0 * c / R;
		while (!Q.empty())
		{
			pair <int, int> P = Q.top();
			if ((R + (-P.first)) * t >= P.second)
			{
				ans += 1.0 * P.second / (R + (-P.first));
				t -= 1.0 * P.second / (R + (-P.first));
				Q.pop();
			}
			else
			{
				ans += t + (1.0 * P.second - t * (R + (-P.first))) / (S + (-P.first));
				Q.pop();
				break;
			}
		}
		while (!Q.empty())
		{
			pair <int, int> P = Q.top();
			ans += 1.0 * P.second / (S + (-P.first));
			Q.pop();
		}
	}
	printf("%.9f\n", ans);
}

int main()
{
	//small("A", 1);
	large("A");
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