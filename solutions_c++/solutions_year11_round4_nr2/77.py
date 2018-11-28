#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <complex>
#include <set>
#include <map>

using namespace std;

const int MAXN = 505;

#define ll long long

int T;

int R, C, D;
char temp[MAXN][MAXN];
complex< ll > mem[MAXN][MAXN];
complex< ll > sum[MAXN][MAXN];

ll mem2[MAXN][MAXN];
ll sum2[MAXN][MAXN];

int main() {
	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d %d\n",&R,&C,&D);
		for(int i = 1 ; i <= R ; i++) {
			scanf("%s\n",temp[i]);
			for(int j = 1 ; j <= C ; j++) {
				ll mult = temp[i][j - 1] - '0';
				mem[i][j] = complex< ll >(mult * i, mult * j);
				mem2[i][j] = mult;
			}
		}
		for(int i = 0 ; i < MAXN ; i++) {
			sum[i][0] = complex< ll >(0,0);
			sum[0][i] = complex< ll >(0,0);
			sum2[i][0] = 0;
			sum2[0][i] = 0;
		}
		for(int i = 1 ; i <= R ; i++) {
			for(int j = 1 ; j <= C ; j++) {
				sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + mem[i][j];
				sum2[i][j] = sum2[i - 1][j] + sum2[i][j - 1] - sum2[i - 1][j - 1] + mem2[i][j];
			}
		}
		
		int len = min(R, C);
		while (len >= 3) {
			bool done = false;
			for(int i = 1 ; i + len <= R + 1 && !done; i++) {
				for(int j = 1 ; j + len <= C + 1 ; j++) {
					//i + (len - 1) / 2;
					//j + (len - 1) / 2;
					complex< ll > center2 = complex< ll >(2 * i + len - 1, 2 * j + len - 1);
					complex< ll > tot = sum[i + len - 1][j + len - 1] - sum[i - 1][j + len - 1] - sum[i + len - 1][j - 1] + sum[i - 1][j - 1];
					tot -= (mem[i][j] + mem[i + len - 1][j] + mem[i][j + len - 1] + mem[i + len - 1][j + len - 1]);
					tot *= 2;
					
					ll tot2 = sum2[i + len - 1][j + len - 1] - sum2[i - 1][j + len - 1] - sum2[i + len - 1][j - 1] + sum2[i - 1][j - 1];
					tot2 -= (mem2[i][j] + mem2[i + len - 1][j] + mem2[i][j + len - 1] + mem2[i + len - 1][j + len - 1]);
					
					if (tot == center2 * tot2) {
						done = true;
						break;
					}
				}
			}
			if (done) {break;}
			len--;
		}
		printf("Case #%d: ",t);
		if (len >= 3) {
			printf("%d\n",len);
		}	else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
