#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char rbt[2];
int rbtI[105];
int idx[105];
int p[2];
int q[2][105];
int aw[2], ak[2];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int nc, tc, i, n;
	int tambah, selisih, waktu;
	int nowR, othR;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		aw[0] = aw[1] = 0;
		ak[0] = ak[1] = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s%d", rbt, &idx[i]);
			if (rbt[0] == 'O')
				rbtI[i] = 0;
			else
				rbtI[i] = 1;
			q[rbtI[i]][ak[rbtI[i]]++] = idx[i];
		}
		waktu = 0;
		p[0] = p[1] = 1;
		for (i = 0; i < n; i++) {
			nowR = rbtI[i];
			othR = 1-nowR;
			tambah = abs(p[nowR]-idx[i])+1;
			p[nowR] = idx[i];
			selisih = q[othR][aw[othR]]-p[othR];
			if (abs(selisih) <= tambah)
				p[othR] = q[othR][aw[othR]];
			else
				p[othR] += (selisih/abs(selisih))*tambah;
			aw[nowR]++;
			waktu += tambah;
		}
		printf("Case #%d: %d\n", nc, waktu);
	}
}
