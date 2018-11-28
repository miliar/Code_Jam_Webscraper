#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define MAXN 805

using namespace std;

int jmlcase;
int n;
int angka[2][MAXN];
int a,b,c,d,e;

int main() {
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d",&n);
		for (a = 0;a < 2;a++) {
			for (b = 0;b < n;b++) {
				scanf("%d",&angka[a][b]);
				}
			}
		sort(angka[0],angka[0] + n);
		sort(angka[1],angka[1] + n);
		long long jawab = 0;
		for (a = 0;a < n;a++) {
			jawab += ((long long)angka[0][a] * (long long)angka[1][n - a - 1]);
			}
		
		printf("Case #%d: %lld\n",e + 1,jawab);
		}
	return 0;
	}


