#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

char map[256];

int main(int ac, char **av) {
	int N;
	char buf[100];
	int dig[100];

	cin >> N;
	for(int t=1; t <= N; t++) {
		unsigned long long ans = 0;

		cin >> buf;
		int len = strlen(buf);
		for(int i = 0; i < 256; ++i)
			map[i] = -1;

		int next = 0;
		for(int i =0; i < len; ++i) {
			if(i==0) {
				map[buf[i]] = 1;
				dig[0] = 1;
			}
			else if(map[buf[i]]==-1) {
				map[buf[i]] = next;
				dig[i] = next;
				next++;
				if(next==1)
					next=2;
			}
			else
				dig[i] = map[buf[i]];
		}
		if(next<2) next=2;

		unsigned long long base=1;
		for(int i = len-1; i>=0 ; --i) {
			if(dig[i]!=0)
				ans += dig[i] * base;
			base *= next;
		}
		printf("Case #%d: %lld\n", t, ans);
	}
	return 0;
}

