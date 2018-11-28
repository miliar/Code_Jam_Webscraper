#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>

using namespace std;

char s[1000000];
char t[1000000];
int a[100];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int k; scanf("%d", &k);
		scanf("%s", s);
		for (int i = 0; i < k; ++i) {
			a[i] = i;
		}
		int result = strlen(s);
		do {
			int q = 0;
			for (int i = 0; s[i] != 0; ++i) {
				t[i] = s[(i / k) * k + a[i % k]];
				if (!i || (t[i] != t[i - 1])) ++q;
			}
			if (q < result) result = q;
		} while (next_permutation(a, a + k));
		printf("Case #%d: ", tt + 1);
		printf("%d\n", result);
	}
	return 0;
}
