#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<sstream>
#include<cctype>

using namespace std;

#define pb push_back
#define pf printf
#define sf scanf
#define re return

#define DBG 0

char grid[105][105];
char C[105][105];
bool all0() {
	int i, j;
	for(i=1;i<=100;i++)
	 for(j=1;j<=100;j++)
	   if( grid[i][j] == '1' ) re false;
	re true;
}

int main() {
	int t, cases = 1;
	for( sf("%d", &t); t--; ) {
		int R;
		cin >> R;
		int i, a, b, j;
		for(a=0;a<=100;a++)
		 for(b=0;b<=100;b++)
		  grid[a][b] = '0';

		for(i=0;i<R;i++) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(a=y1;a<=y2;a++)
			 for(b=x1;b<=x2;b++)
			   grid[a][b] = '1';
		}

		int res = 0;

		while(1) {
			if( all0() ) break;

			for(i=1;i<=100;i++)
			 for(j=1;j<=100;j++) {
                if( grid[i][j] == '1' ) {
				  if( grid[i-1][j] == '0' && grid[i][j-1] == '0')
				    C[i][j] = '0';
				  else C[i][j] = '1';
				}
				else {
				  if( grid[i-1][j] == '1' && grid[i][j-1] == '1')
				    C[i][j] = '1';
				  else C[i][j] = '0';
				}
			 }

			res++;
			for(i=1;i<=100;i++)
			 for(j=1;j<=100;j++)
			   grid[i][j] = C[i][j];
		}
		pf("Case #%d: %d\n", cases++, res);

	}
	return 0;
}
