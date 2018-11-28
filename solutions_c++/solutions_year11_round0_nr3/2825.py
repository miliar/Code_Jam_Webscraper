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
	freopen("C-small-attempt2.in", "r", stdin );
//	freopen("B-large.in", "r", stdin );
	freopen("output.txt", "w", stdout );
	int cas;
	scanf("%d", &cas);
	for ( int cass=1; cass<=cas; ++cass)
	{
		int n;
		scanf("%d", &n);
		int a[1009];
		for (int i=0; i<n; ++i) scanf("%d", &a[i]);
		int res = -1;
		for (int i=1; i<(1<<n)-1; ++i)
		{
			int x=0,y=0,tx=0,ty=0;
			for (int j=0; j<n; ++j)
			{
				if ( i&(1<<j) )
				{
					x ^= a[j];
					tx += a[j];
				}
				else 
				{
					y ^= a[j];
					ty += a[j];
				}
			}
			if ( x == y ) res = max(res, max( tx, ty ));
		}
		printf("Case #%d: ", cass );
		if ( res== -1) puts("NO");
		else printf("%d\n", res );

	}
	return 0;
}
