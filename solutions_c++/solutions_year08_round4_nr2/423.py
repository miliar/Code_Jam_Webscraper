#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

using namespace std;

void init () {
}

void solve (int _nn) {
	int m, n, a;
	scanf ("%d %d %d",&n,&m,&a);

	printf ("Case #%d: ",_nn);

	for (int x1 = 0; x1 <= n; x1++)
		for (int x2 = 0; x2 <= n; x2++)
			for (int y1 = 0; y1 <= m; y1++)
				for (int y2 = 0; y2 <= m; y2++)
				{
					int area = abs(x1*y2 - x2*y1);
					if (area == a) {
						printf ("%d %d %d %d %d %d\n",0,0,x1,y1,x2,y2);
						return;
					}
				}
	printf ("IMPOSSIBLE\n");
}

int main () {
	int cases;

	scanf ("%d",&cases);
	for (int i = 1; i <= cases; i++)
		solve (i);
}
