#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#define zbwmqlw
#define PI 3.141592653589793238463
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define fill(x,y) memset((x),(y),sizeof(x))
#define lch(x) (((x)<<1)+1)
#define rch(x) (((x)<<1)+2)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>0?(x):-(x))
#define two(x) (1<<(x))

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;

const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) 
{if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) 
{if (b>a) a=b;}


int T,t,n;
bool map[2][105][105];

bool empty(int ID)
{
	for (int i = 1; i <= 100; ++i) for (int j = 1; j <= 100; ++j) 
		if (map[ID][i][j] == 1) return false;
	return true;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	for (scanf("%d\n",&T),t = 1; t <= T; ++t) {
		scanf("%d",&n);
		fill(map[0], 0);
		for (int i = 1; i <= n; ++i) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x) for (int y = y1; y <= y2; ++y) map[0][x][y] = true;
		}
		int round = 0;
		while (!empty(round&1)) {
			++round;
			int now = round & 1;
			int last = (round - 1) & 1;
			for (int i = 1; i <= 100; ++i) for (int j = 1; j <= 100; ++j) {
				map[now][i][j] = map[last][i][j];
				if (map[last][i][j-1] == 0 && map[last][i-1][j] == 0) map[now][i][j] = 0;
				if (map[last][i][j-1] == 1 && map[last][i-1][j] == 1) map[now][i][j] = 1;
			}
		}
		printf("Case #%d: %d\n", t, round);
	}
}
