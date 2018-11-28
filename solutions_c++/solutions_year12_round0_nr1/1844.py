#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 128;

char s[MAXN];
char mp[MAXN<<1];

void init() {
	
	for (int i=0; i<MAXN*2; ++i) mp[i] = i;
	
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
}

int main() {
	int i, j, k;
	int m, n;
	int tc, cn(0);
	
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	init();	
	scanf("%d", &tc);
	gets(s);
	while (tc--) {
		gets(s);
		printf("Case #%d: ", ++cn);
		for (i=0; s[i]; ++i) printf("%c", mp[s[i]]);
		puts("");
	}
	
	return 0;
}