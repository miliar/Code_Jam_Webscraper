#include <iostream>

using namespace std;

char temp[5];
int mat[515][515];
char token[200];
int byk[515][515];
bool pake[515][515];
int all[515];

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int tc, nc, brs, klm, i, j, k, cnt, bil;
	int petak, max1, pmax, y, x;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		memset(all, 0, sizeof(all));
		memset(byk, 0, sizeof(byk));
		scanf("%d%d", &brs, &klm);
		for (i = 1; i <= brs; i++) {
			scanf("%s", token);
			temp[1] = '\0';
			cnt = 1;
			for (j = 0; j < klm/4; j++) {
				temp[0] = token[j];
				sscanf(temp, "%X", &bil);
//				cout << "aaaa " << bil << endl;
				for (k = 3; k >= 0; k--) {
					mat[i][cnt+k] = bil%2;
					bil /= 2;
				}
				cnt += 4;
			}
		}
		/*
		for (i = 1; i <= brs; i++) {
			for (j = 1; j <= klm; j++)
				cout << mat[i][j] << ' ';
			cout << endl;
		}
		system("pause");
		*/
		petak = brs*klm;
		pmax = 0;
		memset(pake, false, sizeof(pake));
		while (petak > 0) {
			max1 = 0;
			for (i = 1; i <= brs; i++) {
				for (j = 1; j <= klm; j++) {
					if (pake[i][j])
						byk[i][j] = 0;
					else
						byk[i][j] = 1;
				}
			}
			x = klm+1;
			y = brs+1;
			for (i = brs; i >= 1; i--) {
				for (j = klm; j >= 1; j--) {
					if (pake[i][j])
						continue;
					if ((mat[i][j] == mat[i+1][j+1]) && (mat[i][j] != mat[i][j+1]) && (mat[i][j] != mat[i+1][j])) {
						byk[i][j] = min(byk[i+1][j+1], min(byk[i+1][j], byk[i][j+1]))+1;
						
					}
					if (max1 <= byk[i][j]) {
						max1 = byk[i][j];
						if ((y > i) || ((y == i) && (x > j))) {
							y = i;
							x = j;
						}
					}
				}
			}
			/*
			for (i = 1; i <= brs; i++) {
				for (j = 1; j <= klm; j++) {
					cout << byk[i][j] << ' ';
				}
				cout << endl;
			}
			cout << max1 << ' ' << y << ' ' << x << endl;
			*/
			//cout << petak << ' ' << max1 << ' ' << x << ' ' << y << endl;
			pmax = max(pmax, max1);
			all[max1]++;
			for (i = y; i < y+max1; i++) {
				for (j = x; j < x+max1; j++) {
					pake[i][j] = true;
					byk[i][j] = 0;
					petak--;
				}
			}
			/*
			for (i = 1; i <= brs; i++) {
				for (j = 1; j <= klm; j++) {
					cout << byk[i][j] << ' ';
				}
				cout << endl;
			}
			cout << max1 << ' ' << y << ' ' << x << endl;
			system("pause");
			*/
		}
		cnt = 0;
		for (i = 512; i >= 1; i--) {
			if (all[i] > 0) {
				cnt++;
				//printf("%d %d\n", i, all[i]);
			}
		}
		printf("Case #%d: %d\n", nc, cnt);
		for (i = 512; i >= 1; i--) {
			if (all[i] > 0) {
				printf("%d %d\n", i, all[i]);
			}
		}
	}
}
