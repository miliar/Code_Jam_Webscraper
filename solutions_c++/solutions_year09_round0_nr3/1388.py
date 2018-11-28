#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>

#include <memory>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

#define TASK "C"

using namespace std;

typedef long long int64;

const string str = "welcome to code jam";

const int MAXL = 512;

int n;
int64 answer;
char t[MAXL];
int64 v[MAXL][20];

int main() {
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif

	scanf("%d\n", &n);

	for (int cs = 1; cs <= n; cs++) {
		gets(t);
		int len = strlen(t);

		printf("Case #%d: ", cs);

		memset(v, 0, sizeof(v));

		for (int i = 0; i < len; i++) {
			for (int j = 0; j < 19; j++) {
				if (str[j] == t[i]) {
					if (j == 0) {
						v[i][j] = 1;
					}
					else {
						for (int k = 0; k < i; k++) {
							v[i][j] += v[k][j-1];
						}
				   	}
				}
			}
		}

		answer = 0;
		for (int i = 0; i < len; i++) answer += v[i][18];

		if (answer >= 1000) printf("%I64d\n", answer % 10000);
		else if (answer >= 100) printf("0%I64d\n", answer);
		else if (answer >= 10) printf("00%I64d\n", answer);
		else printf("000%I64d\n", answer);
	}

	return 0;
}

