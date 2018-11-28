#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cmath>
#include <sstream>

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define re return
#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,n) for(int i = 0; i < n; i++)
#define sqr(x) ((x) * (x))
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

using namespace std;

template<class T> T abs(T x) {re x > 0 ? x : -x;}

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;

int n;
int m;

string dict[5000];

int l, d;
string s;
int col;

string token[15];

void check() {
	col = 0;
	rep(i, l)
		sort(all(token[i]));
//	rep(i, l)
//		cout << token[i] << ' ';
//	cout << endl;
	rep(i, d) {
		int f = 1;
		rep(j, l)
			if (!binary_search(all(token[j]), dict[i][j])) {
				f = 0;
				break;
			}
		col += f;					
	}	
}	

void parse(string s, int p) {
	if (p == l) {
		check();
		re;
	}
		
	if (isalpha(s[0])) {
		token[p] = s.substr(0, 1);
		if (p < l - 1)
			parse(s.substr(1, sz(s) - 1), p + 1);
		else
			check();	
	}
	else {
		int c = 1;
		while (s[c] != ')')
			c++;
		token[p] = s.substr(1, c - 1);
		if (p < l - 1)
			parse(s.substr(c + 1, sz(s) - c - 1), p + 1);
		else
			check();
	}
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);


	cin >> l >> d >> n;

	rep(i, d)
		cin >> dict[i];

	sort(dict, dict + d);

	rep(i, n) {	
		cin >> s;
		col = 0;
		parse(s, 0);	
		cout << "Case #" << i + 1 << ": " << col << endl;
	}	

	return 0;	
}