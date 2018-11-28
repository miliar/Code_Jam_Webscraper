#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;
static double a[100];
static double b[100];
static double c[100];
static char d[100][100];
static int cnt[100];

static void solve(int t)
{
	int n;
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	memset(c, 0, sizeof(c));
	memset(d, 0, sizeof(d));
	memset(cnt, 0, sizeof(cnt));
	
	scanf("%d", &n);
	getchar();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char r  = getchar();
			d[i][j] = r;
			switch(r) {
			case '1':
				a[i] += 1; 
				break;
			case '0':
				break;
			case '.':
				cnt[i]--;
				break;
			}
		}
		getchar();
		cnt[i] += n;
		a[i] /= cnt[i];
		fprintf(stderr, "%lf\n", a[i]);
	}

	// compute b[i]
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) if (i != j && d[i][j] != '.') {
			double tmp = a[j] * cnt[j];
			fprintf(stderr, "tmp %d %d %lf %c %c\n", i, j, tmp, d[i][j], d[j][i]); 
			b[i] += (tmp - (d[j][i] == '1'? 1: 0)) / (cnt[j] - 1);
		}
		b[i] /= cnt[i];
		fprintf(stderr, "%lf\n", b[i]);
	}

	// compute c[i]
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) 
			if (i != j && d[i][j] != '.')
				c[i] += b[j];
		c[i] /= cnt[i];
	}
	printf("\n");
	for (int i = 0; i < n; i++) {
		printf("%.6lf\n", a[i] / 4 + b[i] / 2 + c[i] / 4);
	}
}


int main()
{
  int T;
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  freopen("err.out", "w", stderr);
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    //printf("", i + 1);
  }
  return 0;
}