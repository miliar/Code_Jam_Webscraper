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
	int n, p, c = 0, o1 = 1, o2 = 1, b1 = 1, b2 = 1;
	char r[2];
	scanf("%d", &n);
	while (n--)
	{
		scanf("%s%d", r, &p);
		if (r[0] == 'O')
		{
			if (p < o1 || p > o2)
			{
				c += min (abs(p - o1), abs(p - o2));
				b1 -= min (abs(p - o1), abs(p - o2));
				b2 += min (abs(p - o1), abs(p - o2));
			}
			o1 = o2 = p;
			++c;
			--b1;
			++b2;
			if (b1 < 1) b1 = 1;
			if (b2 > 100) b2 = 100;
		}
		else
		{
			if (p < b1 || p > b2)
			{
				c += min (abs(p - b1), abs(p - b2));
				o1 -= min (abs(p - b1), abs(p - b2));
				o2 += min (abs(p - b1), abs(p - b2));
			}
			b1 = b2 = p;
			++c;
			--o1;
			++o2;
			if (o1 < 1) o1 = 1;
			if (o2 > 100) o2 = 100;
		}
		//printf("c %d o1 %d o2 %d b1 %d b2 %d\n", c, o1, o2, b1, b2);
	}
	printf("%d\n", c);
}

int main()
{
	//small("A", 0);
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