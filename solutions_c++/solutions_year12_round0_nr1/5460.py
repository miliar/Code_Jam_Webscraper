#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <deque>
#include <set>
#include <map>
#include <time.h>
using namespace std;

//#define mp make_pair
#define pb push_back
#define ppb pop_back
const int INF = ~(1 << 31);
const double EPS = 1e-8;

map<char, char> mp;

void init(){
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
	mp[' '] = ' ';
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	/*freopen("f7.in", "r", stdin);
	freopen("f7.out", "w", stdout);*/
	int n;
	cin >> n;
	init();
	char ch = getchar();
	string s;
	for(int i = 1; i <= n; i++){
		getline(cin, s);
		cout << "Case #" << i << ": ";
		for(int j = 0; j < s.size(); j++) cout << mp[s[j]];
		cout << endl;
	}
	return 0;
}