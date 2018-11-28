#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for (i=a; i<=b; i++)
#define fj(a, b) for (j=a; j<=b; j++)
#define fo(a, b) for (o=a; o<=b; o++)
#define fdi(a, b) for (i=a; i>=b; i--)
#define fdj(a, b) for (j=a; j>=b; j--)
#define fdo(a, b) for (o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(y))

typedef long long int64;

int t;
int n;
int q;

int main() {
	int i, j, o;
	int l;
	char str[100];
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d", &t);
	int f;
	fi(1, t) {
		scanf("%s", &str);
		l = strlen(str);
		printf("Case #%d: ", i);
		f = 0;
		if (l != 1) {
			fj(1, l - 1) {
				if (str[j] != '0') {
					f = 1;
					break;
				}
			}
			if (!f) {
				fj(0, l - 1) {
					printf("%c", str[j]);
				}
				printf("0");
				printf("\n");
				continue;
			}
		}
		if (next_permutation(str, str + l)) {
			printf("%s", str);
		} else {
			q = 0;
			fj(0, l - 1) {
				if (str[j] == '0') q++;
			}
			sort(str, str + l);
			o = 0;
			while (str[o] == '0') o++;
			printf("%c", str[o]);
			fj(1, q + 1) {
				printf("0");
			}
			fj(o + 1, l - 1) {
				printf("%c", str[j]);
			}
		}
		printf("\n");
	}
	return 0;
}