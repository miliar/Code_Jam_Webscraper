#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#define MAX 2<<10
using namespace std;

typedef struct{
	int x, y;
}pnt;
struct cmp {
	inline bool operator()(const pnt& a, const pnt& b) {
		return a.x < b.x;
	}
};
static pnt p[MAX];

int main () {
	int k, i, n, j,m, t, h, cs = 0; 
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		for (j = 0; j < n; j++)
			scanf("%d %d", &p[j].x, &p[j].y);
		sort(p, p+n, cmp());
		int it = 0;
//		for (k = 0; k < n; k++)
//			printf("%d %d\n", p[k].x, p[k].y);
		for(j = 0; j < n; j++) {
			h = p[j].y;
		//	printf("h = %d....", h);
			for (m = j+1; m < n; m++) {
				if (p[m].y < h) it++;
		//		printf(" %d ", p[m].y);
			}
		}
		printf("Case #%d: %d\n", ++cs, it);
	}
	return 0;
}
