#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef long long       Long;

#define toStr(a)      (((stringstream&)((stringstream()<<(a)))).str())
#define for(i, a, b)    for (int i = (a); i < (b); i++)
#define all(a)        ((a).begin(), (a).end())
#define pb(a)         push_back(a)
#define _x            first
#define _y            second

int c[10][1024];
int m[1024];
int p2[11];

void setup()
{
	p2[0] = 1;
	for(i,1,11)
		p2[i] = 1<<i;
}

//topic: trade between china and america, how has it changed over the years...

int recurse(int a, int b)
{
	if (a>=b) return 0;
	//cout << "starting " << a << " " << b << " -> len = " << (b-a+1) << endl;
	
	bool ok = false;
	for (i, a, b+1)
		ok |= m[i] > 0;

	if (!ok) return 0;
	
	for(i,a,b+1)
		m[i]--;
	
	//cout << "found\n";
	return 1 + ((a+1!=b) ? recurse(a, a+(b-a+1)/2-1)+recurse(a+(b-a+1)/2, b) : 0);
}

void solve()
{
	int p;
	scanf("%d", &p);

	for(i,0,p2[p])
	{
		scanf("%d", m+i);
		m[i] = p-m[i]; //turn into need
	}

	
	int n = p2[p];
	for (i,0,p)
		for (j,0,p2[i])
			scanf("%d", &c[i][j]);
	
	int ans = recurse(0, p2[p]-1);

	printf("%d\n", ans);
}

//how did the census affect the economy. (increased jobs )
//superbowl, use the force
//etc

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);
	//cout << cases << endl;

	for (cas, 1, cases+1)
	{
		printf("Case #%d: ", cas);
		setup();
		solve();
	}
}