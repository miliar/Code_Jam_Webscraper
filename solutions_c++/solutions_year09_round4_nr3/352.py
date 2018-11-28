#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>
#include <cstring>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define For(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,n) For(i,0,n)
#define re return
#define fi first
#define se second
#define y0 y47847892
#define y1 y47824262
#define fill(x, val) memset(x, val, sizeof(x))

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, k;
int m;

int mas[20][30];
int matr[40][40];

int bad(int i, int j) {
	int a = 0, b = 0;
	rep(t, k){
	if (mas[i][t] >= mas[j][t])
		a = 1;
	if (mas[i][t] <= mas[j][t])
		b = 1;
	}
	if (a && b)
		re 1;
	re 0;
}

int check(int m) {

	rep(i, n)
	rep(j, n)
	if (i != j)
	if (m & (1 << i))
		if (m & (1 << j))
			if (matr[i][j])
				re 0;

	re 1;
}

int cc[70000];

int table[70000];
int getans(int m) {
	if (m == 0)
		re 0;
	int &ans = table[m];
	if (ans != -1)
		re ans;
	ans = 100;
	//cout << "   m = " << m << endl;
	for (int i = m; i; i = ((i - 1) & m)) {
		//cout << "i = " << i << endl;
		if (cc[i])
			ans = min(ans, 1 + getans(m - i));
	}

	re ans;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tCount;
	cin >> tCount;
	rep(test, tCount) {
		cout << "Case #" << test + 1 << ":" << ' ';

		cin >> n >> k;
		rep(i, n) rep(j, k)
			cin >> mas[i][j];

		memset(matr, 0, sizeof(matr));

		rep(i, n) rep(j, n)
		if (bad(i, j))
			matr[i][j] = matr[j][i] = 1;


		if (0)
		rep(i, n) {
			rep(j, n)
				cout << matr[i][j] << ' ';
			cout << endl;
		}

		rep(i, (1 << n))
		cc[i] = check(i);

		memset(table, 255, sizeof(table));
		cout << getans((1 << n) - 1);

		cout << endl;
	}

	return 0;
}
