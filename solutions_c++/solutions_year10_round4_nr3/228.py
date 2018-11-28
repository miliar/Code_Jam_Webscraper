#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

// {{{ gprintf for debugging
bool gprintf(int debug,const char *format,...) {
	if(DBG & debug) {
		va_list	listpointer;

		va_start(listpointer, format);
		vfprintf(stderr,format,listpointer);
		va_end(listpointer);

		return true;
	}
	else
		return false;
}
// }}}

bool	g[100][100];
int	min_x,max_x,min_y,max_y;

bool simulate() {
	int	i,j;
	bool	p,q,f = false;
	int	c = 0;
	/*for(i = min_y; i <= max_y; i++) {
		for(j = min_x; j <= max_x; j++) {
			printf("%c ",g[i][j] ? 'Y' : 'N');
		}

		printf("\n");
	}*/

	for(i = max_y; i >= min_y; i--) {
		for(j = max_x; j >= min_x; j--) {
			p = (i > 0 && g[i-1][j]);
			q = (j > 0 && g[i][j-1]);

			g[i][j] = (g[i][j] ? (p || q) : (p && q));

			/*if(i == min_y && j == min_x) {
				cout << p << " " << q << " " << g[i][j] << endl;
				cout << i << " " << (j-1) << " " << g[i][j-1] << endl;
//				exit(EXIT_FAILURE);
			}*/

			if(g[i][j]) { f = true; c++; }
		}
	}

	/*for(i = min_y; i <= max_y; i++) {
		for(j = min_x; j <= max_x; j++) {
			printf("%c ",g[i][j] ? 'Y' : 'N');
		}

		printf("\n");
	}*/

	//printf("c = %d\n",c);

	return f;
}

int main()
{
	int	C,cs;
	int	R;
	int	x1,y1,x2,y2,x,y;
	int	T;

	scanf("%d",&C);

	rab(cs,1,C) {
		scanf("%d",&R);

		min_x = max_x = min_y = max_y = -1;

		memset(g,0,sizeof(g));

		while(R--) {
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);

			x1--;x2--;y1--;y2--;

			if(min_x == -1 || x1 < min_x) min_x = x1;
			if(max_x == -1 || x2 > max_x) max_x = x2;
			if(min_y == -1 || y1 < min_y) min_y = y1;
			if(max_y == -1 || y2 > max_y) max_y = y2;

			rab(x,x1,x2) rab(y,y1,y2) g[y][x] = true;
		}

		for(T = 1; ;T++) {
			if(!simulate()) break;
		}

		printf("Case #%d: %d\n",cs,T);
	}

	return 0;
}
