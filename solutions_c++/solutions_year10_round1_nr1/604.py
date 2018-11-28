#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define	PI	3.14159265358979323846

#define	ABS(a)		((a) < 0 ? -(a) : (a))
#define	MIN(a, b)	((a) < (b) ? (a) : (b))
#define	MAX(a, b)	((a) > (b) ? (a) : (b))

#define	MAXN	100

int main(int argc, char *argv[])
{
	int nc, ci;
	int n, k, b, r, c;
	int i, j, ii, jj, flag;
	static char m[MAXN][MAXN], t;
	const char *res;
	
	scanf("%d", &nc);
	
	for (ci = 1; ci <= nc; ci++) {
		scanf("%d %d", &n, &k);
		for (i = 0; i < n; i++)
			scanf("%s", m[i]);
		for (i = 0; i < n; i++) {
			for ( ; ; ) {
				flag = 0;
				for (j = n - 1; j >= 0; j--) {
					if (j > 0 && m[i][j] == '.' && m[i][j - 1] != '.') {
						t = m[i][j], m[i][j] = m[i][j - 1], m[i][j - 1] = t;
						flag = 1;
					}
				}
				if (flag == 0) break;
			}
		}
		
		// for (i = 0; i < n; i++) printf("%s\n", m[i]);

		b = r = 0;
		
		for (i = 0; i < n; i++) {
			for (j = 0; j <= n - k; j++) {
				if (m[i][j] == 'B') {
					c = 0;
					for (jj = 0; jj < k; jj++)
						if (m[i][j + jj] == 'B') c++;
					if (c == k) b++;
				} else if (m[i][j] == 'R') {
					c = 0;
					for (jj = 0; jj < k; jj++)
						if (m[i][j + jj] == 'R') c++;
					if (c == k) r++;
				}
			}
		}

		for (j = 0; j < n; j++) {
			for (i = 0; i <= n - k; i++) {
				if (m[i][j] == 'B') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i + ii][j] == 'B') c++;
					if (c == k) b++;
				} else if (m[i][j] == 'R') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i + ii][j] == 'R') c++;
					if (c == k) r++;
				}
			}
		}
		
		for (i = 0; i <= n - k; i++) {
			for (j = 0; j <= n - k; j++) {
				if (m[i][j] == 'B') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i + ii][j + ii] == 'B') c++;
					if (c == k) b++;
				} else if (m[i][j] == 'R') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i + ii][j + ii] == 'R') c++;
					if (c == k) r++;
				}
			}
		}
		
		for (i = k - 1; i < n; i++) {
			for (j = 0; j <= n - k; j++) {
				if (m[i][j] == 'B') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i - ii][j + ii] == 'B') c++;
					if (c == k) b++;
				} else if (m[i][j] == 'R') {
					c = 0;
					for (ii = 0; ii < k; ii++)
						if (m[i - ii][j + ii] == 'R') c++;
					if (c == k) r++;
				}
			}
		}
		
		if (r == 0 && b == 0) res = "Neither";
		else if (r > 0 && b > 0) res = "Both";
		else if (r > 0) res = "Red";
		else if (b > 0) res = "Blue";
		
		printf("Case #%d: %s\n", ci, res);
	}

	return 0;
}
