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

const int MAXN = 128;

bool a[MAXN][MAXN], b[MAXN][MAXN];
             
int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		memset(a, 0, sizeof(a));

		int r;
        scanf("%d", &r);

        for (int i = 1; i <= r; i++) {
        	int x1, y1, x2, y2;
        	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			
			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					a[x][y] = true;
				}
			}
        }

        int timer = 0;
        bool did = true;
        while (did) {
        	timer++;
        	did = false;

        	memset(b, 0, sizeof(b));

        	for (int x = 1; x < MAXN; x++) {
        		for (int y = 1; y < MAXN; y++) {
        			if (a[x][y]) {
        				if (a[x-1][y] || a[x][y-1]) {
        					b[x][y] = true;
        					did = true;
        				}
        			}
        			else {
        				if (a[x-1][y] && a[x][y-1]) {
        					b[x][y] = true;
        					did = true;
        				}
        			}
        		}
        	}

        	memcpy(a, b, sizeof(b));
        }

        printf("%d", timer);

		printf("\n");
	}

	return 0;
}

