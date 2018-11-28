//USER LGQ
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <set>
#include <deque>

using namespace std;

const int maxn = 1100;

int qiut[maxn];

bool isprime[maxn];
int prime[maxn], pn;
void getpri() {
	memset(isprime, true, sizeof (isprime));
	isprime[0] = isprime[1] = false;
	pn = 0;
	for (int i = 2; i < maxn; i++) {
		if (isprime[i]) {
			prime[pn++] = i;
			if (i * i < maxn)
				for (int j = i + i; j < maxn; j += i)
					isprime[j] = false;
		}
	}
}

int main() {
    int T, n, cas = 1;
    getpri();
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        int left = 0, right = 0;
		if (n == 1) {
            printf("Case #%d: 0\n", cas++); continue;
        }
		memset(qiut, 0, sizeof(qiut));
        for (int i = 2; i <= n; ++i) {
            for (int j = 0; prime[j] <= i; j++) {
                if (i % prime[j] == 0) {
                    int cnt = 0, tmp = i;
                    if (qiut[prime[j]] == 0) ++left;
                    while (tmp % prime[j] == 0) {
                        tmp /= prime[j];
                        cnt++;
                    } 
                    if (cnt > qiut[prime[j]]) qiut[prime[j]] = cnt;
                }
            }
        }
        for (int i = 2; i <= n; ++i) right += qiut[i];
		int res = right + 1 - left;
        printf("Case #%d: %d\n", cas++, res);
    }
    return 0;
}
