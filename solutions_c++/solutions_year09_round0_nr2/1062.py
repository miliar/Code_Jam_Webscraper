#include<stdio.h>
#include<queue>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define ii pair<int, int>
#define lg 105

int nrs, n, m, i, j, s, k, xx, yy, x, y, am, aa, bb, tx, ty, a[lg][lg], scriu[lg][lg], test, pun;
bool fst[lg][lg];
ii mark[lg][lg];

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	scanf("%d", &nrs);
	for (test = 1; test <= nrs; test ++){
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i ++)
			for (j = 1; j <= m; j ++)
				scanf("%d", &a[i][j]);

		queue<ii> q; memset(fst, 0, sizeof(fst)); memset(scriu, 0, sizeof(scriu));

		for (i = 1; i <= n; i ++)
			for (j = 1; j <= m; j ++){
				s = 0;

				for (k = 0; k < 4; k ++){
					xx = i + dx[k], yy = j + dy[k];

					if (xx > 0 && xx <= n && yy > 0 && yy <= m)
						if (a[xx][yy] < a[i][j])
							s = 1;
				}

				if (!s){
					//printf("bag %d %d\n", i, j);
					q.push(mp(i, j)); fst[i][j] = 1;
					mark[i][j] = mp(i, j);
				}
			}

		while (!q.empty()){
			x = (q.front()).x, y = (q.front()).y; q.pop();

			for (i = 0; i < 4; i ++){
				xx = x + dx[i], yy = y + dy[i];

				if (xx > 0 && xx <= n && yy > 0 && yy <= m && !fst[xx][yy]){
					am = 0x3f3f3f3f;
					for (j = 0; j < 4; j ++){
						aa = xx + dx[j], bb = yy + dy[j];

						if (a[aa][bb] < am && aa > 0 && aa <= n && bb > 0 && bb <= m){
							am = a[aa][bb];
							tx = aa, ty = bb;
						}
					}

					//printf("pentru %d %d  %d %d\n", xx, yy, tx, ty);

					if (tx == x && ty == y){
						fst[xx][yy] = 1; mark[xx][yy] = mark[x][y];
						q.push(mp(xx, yy));
					}
				}
			}
		}

		printf("Case #%d:\n", test);

		pun = 'a';
		for (i = 1; i <= n; i ++){
			for (j = 1; j <= m; j ++){
				x = scriu[ mark[i][j].x ][ mark[i][j].y ];
				if (!x){
					scriu[ mark[i][j].x ][ mark[i][j].y ] = pun;
					printf("%c ", pun);
					pun ++;
				}
				else
					printf("%c ", x);

				//printf("%d %d   ", mark[i][j].x, mark[i][j].y);
			}
			printf("\n");
		}
	}

	return 0;
}

