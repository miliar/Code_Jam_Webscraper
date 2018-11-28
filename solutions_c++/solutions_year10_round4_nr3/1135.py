#include <cstdio>

bool map[100][100];
bool next[100][100];

int test() {
	for (int i=0;i<100;i++) for (int j=0;j<100;j++) map[i][j]=next[i][j]=0;
	int r;
	scanf("%d", &r);
	for (int i=0;i<r;i++) {
		int a,b,c,d;
		scanf("%d%d%d%d", &a, &b, &c, &d);
		for (int j=a-1;j<c;j++) for (int k=b-1;k<d;k++) map[j][k] = 1;
	}
	int found = 1;
	int steps = 0;
	if (r==0) return 0;
	while (found) {
		steps++;
		for (int i=0;i<100;i++) {
			for (int j=0;j<100;j++) {
				int n = 0;
				if (j>0 && map[i][j-1]) n++;
				if (i>0 && map[i-1][j]) n++;
				if (n==2) {
					//printf("Nowa komorka %d %d\n", i,j);
					next[i][j]=1;
				}
				else if (n==0) next[i][j]=0;
				else next[i][j] = map[i][j];
			}
		}
		found = 0;
		for (int i=0;i<100;i++) for (int j=0;j<100;j++) {
			map[i][j]=next[i][j];
			if (map[i][j]) found++;
			next[i][j] = 0;
		}
		//printf("At step %d found %d\n", steps, found);
	}
	return steps;
}

main() {
	int z;
	scanf("%d", &z);
	for (int i=0;i<z;i++) printf("Case #%d: %d\n", i+1, test());
}

