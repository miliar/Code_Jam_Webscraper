#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#define N 1005
using namespace std;

char s[N],t[N],mp[N],buf[5];
int TC,n;

int main(){
	scanf("%d",&TC);
	gets(buf);
	mp['a'] = 'y';
	mp['b'] = 'n';
	mp['c'] = 'f';
	mp['d'] = 'i';
	mp['e'] = 'c';
	mp['f'] = 'w';
	mp['g'] = 'l';
	mp['h'] = 'b';
	mp['i'] = 'k';
	mp['j'] = 'u';
	mp['k'] = 'o';
	mp['l'] = 'm';
	mp['m'] = 'x';
	mp['n'] = 's';
	mp['o'] = 'e';
	mp['p'] = 'v';
	mp['q'] = 'z';
	mp['r'] = 'p';
	mp['s'] = 'd';
	mp['t'] = 'r';
	mp['u'] = 'j';
	mp['v'] = 'g';
	mp['w'] = 't';
	mp['x'] = 'h';
	mp['y'] = 'a';
	mp['z'] = 'q';
	for (int test=1;test<=TC;test++){
		memset(s,0,sizeof(s));
		gets(s);
		n = strlen(s);
		printf("Case #%d: ",test);
		for (int i=0;i<n;i++)
			if ('a' <= s[i] && s[i] <= 'z'){
				for (char c='a';c<='z';c++)
					if (mp[c]==s[i])
						printf("%c",c);
			}
			else printf("%c",s[i]);
		printf("\n");
	}
	return 0;
}
