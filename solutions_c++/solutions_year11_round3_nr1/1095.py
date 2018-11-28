#include <stdio.h>
#define N 100
char map[220][220];
int main()
{	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", map[i]);
		for (int i = 0; i < n -1; ++i) {
			for (int j = 0; j < m -1; ++j)
				if (map[i][j] == '#' && map[i +1][j] == '#' && map[i][j +1] == '#' && map[i +1][j +1] == '#') {
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';	
				}
		}
		
		int pass = 1;
		for (int i = 0; i < n && pass; ++i)
			for (int j = 0; j < m && pass; ++j)
				if (map[i][j] == '#')
					pass = 0;
					
		printf("Case #%d:\n", t);
		if (!pass)	puts("Impossible");
		else {
			for (int i = 0; i < n; ++i,puts(""))
				for(int j=0;j<m;++j)
					printf("%c",map[i][j]);
		}
	}
	//scanf(" ");
	return 0;
}
