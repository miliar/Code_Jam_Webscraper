#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>

#define inf 0x3f3f3f3f
#define maxl (1 << 16)
#define maxk (1 << 3)
char s[maxl];
int l, k;

int perm[maxk];
char ps[maxl];

int main() {
	int t, tc, i, j, n;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		scanf("%d %s", &k, s);
		l = strlen(s);
		n = l / k;
		for(i = 0; i < k; i++) perm[i] = i;
		int bans = inf;
		do {
			for(i = 0; i < k; i++)
				for(j = 0; j < n; j++)
					ps[i + j*k] = s[perm[i] + j*k];
			int cur = 1;
			for(i = 1; i < l; i++)
				if(ps[i] != ps[i-1]) cur++;
			if(bans > cur) bans = cur;
		} while(std::next_permutation(perm, perm+k));
		printf("Case #%d: %d\n", t, bans);
	}
	return 0;
}
