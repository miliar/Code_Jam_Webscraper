#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
using namespace  std;
int main()
{
	//FILE * fp_open, * fp_out;
	//fp_open = fopen("A-small-attempt0.in","r");
	freopen(".\\A-small-attempt1.in","r", stdin);
	freopen(".\\A-samll-attempt1.out", "w", stdout);
	//fp_out = fopen("A-small-attempt0.out","w");
	int h[300];
	h['a'] = 'y'; h['b'] = 'h';h['c'] = 'e'; h['d'] = 's';h['e'] = 'o'; h['f'] = 'c';
	h['g'] = 'v'; h['h'] = 'x';h['i'] = 'd'; h['j'] = 'u';h['k'] = 'i'; h['l'] = 'g';
	h['m'] = 'l'; h['n'] = 'b';h['o'] = 'k'; h['p'] = 'r';h['q'] = 'z'; h['r'] = 't';
	h['s'] = 'n'; h['t'] = 'w';h['u'] = 'j'; h['v'] = 'p';h['w'] = 'f'; h['x'] = 'm';
	h['y'] = 'a'; h['z'] = 'q';
	int t, n, casid = 0;
	char str[1000];
	scanf( "%d", &t);
	getchar();
	while(t--) {
		gets( str);
		for(int i = 0; str[i] != '\0';  ++i)
			if(str[i] >= 'a' && str[i] <= 'z')
				str[i] = h[str[i]];
		printf("Case #%d: %s\n", ++casid, str);
		//cout<<str<<endl;
	}
	
}