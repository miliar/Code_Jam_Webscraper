#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int n;
char ent[1001], sai[1001], conv[256];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int t;
	scanf("%d", &t);
	gets(ent);
	memset(conv, '!', 256);
	conv[' '] = ' ';	conv['a'] = 'y';
	conv['b'] = 'h';	conv['c'] = 'e';
	conv['d'] = 's';	conv['e'] = 'o';
	conv['f'] = 'c';	conv['g'] = 'v';
	conv['h'] = 'x';	conv['i'] = 'd';
	conv['j'] = 'u';	conv['k'] = 'i';
	conv['l'] = 'g';	conv['m'] = 'l';
	conv['n'] = 'b';	conv['o'] = 'k';
	conv['p'] = 'r';	conv['q'] = 'z';
	conv['r'] = 't';	conv['s'] = 'n';
	conv['t'] = 'w';	conv['u'] = 'j';
	conv['v'] = 'p';	conv['w'] = 'f';
	conv['x'] = 'm';	conv['y'] = 'a';
	conv['z'] = 'q';	
	for(int _ = 1; _ <= t; ++_){
		int siz = -1;
		gets(ent);
		while(ent[++siz]){
			sai[siz] = conv[ent[siz]];
		}
		sai[siz] = 0;
		printf("Case #%d: %s\n", _, sai);
	}
	return 0;
}


