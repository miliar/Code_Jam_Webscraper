#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>

using namespace std;

int main(){

	int T;
	cin >> T;
	
	map <char, char> mcc;
	mcc['a'] = 'y';
	mcc['b'] = 'h';
	mcc['c'] = 'e';
	mcc['d'] = 's';
	mcc['e'] = 'o';
	mcc['f'] = 'c';
	mcc['g'] = 'v';
	mcc['h'] = 'x';
	mcc['i'] = 'd';
	mcc['j'] = 'u';
	mcc['k'] = 'i';
	mcc['l'] = 'g';
	mcc['m'] = 'l';
	mcc['n'] = 'b';
	mcc['o'] = 'k';
	mcc['p'] = 'r';
	mcc['q'] = 'z';
	mcc['r'] = 't';
	mcc['s'] = 'n';
	mcc['t'] = 'w';
	mcc['u'] = 'j';
	mcc['v'] = 'p';
	mcc['w'] = 'f';
	mcc['x'] = 'm';
	mcc['y'] = 'a';
	mcc['z'] = 'q';
	mcc[' '] = ' ';
	
	string g;
	getline(cin,g);
	
	for (int i = 1 ; i <=T ; i++){
	
		string s = "";
		getline(cin,g);
		for (int j = 0 ; j < g.size(); j++){
			s += mcc[g[j]];
		}
	
		cout << "Case #" << i << ": " << s << endl;
	}
	return 0;
	
}
