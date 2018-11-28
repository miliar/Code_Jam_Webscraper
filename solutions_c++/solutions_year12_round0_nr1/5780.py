#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define ll long long

map<char, char> Map;

void init() {
	Map['y'] = 'a';
	Map['n'] = 'b';
	Map['f'] = 'c';
	Map['i'] = 'd';
	Map['c'] = 'e';
	Map['w'] = 'f';
	Map['l'] = 'g';
	Map['b'] = 'h';
	Map['k'] = 'i';
	Map['u'] = 'j';
	Map['o'] = 'k';
	Map['m'] = 'l';
	Map['x'] = 'm';
	Map['s'] = 'n';
	Map['e'] = 'o';
	Map['v'] = 'p';
	Map['z'] = 'q';
	Map['p'] = 'r';
	Map['d'] = 's';
	Map['r'] = 't';
	Map['j'] = 'u';
	Map['g'] = 'v';
	Map['t'] = 'w';
	Map['h'] = 'x';
	Map['a'] = 'y';
	Map['q'] = 'z';
}

int main() {    
	 freopen("A-small-attempt0.in", "r", stdin);
	 freopen("output.txt", "w", stdout);
	
	init();

	int t;
	cin >> t;
	char str[200];
	gets(str);

	for (int j = 1; j <= t; j++) {
		gets(str);

		int n = strlen(str);
		for (int i = 0; i < n; i++) {
			if (str[i] != ' ' && str[i] != '\n') {
				str[i] = Map[str[i]];
			}
		}

		printf("Case #%d: %s\n", j, str);
	}


    return 0;
}