#include <iostream>

using namespace std;

const int dx[4] = {1, 1, 0, -1};
const int dy[4] = {0, 1, 1, 1};

bool status[100];
char mat[60][60];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	char dum[5];
	int i, j, k, l, n, b, tc, nc, by, cnt;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		memset(mat, 0, sizeof(mat));
		status['R'] = status['B'] = false;
		scanf("%d%d", &n, &b);
		gets(dum);
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				scanf("%c", &mat[j][n-i-1]);
			}	
			gets(dum);
		}
		for (i = 0; i < n; i++) {
			cnt = n-1;
			for (j = n-1; j >= 0; j--) {
				if (mat[j][i] != '.')
					mat[cnt--][i] = mat[j][i];
			}
			for (j = cnt; j >= 0; j--)
				mat[j][i] = '.';
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (mat[i][j] == '.')
					continue;
				for (l = 0; l < 4; l++) {
					by = 1;
					for (k = 1; k < b; k++) {
						if (mat[i+dy[l]*k][j+dx[l]*k] == mat[i][j])
							by++;
						else
							break;
					}
					if (by >= b)
						status[mat[i][j]] = true;
				}
			}
		}
		printf("Case #%d: ", nc);
		if ((status['R'] && status['B']))
			printf("Both\n");
		else if (status['R'])
			printf("Red\n");
		else if (status['B'])
			printf("Blue\n");
		else
			printf("Neither\n");
	}	
}
