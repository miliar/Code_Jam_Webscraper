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

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


bool hash[110][110];
bool tp[110][110];
int main() {
	int T;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d",&T);
	int b = 1;
	while (T--) {
		int R;
		scanf("%d", &R);

		while (R--) {
			int x0,x1,y0,y1;
			scanf("%d%d%d%d",&x0, &y0, &x1, &y1);
			for (int i = x0; i <= x1; ++i) {
				for (int j = y0; j<= y1; ++j) {
					hash[j][i] = true;
				}
			}
		}
		int T = 0;
		while (1)
		{
			bool flag = true;
			for (int i = 1; i <= 100; ++i) {
				for (int j = 1 ; j<= 100; ++j) {
					if (hash[i][j]) {
						flag = false;
						goto l1;
					}
				}
			}
l1:
			if (flag) {
				break;
			}
			memset(tp,0, sizeof(tp));
			for (int i = 1; i <= 100; ++i) {
				for (int j = 1 ; j<= 100; ++j) {
					if (hash[i][j]) {
						if (hash[i-1][j] || hash[i][j-1]) {
							tp[i][j] = true;
						}
					} else {
						if (hash[i-1][j] && hash[i][j-1]) {
							tp[i][j] = true;
						}
					}
				}
			}
			++T;
			memcpy(hash, tp, sizeof(hash));
		}
		printf("Case #%d: ", b);
		printf("%d\n", T);
		++b;
	}
	return 0;
}