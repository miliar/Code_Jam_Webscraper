#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;


int main()
{
	map<char, char> alp;
	vector<char> a;

	string s, t;
/*	alp['y'] = 'a';
	alp['e'] = 'o';
	alp['q'] = 'z'; 
	alp['z'] = 'q';*/
/*	alp['a'] = 'y';
	alp['o'] = 'e';
	alp['z'] = 'q';*/
	alp['a'] = 'y';
	alp['b'] = 'h';
	alp['c'] = 'e';
	alp['d'] = 's';
	alp['e'] = 'o';
	alp['f'] = 'c';
	alp['g'] = 'v';
	alp['h'] = 'x';
	alp['i'] = 'd';
	alp['j'] = 'u';
	alp['k'] = 'i';
	alp['l'] = 'g';
	alp['m'] = 'l';
	alp['n'] = 'b';
	alp['o'] = 'k';
	alp['p'] = 'r';
	alp['q'] = 'z';
	alp['r'] = 't';
	alp['s'] = 'n';
	alp['t'] = 'w';
	alp['u'] = 'j';
	alp['v'] = 'p';
	alp['w'] = 'f';
	alp['x'] = 'm';
	alp['y'] = 'a';
	alp['z'] = 'q';
	alp[' '] = ' ';

	long long n, k;
	cin >> n;
	cin.sync();
	getline(cin, s);
	for(int i = 0; i < n; i++) {
		getline(cin, s);
		//cout << "!!" <<  s << endl;
		for(int st = 0; st < s.size(); st++)
			s[st] = alp[s[st]];
		cout << "Case #" << i + 1 << ": " << s << endl;
	}

	return 0;
}
