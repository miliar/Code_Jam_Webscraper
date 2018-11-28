#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

#define MAXL 200

using namespace std;

char str[MAXL];
map<char, char> mapa;

void inic() {
	mapa.clear();
	mapa['a'] = 'y';
	mapa['b'] = 'h';
	mapa['c'] = 'e';
	mapa['d'] = 's';
	mapa['e'] = 'o';
	mapa['f'] = 'c';
	mapa['g'] = 'v';
	mapa['h'] = 'x';
	mapa['i'] = 'd';
	mapa['j'] = 'u';
	mapa['k'] = 'i';
	mapa['l'] = 'g';
	mapa['m'] = 'l';
	mapa['n'] = 'b';
	mapa['o'] = 'k';
	mapa['p'] = 'r';
	mapa['q'] = 'z';
	mapa['r'] = 't';
	mapa['s'] = 'n';
	mapa['t'] = 'w';
	mapa['u'] = 'j';
	mapa['v'] = 'p';
	mapa['x'] = 'm';
	mapa['y'] = 'a';
	mapa['z'] = 'q';
	mapa['w'] = 'f';
}

int main() {
	inic();
	int caso = 0, casos;
	scanf("%d", &casos);
	gets(str);
	for(int x = 0; x < casos; ++x) {
		gets(str);
		if(!str[0]) continue;
		for(int i = 0; str[i]; ++i)
			if(str[i] != ' ') str[i] = mapa[ str[i] ];
		printf("Case #%d: %s\n", ++caso, str);
		str[0] = '\0';
	}
	return 0;
}



