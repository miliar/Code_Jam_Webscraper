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

int len[3333333], shft[3333333][10], pow10[9];


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	pow10[0] = 1;
	for (int i = 1; i < 9; i++) pow10[i] = pow10[i-1]*10;

	len[0] = 0;
	for (int i = 1; i <= 3000000; i++) {
		len[i] = len[i / 10] + 1;
		int y = i;
		for (int j = 1; j < len[i]; j++) {
			y = y / 10 + (y % 10) * pow10[len[i] - 1];
			if (y >= pow10[len[i] - 1] && y < i) {
				shft[i][++shft[i][0]] = y;
			}
		}
		sort(shft[i] + 1, shft[i] + shft[i][0] + 1);
		shft[i][0] = unique(shft[i] + 1, shft[i] + shft[i][0] + 1) - shft[i] - 1;
//		printf("%d :", i);
//		for (int j = 1; j <= shft[i][0]; j++) printf(" %d", shft[i][j]);
//		puts("");
	}

	int T;
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		int ans = 0, A, B;
		cin >> A >> B;
		for (int y = A; y <= B; y++) {
			for (int j = 1; j <= shft[y][0]; j++) {
				if (shft[y][j] >= A) ans++;
			}
		}
		
		printf("Case #%d: ",_);
		cout << ans << endl;
	}

	return 0;
}
