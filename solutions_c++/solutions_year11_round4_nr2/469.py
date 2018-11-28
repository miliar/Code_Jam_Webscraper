#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

char s[510][510];

int sX[510][510], sY[510][510], m[510][510];

bool ok(int i, int j, int k)
{
	int ki = i+k-1, kj = j+k-1;
	int mass = m[ki][kj] + m[i-1][j-1] - m[ki][j-1] - m[i-1][kj] - (s[ki-1][kj-1]-'0' + s[ki-1][j-1]-'0' + s[i-1][kj-1]-'0' + s[i-1][j-1]-'0');
	int sx = sX[ki][kj] + sX[i-1][j-1] - sX[ki][j-1] - sX[i-1][kj] - ((s[ki-1][kj-1]-'0')*(ki) + (s[ki-1][j-1]-'0')*(ki) + (s[i-1][kj-1]-'0')*(i) + (s[i-1][j-1]-'0')*(i));
	int sy = sY[ki][kj] + sY[i-1][j-1] - sY[ki][j-1] - sY[i-1][kj] - ((s[ki-1][kj-1]-'0')*(kj) + (s[ki-1][j-1]-'0')*(j) + (s[i-1][kj-1]-'0')*(kj) + (s[i-1][j-1]-'0')*(j));
	
	double srx = i+(double)(k-1)/2;
	double sry = j+(double)(k-1)/2;
	
	srx *= mass;
	sry *= mass;
	
	return max(fabs(srx-sx), fabs(sry-sy)) < 1e-4;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int icase=1; icase<=cases; ++icase)
	{
		int res = 0;
		
		int x, y, d;
		scanf("%d%d%d", &x, &y, &d);
		assert(min(x,y) <= 500);
		for(int i=0; i<x; ++i) scanf("%s", s[i]);
		
		for(int i=0; i<=max(x,y); ++i)
		{
			m[0][i] = m[i][0] = 0;
			sX[i][0] = sX[0][i] = 0;
			sY[i][0] = sY[0][i] = 0;
		}
		
		for(int i=1; i<=x; ++i)
		{
			for(int j=1; j<=y; ++j)
			{
				m[i][j] = m[i-1][j] + m[i][j-1] - m[i-1][j-1] + s[i-1][j-1]-'0';
				sX[i][j] = sX[i-1][j] + sX[i][j-1] - sX[i-1][j-1] + (s[i-1][j-1]-'0')*i;
				sY[i][j] = sY[i-1][j] + sY[i][j-1] - sY[i-1][j-1] + (s[i-1][j-1]-'0')*j;
			}
		}
		
		bool found = false;
		for(res=min(x,y); res>=3 && !found; )
		{
			for(int i=1; i+res-1<=x && !found; ++i)
			{
				for(int j=1; j+res-1<=y && !found; ++j)
				{
					if(ok(i,j,res)){ found = true; }
				}
			}
			
			if(!found) res--;
		}
		
		if(found)
			printf("Case #%d: %d\n", icase, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", icase);
	}
	return 0;
}
