#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
const int inf = -10000000;
const int MAXN = 200;
#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef struct {
	int mi,mj,now;
}node;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
int mat[MAXN][MAXN];
node key[MAXN];

bool isOK(int x,int y) {
	return (x>0 && x<200 && y>0 && y<200);
}
inline void init() {
	for (int i=1;i<200;i++) {
		for (int j=1;j<200;j++) {
			mat[i][j]=inf;
		}
	}
}
bool vist[MAXN][MAXN];
void check(int mi, int mj, int &lim) {
	int i;
	for (i = 1;i <= lim; ++i) {
		if (key[i].mi == mi&&key[i].mj == mj) {
			break;
		}
	}
	if (i > lim) {
		lim++;
		key[lim].now=1;
		key[lim].mi=mi;
		key[lim].mj=mj;
	}
}
bool vist2[MAXN];

bool check2(int i, int j) {
	return (vist2[i] && isOK(key[j].mi,key[j].mj) &&isOK(key[i].mi,key[i].mj) 
		&&mat[key[i].mi][key[i].mj]==mat[key[j].mi][key[j].mj]&&mat[key[i].mi][key[i].mj]!=inf);
}
int max(int a, int b) {
	return a>b?a:b;
}
int doit(int x, int y, int xx) {
	int ret = 0;
	int len;
	for (int i=1;i <= xx;i++) {
		for (int j=1;j <= xx;j++) {
			if (mat[i][j] != inf && !vist[i][j]) {
				len = 1;
				key[len].mi=i;
				key[len].mj=j;
				key[len].now=1;
				check(i , 2 * y - j, len);
				check(2 * x - i, 2 * y - j, len);
				check(2 * x - i , 2 * y-j,len);
				memset(vist2,1,sizeof(vist2));
				for (int k = 1;k <= len; ++k) {
					if (vist2[k]) {
						for (int l = k+1;l <= len;l++) {
							if (check2(l, k))
							{
								key[k].now++;
								vist2[l]=false;
							}
						}

					}
				}
				int res = 0;
				for (int k = 1;k <= len;k++) {
					if (vist2[k]) {
						res = max(res, key[k].now);
					}
				}
				ret += (len-res);
			}
		}
	}
	return ret;
}

int slove(int x,int y, int xx) {
	memset(vist,0,sizeof(vist));
	return doit(x, y, xx);
}

int main()
{
        freopen("A2.in","r",stdin);
        freopen("A2.out","w",stdout);
	int T;
	int b = 1;
	scanf("%d",&T);
	while (T--) {
		int k, j;
		scanf("%d",&k);
		init();
		int tp = k - 2;
		for (int i=1;i<= k;i++) {
			for (int pp = 0, j= k-i+1;pp <= i;j += tp, ++pp) {
				scanf("%d",&mat[i][j]);
			}
		}
		for (int i = k + 1;i< 2 * k; ++i) {
			for (int pp = 0,j = 2 * k - i;pp <= i;j += tp, ++pp) {
				scanf("%d",&mat[i][j]);
			}
		}
		int ret = INT_MAX;
		for (int i = 1;i <= k; ++i)
		{
			for (j = 1;j <= i; ++j) {
				if (mat[i][j] != inf) {
					ret=min(ret, slove(i,j, k));
				}
			}
		}
		printf("Case #%d: %d\n", b ,ret);
		++b;
	}
}
