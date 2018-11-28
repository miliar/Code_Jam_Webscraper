#include<cstdio>
#include<cstring>
char s[600];
const char ss[] = "welcome to code jam";
int cache[600][20];

int doit(int len, int move) {
	if ( cache[len][move] != -1 ) return cache[len][move];
	if ( move == 0 ) return ( cache[len][move] = (s[len] == ss[move]) );
	int ret = 0;
	for(int i=len-1; i >= 0; i--) if ( s[i] == ss[move-1] ) ret = (ret + doit(i, move-1)) % 10000;
	return (cache[len][move] = ret);
}

int main() {
	int ntc;
	scanf("%d", &ntc);
	getchar();
	for(int TC=1; TC<=ntc; TC++) {
		gets(s);
		int len = strlen(s) - 1;
		int ans = 0;
		memset(cache, -1, sizeof(cache));
		for(int i=len; i>=0; i--) if ( s[i] == 'm' ) ans = ( ans + doit(i,18)) % 10000;
		printf("Case #%d: %04d\n", TC, ans);
	}
	return 0;
}
