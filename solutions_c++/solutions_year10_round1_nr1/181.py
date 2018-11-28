#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define IN(x,y) ((x)>=0&&(x)<n&&(y)>=0&&(y)<n)
const int dir[][2] = {{0,1},{1,0},{1,1},{1,-1}};
char buf[64][64];
int k, n;

int check(char ch) {
	int i, j,d, tx, ty;
	for (i = 0 ; i < n ; i++)
		for (j = 0 ; j < n ; j++) {
			if (buf[i][j] != ch) continue;
			for (d = 0 ; d < 4 ; d++) {
				tx = i; ty = j;
				int cnt = 1;
				while (1) {
					tx += dir[d][0];
					ty += dir[d][1];
					if (!IN(tx,ty) || buf[tx][ty] != ch) break;
					if (++cnt >= k) {
						//printf("i:%d j:%d d:%d cnt:%d %d %d\n",i,j,d,cnt,tx,ty);
						return 1;
					}
				}
			}
		}
	return 0;
}

int main() {
	//freopen("a-small.in","r",stdin);
	//freopen("a-small.out","w",stdout);
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int T, ca;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++) {
		scanf("%d%d",&n,&k);
		int i, j;
		for (i = 0 ; i < n ; i++)
			scanf("%s",buf[i]);
		for (i = 0 ; i < n ; i++) {
			int p = n - 1;
			for (j = n - 1 ; j >= 0 ; j--) {
				if (buf[i][j] == '.') continue;
				else buf[i][p--] = buf[i][j];
			}
			for ( ; p >= 0 ; p--)
				buf[i][p] = '.';
			//printf("%s\n",buf[i]);
		}
		int flg = 0;
		if (check('R')) flg += 1;
		if (check('B')) flg += 2;
		printf("Case #%d: ",ca);
		if (flg == 0) printf("Neither\n");
		else if (flg == 1) printf("Red\n");
		else if (flg == 2) printf("Blue\n");
		else printf("Both\n");
	}
	return 0;
}
