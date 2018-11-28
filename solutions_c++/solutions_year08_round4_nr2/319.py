#include <stdio.h>
#include <math.h>

int n, m;
int area;

int main () {
	int c, t;
	int pom,x1,y1,x2,y2,x3,y3;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for (scanf("%d", &t), c=1; c<=t; c++) {		
		scanf("%d%d", &n, &m);
		scanf("%d", &area);
		printf("Case #%d: ", c);

		x1=y1=0;
		//for (x1=0; x1<=n; x1++)
			//for (y1=0; y1<=m; y1++)
				for (x2=0; x2<=n; x2++)
					for (y2=0; y2<=m; y2++)
						for (x3=0; x3<=n; x3++)
							for (y3=0; y3<=m; y3++) {
								pom=abs((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1));
								if (area==pom)
									goto skip;
							}

		printf("IMPOSSIBLE\n");
		continue;
skip:
		printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
	}
	return 0;
}