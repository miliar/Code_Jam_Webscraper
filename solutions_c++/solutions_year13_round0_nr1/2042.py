#include <cstdio>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ctime>

#include <iostream>
#include <fstream>
#include <sstream>

#include <algorithm>
#include <utility>

#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <list>

using namespace std;

#define fi(i, n) for (int i = 0; i < (n); ++i)
#define fv(i, v) fi (i, (v).size())
#define fab(i, a, b) for (int i = (a); i <= (b); ++i)
#define fba(i, b, a) for (int i = (b); i >= (a); --i)

#define V vector
#define VI vector<int>
#define VS vector<string>
#define uint unsigned int
#define uchar unsigned char
#define LL long long
#define uLL unsigned LL

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz size()

uLL fact(int n, uLL mod) { return n ? n * fact(n - 1, mod) % mod : 1; }
uLL gcd(uLL a, uLL b) { return a ? gcd(b % a, b) : b; }
uLL qpow(uLL a, uLL b, uLL mod) { if (!b) return 1; if (b % 2) return a * qpow(a, b - 1, mod) % mod; else {uLL t = qpow(a, b / 2, mod); return t * t % mod; }}

char wins(char a, char b, char c, char d) {
	if (a == 'T' || b == 'T' || c == 'T' || d == 'T') {
		a = a == 'T' ? d : a;
		b = b == 'T' ? a : b;
		c = c == 'T' ? b : c;
		d = d == 'T' ? c : d;
	}
	return (a == b && b == c && c == d) ? a : '.';
}

void solve_the_problem() {
	const char c[10][4] = {
		{0 ,1 ,2, 3 },
		{4 ,5 ,6, 7 },
		{8 ,9 ,10,11},
		{12,13,14,15},
		{0 ,4 ,8, 12},
		{1 ,5 ,9, 13},
		{2 ,6 ,10,14},
		{3 ,7 ,11,15},
		{0 ,5 ,10,15},
		{3 ,6 , 9,12}
	};
	char a[17];
	fi(i, 4) {
		cin >> (a + 4 * i);
	}
	fi(i, 10) {
		char ch;
		if ( (ch = wins(a[c[i][0]], a[c[i][1]], a[c[i][2]], a[c[i][3]])) != '.' ) {
			cout << ch << " won";
			return;
		}
	}
	fi (i, 16) {
		if (a[i] == '.') {
			cout << "Game has not completed";
			return;
		}
	}
	cout << "Draw";
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	fab(i, 1, t) {
		cerr << "Test #" << i << ":" << endl;
		cout << "Case #" << i << ": ";
		solve_the_problem();
		cout << endl;
	}
	return 0;
}
