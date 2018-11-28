#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f

#define maxl (1 << 7)

char num[maxl];
int cnt[10];

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
		int l, i, j;
		memset(num, 0, sizeof(num));
		scanf(" %s", num);
		l = strlen(num);
		for(i = 0; i < l; i++) num[i] -= '0';
		std::reverse(num, num+l);
		for(i = 0; ; i++) {
			for(j = num[i]+1; j < 10 && cnt[j] == 0; j++);
			cnt[num[i]]++;
			if(j < 10) break;
		}
		for(cnt[num[i--] = j]--; i >= 0; i--) {
			for(j = 0; j < 10 && cnt[j] == 0; j++);
			num[i] = j;
			cnt[j]--;
		}
		for(i = maxl-1; i > 0 && num[i] == 0; i--);
		for(; i >= 0; i--)
			printf("%c", num[i] + '0');
		printf("\n");
	}
	return 0;
}
