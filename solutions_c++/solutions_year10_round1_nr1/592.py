#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i < (n); i++)
#define forn(i,n) forsn(i,0,(n))
#define dforsn(i,s,n) for(int i=(n)-1;i>=(s);i--)
#define dforn(i,n) dforsn(i,0,(n))

typedef long long tint;

string lot(char c, int times) {
	string s;
	forn(i,times) s += c;
	return s;
}

void rotate(vector<string> &m) {
	int n = m.size();
	vector<string> m2;
	forn(y,n) {
		string line;
		forn(x,n) {
			if (m[y][x] == 'R') line += 'R';
			if (m[y][x] == 'B') line += 'B';
		}
		m2.push_back(lot('.', n-line.size()) + line);
	}
	m = m2;
}

bool valid(int n, int x, int y) {
	return (x >= 0) && (y >= 0) && (x < n) && (y < n);
}

bool winposition(vector<string> &m, int k, char c, int x, int y) {
	int n = m.size();
	int cv = 0, ch = 0, d1 = 0, d2 = 0;
	forn(i,k) {
		if (valid(n,x+i,y) && m[y][x+i] == c) ch++;
		if (valid(n,x,y+i) && m[y+i][x] == c) cv++;
		if (valid(n,x+i,y+i) && m[y+i][x+i] == c) d1++;
		if (valid(n,x-i,y+i) && m[y+i][x-i] == c) d2++;
	}
	return (cv == k) || (ch == k) || (d1 == k) || (d2 == k);
}

bool wins(vector<string> &m, char c, int k) {
	int n = m.size();
	forn(x,n) forn(y,n) if (winposition(m,k,c,x,y)) return true;
	return false;
}

int main() {
	tint T, n, k;
	cin >> T;
	forn(icase,T) {
		cin >> n >> k;
		vector<string> m;
		
		forn(i,n) {
			string line;
			cin >> line;
			m.push_back(line);
		}
		
		string sol;
		rotate(m);
		//forn(i,n) cout << m[i] << endl;
		bool r = wins(m, 'R', k), b = wins(m, 'B', k);
		if (r && b) sol = "Both";
		else if (r) sol = "Red";
		else if (b) sol = "Blue";
		else sol = "Neither";
		
		cout << "Case #" << (icase+1) << ": " << sol << endl;
	}
	return 0;
}
