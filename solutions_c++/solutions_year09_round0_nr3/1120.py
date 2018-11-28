#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define COPY(a, b) memcpy(a, b, sizeof(b))

#define LEN 1000
#define MOD 10000

int n;
char str[LEN];
int ans;
int d[LEN][LEN];
int len;

char text[20] = "welcome to code jam";

void Solve() {
	int i, j, o;
	ZERO(d);
	len = (int)strlen(str);
	fi(0, len - 1) {
		fj(0, 18) {
			if (str[i] == text[j]) {
				if (j == 0) {
					d[i][j]++;
					d[i][j] %= MOD;
				} else {
					fdo(i - 1, 0) {
						if (str[o] == text[j - 1]) {
							d[i][j] += d[o][j - 1];
							d[i][j] %= MOD;
						}
					}
				}
			}
		}
	}
	fi(0, len - 1) {
		ans += d[i][18];
		ans %= MOD;
	}
}

int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	gets(str);
	sscanf(str, "%d", &n);
	fi(1, n) {
		gets(str);
		ans = 0;
		Solve();
		printf("Case #%d: %04d\n", i, ans);
	}
	return 0;
}