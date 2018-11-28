#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <ctype.h>
#include <string>

using namespace std;

#define pb pus_back
#define sz(v) ((int)v.size())

char mod[300];

void init() {
	mod['a'] = 'y';
	mod['b'] = 'h';
	mod['c'] = 'e';
	mod['d'] = 's';
	mod['e'] = 'o';
	mod['f'] = 'c';
	mod['g'] = 'v';
	mod['h'] = 'x';
	mod['i'] = 'd';
	mod['j'] = 'u';
	mod['k'] = 'i';
	mod['l'] = 'g';
	mod['m'] = 'l';
	mod['n'] = 'b';
	mod['o'] = 'k';
	mod['p'] = 'r';
	mod['q'] = 'z';
	mod['r'] = 't';
	mod['s'] = 'n';
	mod['t'] = 'w';
	mod['u'] = 'j';
	mod['v'] = 'p';
	mod['w'] = 'f';
	mod['x'] = 'm';
	mod['y'] = 'a';
	mod['z'] = 'q';
}

int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	init();
	int N;
	cin >> N;
	string st;
	getline(cin, st);
	for (int i = 0; i < N; ++i) {
		getline(cin, st);
		for (int j = 0; j < sz(st); ++j)
			if (isalpha(st[j]))
				st[j] = mod[st[j]];
		printf("Case #%d: %s\n",i + 1,st.c_str());
	}
	return 0;
}