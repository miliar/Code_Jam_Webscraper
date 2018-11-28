#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <memory>
#include <vector>
#include <string>
#include <set>
#include <map>

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long int64;

int T;

const int MAXN = 64;

char a[MAXN][MAXN];
int n, k;

void printA() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			printf("%c", a[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

const int di[4] = {1, 1, 0, -1},
		  dj[4] = {0, 1, 1, 1};

bool check(int i, int j, int w, char c) {
	int p = i, q = j, counter = 0;
	while (1 <= p && p <= n && 1 <= q && q <= n && a[p][q] == c) {
		counter++;
		p += di[w];
		q += dj[w];
	}

	return (counter >= k);
}

int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		cerr << cs << endl;
		printf("Case #%d: ", cs);

		memset(a, 0, sizeof(a));

		scanf("%d %d\n", &n, &k);

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				scanf("%c", &a[i][j]);
			}
			scanf("\n");
		}

		//printA();

		for (int j = n; j >= 1; j--) {
			for (int i = 1; i <= n; i++) {
				if (a[i][j] != '.') {
					for (int r = j+1; r <= n && a[i][r] == '.'; r++) {
						swap(a[i][r-1], a[i][r]);
					}
				}
			}
		}

		//printA();

		int ans = 0;

        for (int i = 1; i <= n; i++) {
        	for (int j = 1; j <= n; j++) {
        		if (a[i][j] != '.') {
        			for (int w = 0; w < 4; w++) {
        				if (check(i, j, w, 'B')) ans |= 1;
        				if (check(i, j, w, 'R')) ans |= 2;
        			}
        		}
        	}
        }

        if (ans == 0) printf("Neither");
        if (ans == 1) printf("Blue");
        if (ans == 2) printf("Red");
        if (ans == 3) printf("Both");

		printf("\n");
	}

	return 0;
}

