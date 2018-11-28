#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;

bool map[105][105];
int s[105][105];
int ymax, xmax;

const int INF = 100000000;
const int modnum = 10007;

int solve()
{
	int i, j, k;

	for (i = 0; i < ymax; i ++) {
		for (j = 0; j < xmax; j ++) {
			s[i][j] = 0;
		}
	}

	s[0][0] = 1;
	for (i = 0; i < ymax; i ++) {
		for (j = 0; j < xmax; j ++) {
			if (i + 2 < ymax && j + 1 < xmax && map[i+2][j+1] == false) {
				s[i+2][j+1] += s[i][j];
				s[i+2][j+1] %= modnum;

			}
			if (i + 1 < ymax && j + 2 < xmax && map[i+1][j+2] == false) {
				s[i+1][j+2] += s[i][j];
				s[i+1][j+2] %= modnum;
			}
		}
	}

	return s[ymax-1][xmax-1];
}


int main()
{
	int i, j, k;
	int t;
	int nowt;
	int temp;
	int a, b, nr;

	freopen("D-small-attempt0.in.txt", "r", stdin);
//	freopen("D-small-attempt0.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;

		scanf("%d%d%d", &ymax, &xmax, &nr);
		
		for (i = 0; i < ymax; i ++) {
			for (j = 0; j < xmax; j ++) {
				map[i][j] = false;
			}
		}

		for (i = 0; i < nr; i ++) {
			scanf("%d%d", &a, &b);
			a --; b--;

			map[a][b] = true;
		}

		printf("Case #%d: %d\n", nowt, solve());
	}

	return 0;
}



