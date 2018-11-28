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

bool g[128][128];
bool G[128][128];

void print(bool a[][128], int n)
{
	cout << endl;
	for(i,1,n)
	{
		for(j,1,n)
			cout << a[i][j];
		cout << endl;
	}
	cout << endl <<endl;
}

void solve()
{
	fill(*g, *g+128*128, 0);
	fill(*G, *G+128*128, 0);
	
	int n;
	cin >> n;

	for (c,0,n)
	{
		int x1, x2, y1, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		for (i,x1,x2+1)
			for (j,y1, y2+1)
				g[j][i] = true;
	}

//	print(g, 7);

	int cost = 0;
	//cout << "! " << to[0][0] << endl;

	while (true)
	{
		cost++;

		bool ok = false;
		for(i,1,105)
			for(j,1,105)
			{
				//cout << i << " " << j << endl;
				if (cost%2 == 1)
				{	
					if (g[i][j] && (g[i-1][j] || g[i][j-1]) || !g[i][j] && g[i-1][j] && g[i][j-1])
					{
						G[i][j] = true;
						ok = true;
					}
					else G[i][j] = false;
				}
				else
				{
					if (G[i][j] && (G[i-1][j] || G[i][j-1]) || !G[i][j] && G[i-1][j] && G[i][j-1])
					{
						g[i][j] = true;
						ok = true;
					}
					else g[i][j] = false;
				}
			}
		
		/*
		cout << "g";
		print(g, 7);
		cout << "G";
		print(G, 7);
		*/

		if (!ok) break;
	}

	printf("%d\n", cost);
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for (cas, 1, cases+1)
	{
		printf("Case #%d: ", cas);
		solve();
	}
}