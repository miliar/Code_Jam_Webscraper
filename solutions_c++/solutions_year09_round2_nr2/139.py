#include <stdio.h>
#include <algorithm>

using namespace std;

char s[100];

int main() {
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		memset(s, 0, sizeof(s));
		gets(s);
		if (!next_permutation(s, s + strlen(s))) {
			int n = strlen(s);
			sort(s, s+n);
			int j = 0;
			while (s[j] == '0') ++j;
			swap(s[j], s[0]);
			for (int i = n; i > 1; --i)
				s[i] = s[i-1];
			s[1] = '0';
		}
		printf("Case #%d: %s\n", i+1, s);
	}
}