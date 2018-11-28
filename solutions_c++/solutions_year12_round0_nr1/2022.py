#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

char map[256];

int main()
{
    map[(int)'a'] = 'y';
map[(int)'b'] = 'h';
map[(int)'c'] = 'e';
map[(int)'d'] = 's';
map[(int)'e'] = 'o';
map[(int)'f'] = 'c';
map[(int)'g'] = 'v';
map[(int)'h'] = 'x';
map[(int)'i'] = 'd';
map[(int)'j'] = 'u';
map[(int)'k'] = 'i';
map[(int)'l'] = 'g';
map[(int)'m'] = 'l';
map[(int)'n'] = 'b';
map[(int)'o'] = 'k';
map[(int)'p'] = 'r';
map[(int)'r'] = 't';
map[(int)'s'] = 'n';
map[(int)'t'] = 'w';
map[(int)'u'] = 'j';
map[(int)'v'] = 'p';
map[(int)'w'] = 'f';
map[(int)'x'] = 'm';
map[(int)'y'] = 'a';
map[(int)'z'] = 'q';
map[(int)'q'] = 'z';

    int n; cin >> n;
    string s; getline(cin, s);
    for(int i=0;i<n;i++) {
	getline(cin, s);
	cout << "Case #" << i+1 << ": ";
	for(int j=0;j<s.size();j++) {
	    if(s[j] >= 'a' && s[j] <= 'z') {
		cout << map[s[j]];
	    } else {
		cout << s[j];
	    }
	}
	cout << endl;
    }
}
