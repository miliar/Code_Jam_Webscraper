#include <cstring>
#include <map>
#include <cstdio>

using namespace std;

map<char, char> mp;

void init() {

	mp[' ']=' ';mp['a']='y';mp['b']='h';mp['c']='e';
	mp['d']='s';mp['e']='o';mp['f']='c';mp['g']='v';
	mp['h']='x';mp['i']='d';mp['j']='u';mp['k']='i';
	mp['l']='g';mp['m']='l';mp['n']='b';mp['o']='k';
	mp['p']='r';mp['r']='t';mp['s']='n';mp['t']='w';
	mp['u']='j';mp['v']='p';mp['w']='f';mp['x']='m';
	mp['y']='a';mp['q']='z';mp['z']='q';
}

int main() {
	init();
	int T;
	char s[120];
	scanf("%d", &T);
	getchar();
	for (int re = 1; re <= T; ++re) {
		gets(s);
		for (int i = 0; s[i]; ++i) {
			s[i] = mp[s[i]];
		}
		printf("Case #%d: ", re);
		puts(s);
	}
	return 0;
}
