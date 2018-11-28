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
	int n, c, minc = 1000001, sum = 0, wrongsum = 0;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &c);
		if (minc > c)
			minc = c;
		sum += c;
		wrongsum ^= c;
	}
	if (wrongsum == 0)
		printf("%d\n", sum - minc);
	else
		printf("NO\n");
}

int main()
{
	//small("C", 0);
	large("C");
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