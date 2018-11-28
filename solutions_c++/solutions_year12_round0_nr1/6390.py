#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define VI vector<int>
#define VVI vector<VI>
#define VB vector<bool>
#define VVB vector<VB>

int gcd(int a, int b) {
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

double f[26];
char c[260];
const int n = 26;

void prepare() {
	for(int i=0; i<n; i++) {
		c[i] = 'a'+i;
	}
	f['a'] = 0.08167; f['n'-'a'] = 0.06749;
	f['b'] = 0.01492; f['o'-'a'] = 0.07507;
	f['c'-'a'] = 0.02782; f['p'-'a'] = 0.01929;
	f['d'-'a'] = 0.04253; f['q'-'a'] = 0.00095;
	f['e'-'a'] = 0.12702; f['r'-'a'] = 0.05987;
	f['f'-'a'] = 0.02228; f['s'-'a'] = 0.06327;
	f['g'-'a'] = 0.02015; f['t'-'a'] = 0.09056;
	f['h'-'a'] = 0.06094; f['u'-'a'] = 0.02758;
	f['i'-'a'] = 0.06966; f['v'-'a'] = 0.00978;
	f['j'-'a'] = 0.00153; f['w'-'a'] = 0.02360;
	f['k'-'a'] = 0.00772; f['x'-'a'] = 0.00150;
	f['l'-'a'] = 0.04025; f['y'-'a'] = 0.01974;
	f['m'-'a'] = 0.02406; f['z'-'a'] = 0.00074;
	for(int i=0; i+1<n; i++)
		for(int j=i+1; j<n; j++)
			if (f[i] < f[j]) {
				swap(f[i], f[j]);
				swap(c[i], c[j]);
			}
}

vector<string> a;

int cnt[n];
char ch[n];
int p[n];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	prepare();
	int lines;
	cin >> lines;
	cin.ignore();
	for(int i=0; i<lines; i++) {
		string s;
		getline(cin, s);
		a.push_back(s);
	}


	c['a'] = 'y';
	c['b'] = 'h'; 
	c['c'] = 'e';
	c['d'] = 's';
	c['e'] = 'o';
	c['f'] = 'c';
	c['g'] = 'v';
	c['h'] = 'x';
	c['i'] = 'd';
	c['j'] = 'u';
	c['k'] = 'i';
	c['l'] = 'g';
	c['m'] = 'l';
	c['n'] = 'b';
	c['o'] = 'k';
	c['p'] = 'r';
	c['q'] = 'z'; //
	c['r'] = 't';
	c['s'] = 'n';
	c['t'] = 'w'; //
	c['u'] = 'j';
	c['v'] = 'p';
	c['w'] = 'f';
	c['x'] = 'm';
	c['y'] = 'a';
	c['z'] = 'q'; //
	
	for(int i=0; i<a.size(); i++) {
		cout << "Case #" << i+1 << ": ";
		for(int j=0; j<a[i].size(); j++) {
			if (a[i][j] != ' ') {
				cout << c[a[i][j]];
			} else {
				cout << ' ';
			}
		}
		cout << endl;
	}
	return 0;
}