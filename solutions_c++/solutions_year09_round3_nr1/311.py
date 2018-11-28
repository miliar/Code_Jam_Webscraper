#include <cstdio>

int main(){
	int T = 0;
	char buf[1024];
	scanf("%d ", &T);
	for(int ttt = 1; ttt <= T; ttt++){
		char map[256] = {0};
		scanf("%s ", buf);
		int chars = 0, len = 0;
		for(; buf[len]; len++){
			if(!map[buf[len]]) map[buf[len]] = ++chars;
			buf[len] = map[buf[len]] - 1;
		}
		long long ret = 0;
		chars += (chars <= 1);
		for(int i = 0; i < len; i++){
			ret = ret * chars + (buf[i] ^ (buf[i] < 2));
		}
		printf("Case #%d: %lld\n", ttt, ret);
	}
	return 0;
}
