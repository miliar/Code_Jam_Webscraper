#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define Nul(a) memset(a, 0, sizeof(a))
#define Fil(a, b) memset(a, b, sizeof(a))
#define Size(a) ((int)a.size())

char s[50];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		printf("Case #%d: ", ti);
		scanf("%s", s);
		int l = strlen(s);
		if (!next_permutation(s, s + l)) {
			sort(s, s + l);
			int nz = 1;
			for (int i = 0; ;i++) {
				if (s[i] == '0') {
					nz++;
					continue;
				}
				printf("%c", s[i]);
				for (int j = 0; j < nz; j++) printf("0");
				printf("%s\n", s + i + 1);
				break;
			}
		} else {
			printf("%s\n", s);
		}
	}
	return 0;
}