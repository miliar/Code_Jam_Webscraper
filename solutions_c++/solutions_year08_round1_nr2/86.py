#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int p[2100];
int psa[2100];
int n;

int f[2010][2100][2];
int mf[2010];
int m;

int choose[2010];

bool hasnotsa(int &num)
{
	int i;

	for (i = 0; i < n; i ++) {
		if (psa[i] == 0) {
			num = i;
			return true;
		}
	}

	return false;
}

bool solve()
{
	int i, j, k;
	int num;

	for (i = 0; i < n; i ++) {
		psa[i] = 0;
	}
	for (i = 0; i < m; i ++) {
		choose[i] = 0;
		for (j = 0; j < mf[i]; j ++) {
			if (f[i][j][1] == 0) {
				psa[f[i][j][0]] ++;
			}
		}
	}

	while(hasnotsa(num)) {
		if (p[num] == -1) {
			return false;
		}

		choose[p[num]] = 1;
		for (i = 0; i < mf[p[num]]; i ++) {
			if (f[p[num]][i][1] == 1) {
				psa[f[p[num]][i][0]] ++;
			}
			else {
				psa[f[p[num]][i][0]] --;
			}
		}
	}

	return true;
}

int main()
{
	int i, j, k;
	int t;
	int a, b;
	int nowt;
	int np;

	freopen("B-large.in.txt", "r", stdin);
//	freopen("B-large.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;

		scanf("%d", &m);
		scanf("%d", &n);
		for (i = 0; i < m; i ++) {
			mf[i] = 0;
		}

		for (i = 0; i < n; i ++) {
			scanf("%d", &np);
			p[i] = -1;
			for (j = 0; j < np; j ++) {
				scanf("%d%d", &a, &b);
				a --;

				if (b == 1) p[i] = a;

				f[a][mf[a]][0] = i;
				f[a][mf[a]][1] = b;
				mf[a] ++;
			}
		}

		if (solve() == false) {
			printf("Case #%d: IMPOSSIBLE\n", nowt);
		}
		else {
			printf("Case #%d:", nowt);
			for (i = 0; i < m; i ++) {
				printf(" %d", choose[i]);
			}
			printf("\n");
		}
	}

	return 0;
}
