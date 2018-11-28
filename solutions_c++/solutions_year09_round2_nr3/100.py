#include <iostream>
#include <queue>
#include <map>

using namespace std;

#define MAX 30

struct square {
	char type;
	int value;
	char sign;
};

struct expr {
	string e;
	int v;
	int r, c;
};

bool operator< (const expr & e1, const expr & e2) {
	if (e1.e.length() > e2.e.length()) return true;
	if (e1.e.length() == e2.e.length() && e1.e > e2.e) return true;
	return false;
}

void solve() {
	int w, q; cin >> w >> q;

	square sq[MAX][MAX];

	string dummy;
	getline(cin, dummy);

	for (int i = 0; i < w; i++) {
		string s;
		getline(cin, s);
		for (int j = 0; j < w; j++) {
			if (s[j] == '+' || s[j] == '-') {sq[i][j].type = 's'; sq[i][j].sign = s[j];}
			else {sq[i][j].type = 'd'; sq[i][j].value = s[j] - '0';}
		}	
	}

	for (int i = 0; i < q; i++) {
		int num;
		cin >> num;

		priority_queue<expr> q;

		for (int i = 0; i < w; i++) {
			for (int j = 0; j < w; j++) {
				if (sq[i][j].type == 'd') {
					expr e;
					e.e = '0' + sq[i][j].value;				
					e.v = sq[i][j].value;
					e.r = i; e.c = j;
					q.push(e);
				}
			}
		}
		
		map<pair<int, int>, bool> expanded;

		while (!q.empty()) {
			expr ce = q.top(); q.pop();

			if (ce.v == num) {cout << ce.e << endl; break;}

			if (expanded.find(make_pair(ce.r*w + ce.c, ce.v)) != expanded.end()) continue;
			expanded[make_pair(ce.r*w + ce.c, ce.v)] = true;

			for (int d1 = 0; d1 < 4; d1++) {
				for (int d2 = 0; d2 < 4; d2++) {
					int r1, r2, c1, c2;
					if (d1 == 0) {r1 = ce.r - 1; c1 = ce.c;}
					if (d1 == 1) {r1 = ce.r; c1 = ce.c + 1;}
					if (d1 == 2) {r1 = ce.r + 1; c1 = ce.c;}
					if (d1 == 3) {r1 = ce.r; c1 = ce.c - 1;}

					if (d2 == 0) {r2 = r1 - 1; c2 = c1;}
					if (d2 == 1) {r2 = r1; c2 = c1 + 1;}
					if (d2 == 2) {r2 = r1 + 1; c2 = c1;}
					if (d2 == 3) {r2 = r1; c2 = c1 - 1;}

					if (r1 < 0 || r2 < 0 || c1 < 0 || c2 < 0 || r1 >= w || r2 >= w || c1 >= w || c2 >= w) continue;

					expr e2; 
					e2.e = ce.e + sq[r1][c1].sign + (char)('0' + sq[r2][c2].value);
					e2.c = c2; e2.r = r2;
					if (sq[r1][c1].sign == '+') 
						e2.v = ce.v + sq[r2][c2].value; 
					else 
						e2.v = ce.v - sq[r2][c2].value; 
					q.push(e2);
//					cout << "C : " << ce.e << ' ' << ce.r << ' ' << ce.c << ' ' << endl;
//					cout << "E : " << e2.e << endl;
//					cout << "D : " << d1 << ' ' << d2 << endl;
				}
			}

		}

	}
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ":" << endl;
		solve();
	}
}
