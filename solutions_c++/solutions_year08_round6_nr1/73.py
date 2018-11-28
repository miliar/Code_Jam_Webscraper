#include <cstdio>

int max(int a, int b){return a>b?a:b;}
int min(int a, int b){return a>b?b:a;}

int main(){
	int z;
	scanf("%d", &z);

	for (int cases = 0; cases < z; cases++){
		printf ("Case #%d:\n", cases+1);

		int n;
		int range[1024][2];
		bool isb[1024];
		scanf("%d", &n);

		for (int tmp = 0; tmp < n; tmp++){
			char buf[16];
			scanf("%d%d%s", &range[tmp][0], &range[tmp][1], buf);
			isb[tmp] = (buf[0] == 'B');
			fgets(buf, 16, stdin);
		}
		int i;
		for (i = 0; i < n; i++)
			if (isb[i])
				break;
		if (i == n){
			int m;
			scanf("%d", &m);
			while (m--){
				int x, y;
				scanf("%d%d", &x, &y);
				int j;
				for (j = 0; j < n; j++)
					if (x == range[j][0] && y == range[j][1]){
						printf ("NOT BIRD\n");
						break;
					}
				if (j == n)
					printf ("UNKNOWN\n");
			}
			continue;
		}

		int bxmax = range[i][0];
		int bxmin = range[i][0];
		int bymax = range[i][1];
		int bymin = range[i][1];

		for (; i<n; i++)
			if (isb[i]){
				bxmax = max(bxmax, range[i][0]);
				bxmin = min(bxmin, range[i][0]);
				bymax = max(bymax, range[i][1]);
				bymin = min(bymin, range[i][1]);
			}

		int m;
		scanf("%d", &m);
		while(m--){
			int x, y;
			scanf("%d%d",&x,&y);
			if (x >= bxmin && x <= bxmax && y >= bymin && y <= bymax)
				printf ("BIRD\n");
			else { 
				int xmax, xmin, ymax, ymin;
				xmax = max(x, bxmax);
				xmin = min(x, bxmin);
				ymax = max(y, bymax);
				ymin = min(y, bymin);
				bool fail = false;
				for (i = 0; i < n; i++){
					if (isb[i])
						continue;
					if (range[i][0] >= xmin && range[i][0] <= xmax && range[i][1] >= ymin && range[i][1] <= ymax)
						fail = true;
				}
				if (fail)
					printf ("NOT BIRD\n");
				else
					printf ("UNKNOWN\n");
			}
		}
	}
	return 0;
}
