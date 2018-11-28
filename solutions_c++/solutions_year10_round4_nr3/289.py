#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int table[202][202];
int newtable[202][202];

int main(int argc, char* argv[])
{
//#ifdef _DEBUG
	freopen("Test.in", "r", stdin);
//#endif

	int T;
	scanf("%d", &T);


	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int R;
		scanf("%d", &R);

		int minX = INT_MAX;
		int maxX = -INT_MAX;

		int minY = INT_MAX;
		int maxY = -INT_MAX;

		memset(table, 0, sizeof(table));

		while (R--)
		{
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

			for (int x = x1; x <= x2; x++)
			{
				for (int y = y1; y <= y2; y++)
				{
					table[y][x] = 1;

					minX = min(minX, x);
					minY = min(minY, y);

					maxX = max(maxX, x);
					maxY = max(maxY, y);
				}
			}		
		}

		int res = 0;
		while (true)
		{
			if (minX == INT_MAX)
				break;

			res++;
			memset(newtable, 0, sizeof(newtable));

			int nminX = INT_MAX;
			int nmaxX = -INT_MAX;

			int nminY = INT_MAX;
			int nmaxY = -INT_MAX;

			for (int y = minY; y <= maxY; y++)
			{
				for (int x = minX; x <= maxX; x++)
				{
					newtable[y][x] = table[y][x];
					
					if (!table[y - 1][x] && !table[y][x - 1])
					{
						newtable[y][x] = 0;
					}
					else if (table[y - 1][x] && table[y][x - 1])
						newtable[y][x] = 1;

					if (newtable[y][x] == 1)
					{
						nminX = min(nminX, x);
						nminY = min(nminY, y);

						nmaxX = max(nmaxX, x);
						nmaxY = max(nmaxY, y);
					}
				}
			}

			memcpy(table, newtable, sizeof(table));
			minX = nminX;
			maxX = nmaxX;
			minY = nminY;
			maxY = nmaxY;			

		}
		

		printf("Case #%d: %d\n", nTest, res);
		fflush(stdout);
	} 


	return 0;
}


