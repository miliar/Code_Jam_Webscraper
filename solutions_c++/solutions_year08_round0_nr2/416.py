#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 

#define N 500

int t, na, nb;

int AX[N], AY[N], BX[N], BY[N];

int main () {
	int i, j, T, x, y, pos = 0;
	char str[100];

	scanf("%d", &T);

	for (int cas = 1; cas <= T; cas++) {
		
		scanf("%d%d%d", &t, &na, &nb);
		
		for (i = 0; i < na; i++) {
			scanf("%s", str); str[2] = ' '; sscanf(str, "%d%d", &x, &y); AX[i] = x * 60 + y;
			scanf("%s", str); str[2] = ' '; sscanf(str, "%d%d", &x, &y); AY[i] = x * 60 + y;
		}
		for (i = 0; i < nb; i++) {
			scanf("%s", str); str[2] = ' '; sscanf(str, "%d%d", &x, &y); BX[i] = x * 60 + y;
			scanf("%s", str); str[2] = ' '; sscanf(str, "%d%d", &x, &y); BY[i] = x * 60 + y;
		}

		sort(AX,AX+na); sort(BX,BX+nb); sort(AY,AY+na); sort(BY,BY+nb);
		int ra = 0, rb = 0;

		for (i = 0, pos = 0; i < na; i++) {
			for (j = pos; j < nb; j++) {
				if (AY[i] + t <= BX[j]) {
					rb++;
					pos = j+1;
					break;
				}
			}
		}
		
		for (i = 0, pos = 0; i < nb; i++) {
			for (j = pos; j < na; j++) {
				if (BY[i] + t <= AX[j]) {
					ra++;
					pos = j+1;
					break;
				}
			}
		}

		printf("Case #%d: %d %d\n", cas, na-ra, nb-rb);
	}


	return 0;
}