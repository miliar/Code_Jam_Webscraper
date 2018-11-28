#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
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

const int N=3000;

int f[N][50],limit[N],cost[N];
int T;
int n,p,t;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	for (scanf("%d",&T), t = 1; t <= T; ++t) {
		scanf("%d",&p);
		n = two(p);
		for (int i = n; i < n + n; ++i) {
			scanf("%d",&limit[i]);
			limit[i] = p - limit[i];
		}
		for (int layer = p - 1; layer >= 0; --layer) for (int i = two(layer); i < two(layer + 1); ++i) scanf("%d", &cost[i]);
		for (int i = n + n - 1; i >= 1; --i) for (int j = 0; j <= p; ++j)
			if (i >= n) 
				f[i][j] = (j >= limit[i] ? 0 : inf);
			else {
				f[i][j] = min(inf, f[i * 2][j] + f[i * 2 + 1][j]);
				if (j < p) checkmin(f[i][j], f[i * 2][j + 1] + f[i * 2 + 1][j + 1] + cost[i]);
			}
		printf("Case #%d: %d\n", t, f[1][0]);
	}
}
