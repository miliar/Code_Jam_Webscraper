#include <stdio.h>
#include <map>
#include <cassert>
#include <iostream>

using namespace std;

int main() {
	int N;
	int k = 1;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		map<char, long long> m;
		char s[500];
		scanf("%s", s);
		int len = strlen(s);
		m[s[0]] = 1;
		long long next = -1;
		for (int j = 1; j < len; j++) {
			if (m.count(s[j]) == 0) {
				next++;
				if (next == 1) next++;
				m[s[j]] = next;
			}
		}
		long long base = next + 1;
		if (base == 0) base++;
		if (base == 1) base++;
		assert(base > 1);
		//printf("base: %d\n",base);
		long long ans = 0;
		long long place = 1;
		for (int j = len - 1; j >= 0; j--) {
			ans += (long long)place * (long long)m[s[j]];
			//printf("ans: %d\n",ans);
			place *= base;
		}
		cout << "Case #" << k++ << ": " << ans << endl;
	}
	return 0;
}