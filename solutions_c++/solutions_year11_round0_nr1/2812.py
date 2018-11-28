#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin );
	freopen("output.txt", "w", stdout );
	int cas;
	scanf("%d", &cas);
	for ( int cass=1; cass<=cas; ++cass)
	{
		int res = 0;
		int n;
		scanf("%d", &n);
		int px=1,py=1;
		int lx=0,ly=0;
		for ( int i=0; i<n; ++i)
		{
			char str[3];
			int p;
			scanf("%s %d", str, &p);
			if ( str[0]=='O' )
			{
				int step = abs( p-px) -lx;
				step = max(0, step );
				step ++;
				res += step;
				ly += step;
				lx=0;
				px=p;

			}
			else
			{
				int step = abs(p-py) -ly;
				step = max(0, step);
				step++;
				res += step;
				lx += step;
				ly=0;
				py=p;
			}

		}

		printf("Case #%d: %d\n", cass, res );
	}
	return 0;
}
