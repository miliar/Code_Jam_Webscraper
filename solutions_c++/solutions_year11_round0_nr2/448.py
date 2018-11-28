#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

#define re return
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size())
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
#define y0 y32479
#define y1 y95874
#define fill(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))
#define prev prev239
#define next next239
#define hash hash239
#define rank rank239

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long ll;
typedef double D;
typedef long double LD;

template<class T> T abs(T x) {return x > 0 ? x : -x;}

int n;
int m;

int matr1[26][26], matr2[26][26];

int mas[1000];

int check() {
	if (m < 2)
		re 1;
	int x = mas[m - 1];
	rep(i, m - 1)
	if (matr2[mas[i]][x])
		re 0;
	re 1;
}

void add(int x) {
	mas[m++] = x;
	int f = 0;
	while (m > 1) {
		int a = mas[m - 1];
		int b = mas[m - 2];
		if (matr1[a][b] != -1) {
			int c = matr1[a][b];
			f = 1;
			m--;
			mas[m - 1] = c;
			if (!check()) {
				m = 0;
				re;
			}
		}
		else
			break;
	}

	if (!f)
	if (!check()) {
		m = 0;
		re;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tc;
	cin >> tc;
	rep(tt, tc) {
		cout << "Case #" << tt + 1 << ": ";

		fill(matr1, -1);
		fill(matr2, 0);

		cin >> n;
		rep(i, n) {
			string s;
			cin >> s;
			int a = s[0] - 'A';
			int b = s[1] - 'A';
			int c = s[2] - 'A';
			matr1[a][b] = matr1[b][a] = c;
		}

		cin >> n;
		rep(i, n) {
			string s;
			cin >> s;
			int a = s[0] - 'A';
			int b = s[1] - 'A';
			matr2[a][b] = matr2[b][a] = 1;
		}

		m = 0;

		string s;
		cin >> n;
		cin >> s;

		rep(i, n)
		add(s[i] - 'A');

		cout << "[";
		rep(i, m) {
			cout << (char) (mas[i] + 'A');
			if (i < m - 1)
				cout << ", ";
		}
		cout << "]";
		cout << endl;
	}

	re 0;
}

