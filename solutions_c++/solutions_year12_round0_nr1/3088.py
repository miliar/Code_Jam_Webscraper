#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;

map <char, char> mapping;

int main(void) {
	int testnum;
	scanf("%d\n", &testnum);
	mapping[' '] = ' ';
	mapping['a'] = 'y';
	mapping['b'] = 'h';
	mapping['c'] = 'e';
	mapping['d'] = 's';
	mapping['e'] = 'o';
	mapping['f'] = 'c';
	mapping['g'] = 'v';
	mapping['h'] = 'x';
	mapping['i'] = 'd';
	mapping['j'] = 'u';
	mapping['k'] = 'i';
	mapping['l'] = 'g';
	mapping['m'] = 'l';
	mapping['n'] = 'b';
	mapping['o'] = 'k';
	mapping['p'] = 'r';
	mapping['q'] = 'z';
	mapping['r'] = 't';
	mapping['s'] = 'n';
	mapping['t'] = 'w';
	mapping['u'] = 'j';
	mapping['v'] = 'p';
	mapping['w'] = 'f';
	mapping['x'] = 'm';
	mapping['y'] = 'a';
	mapping['z'] = 'q';
	
	
	for (int testcase = 1; testcase <= testnum; testcase++) {
		char c;
		char ans[111];
		int idx = 0;
		
		while (true) {
			
			if (scanf("%c", &c) != 1 || c == '\n') {
				ans[idx] = 0;
				break;
			}
			ans[idx] = mapping[c];			
			idx++;
		}
			
		printf("Case #%d: %s\n", testcase, ans);
	}
	return 0;
}
