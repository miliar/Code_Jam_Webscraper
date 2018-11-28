#include <string>
#include <vector>
#include <climits>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <deque>
#include <iostream>
#include <boost/foreach.hpp>
#include <cstdio>

using namespace std;

typedef map<char, char> mcc;
typedef pair<char, char> cc;

void fill_map(mcc & m) {
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z'; // tego nie ma!!!
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
}

void dupa(const mcc & m, int j) {
	string str;
	getline(cin, str);
	printf("Case #%d: ", j + 1);
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] >= 'a' && str[i] <= 'z') {
			printf("%c", m.at(str[i]));
		}else if(str[i] == ' '){
			printf(" ");
		}
	}
	printf("\n");
}

int main() {
	mcc m;
	fill_map(m);
	int z;
	scanf("%d\n", &z);
	for (int i = 0; i < z; ++i) {
		dupa(m, i);
	}
}
