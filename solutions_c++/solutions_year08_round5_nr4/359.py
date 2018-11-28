#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;

typedef long long 	i64;
typedef pair <int, int> pii;
typedef vector <int>		vi;

typedef vector <string>		vs;
int 	dx[] = {2, 1};
int 	dy[] = {1, 2};
int 	mod = 10007;

int 	cas, T;


int 	h, w, r;
int 	mp[110][110];	//, cant[110][110];
int 	x, y;



void	prt_case()
{		
	printf("Case #%d: %d\n", ++T, mp[h-1][w-1]);		
}

int main()
{
	int 	i, j, k;
	
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D_s.out", "w", stdout);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		memset(mp, 0, sizeof(mp));
		
		scanf("%d %d %d", &h, &w, &r);
		for (i=0; i<r; i++)
		{
			scanf("%d %d", &x, &y);
			mp[x-1][y-1] = -1;
		}
		
		
		mp[0][0] = 1;
		for (i=0; i<h; i++)
			for (j=0; j<w; j++)
			{
				if (mp[i][j] == -1)	continue;
				
				for (k=0; k<2; k++)
				{
					int	nx, ny;
					nx = i + dx[k];
					ny = j + dy[k];
					
					if (mp[nx][ny] == -1)	continue;
					
					mp[nx][ny] = (mp[nx][ny] + mp[i][j]) % mod;
				}
			}
		
		
		prt_case();
		
	}
	return 0;
}
