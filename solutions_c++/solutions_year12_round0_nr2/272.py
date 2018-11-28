#include <stdio.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <bitset>
#include <time.h>
#include <climits>

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int n, s, p, a[1111];
int f[333][333];
int sur[333], nsur[333];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	for (int i = 0; i <= 10; i++)
		for(int j = i; j <= 10; j++)
			for (int k = j; k <= 10; k++)
				if (k - i <= 2) {
					if (k - i == 2)
						sur[i + j + k] = max(sur[i + j + k], k);else
						nsur[i + j + k] = max(nsur[i + j + k], k);
				}

	int T;
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		cin >> n >> s >> p;
		for (int i  = 0; i < n; i++) cin >> a[i];

		memset(f, 128 + 63, sizeof(f));

		f[0][0] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) if (f[i][j] >= 0) {
				f[i + 1][j] = max(f[i + 1][j], f[i][j] + (nsur[a[i]] >= p));
				f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + (sur[a[i]] >= p));
			}
		}
		
		printf("Case #%d: ",_);
		if (f[n][s] < 0) f[n][s] = 0;
		cout << f[n][s] << endl;
	}

	return 0;
}
