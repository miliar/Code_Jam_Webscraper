#include <cstdio>

int main(){
	freopen("triangle.in", "rt", stdin);
	freopen("triangle.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int n, m, a;
		scanf("%d%d%d", &n, &m, &a);
		printf("Case #%d: ", t);
		bool T = false;
		if (a>n*m){
			printf("IMPOSSIBLE\n");
			continue;
		}
		for (int x1 = 0; x1 <= 0; x1++) if (!T)
			for (int y1 = 0; y1 <= m; y1++) if (!T)
				for (int x2 = 0; x2 <= n; x2++) if (!T)
					for (int y2 = 0; y2 <= m; y2++) if (!T)
						for (int x3 = 0; x3 <= n; x3++) if (!T)
							for (int y3 = 0; y3 <= m; y3++) if (!T){
								int dx1 = x2 - x1;
								int dy1 = y2 - y1;
								int dx2 = x3 - x1;
								int dy2 = y3 - y1;
								int tmp = dx1*dy2-dy1*dx2;
								if (tmp<0) tmp = -tmp;
								if (tmp==a){
									printf("%d %d %d %d %d %d\n", x1,y1,x2,y2,x3,y3);
									T = true;
								}
							}
		if (!T) printf("IMPOSSIBLE\n");
	}
}
