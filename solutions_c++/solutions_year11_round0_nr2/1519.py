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
	int c, d, n;
	char cs[4], ds[3], ns[101];
	map <pair <char, char>, char> cm;
	map <pair <char, char>, bool> dm;
	vector <char> ans;
	scanf("%d", &c);
	while (c--)
	{
		scanf("%s", cs);
		cm[make_pair(cs[0], cs[1])] = cs[2];
		cm[make_pair(cs[1], cs[0])] = cs[2];
	}
	scanf("%d", &d);
	while (d--)
	{
		scanf("%s", ds);
		dm[make_pair(ds[0], ds[1])] = true;
		dm[make_pair(ds[1], ds[0])] = true;
	}
	scanf("%d", &n);
	scanf("%s", ns);
	for (int i = 0; i < n; ++i)
	{
		if (ans.size() == 0)
			ans.push_back(ns[i]);
		else if (cm.find(make_pair(ans.back(), ns[i])) != cm.end())
		{
			ns[i] = cm[make_pair(ans.back(), ns[i])];
			ans.pop_back();
			ans.push_back(ns[i]);
		}
		else
		{
			ans.push_back(ns[i]);
			for (int j = 0; j < (int)ans.size() - 1; ++j)
				if (dm.find(make_pair(ans[j], ns[i])) != dm.end())
					ans.clear();
		}
		//for (int k = 0; k < (int)ans.size(); ++k)
			//printf("%c", ans[k]);
		//printf("\n");
	}
	printf("[");
	for (int i = 0; i < (int)ans.size(); ++i)
	{
		if (i == 0)
			printf("%c", ans[i]);
		else
			printf(", %c", ans[i]);
	}
	printf("]\n");
}

int main()
{
	//small("B", 0);
	large("B");
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