#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define eps 1e-8
#define oo 1e9


using namespace std;

typedef struct{
	int x, y;
}aa;

int T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, an;
aa a[200], b[200];
char c[10];

int main(){
	scanf("%d", &T);
	for (int rr = 1; rr <= T; rr++){
		printf("Case #%d: ", rr);
		z = 0; x = 0; an = 0;
		scanf("%d", &m);
		for (int i=0; i<m; i++){
			scanf("%s%d", c, &q);
			if (c[0] == 'O')
				a[z].x = i, a[z].y = q, z++;
			else b[x].x = i, b[x].y = q, x++;
		}
		a[z].x = oo; b[x].x = oo;
		z = 1; x = 1; q = 0; w = 0;
		for (int i=0; i<m; i++){
			if (a[q].x < b[w].x){
				s = abs(a[q].y - z) + 1;
				an += s;
				z = a[q].y;
				if (abs(b[w].y - x) <= s)
					x = b[w].y;
				else x = b[w].y > x ? x + s : x - s;
				q++;
			} else {
				s = abs(b[w].y - x) + 1;
				an += s;
				x = b[w].y;
				if (abs(a[q].y - z) <= s)
					z = a[q].y;
				else z = a[q].y > z ? z + s : z - s;
				w++;
			}
		}
		printf("%d\n", an);
	}
	return 0;
}
