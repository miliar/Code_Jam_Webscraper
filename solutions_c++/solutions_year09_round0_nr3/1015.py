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
#include <numeric>
#include <bitset>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define fi first
#define se second
#define re return
#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,n) for(int i = 0; i < n; i++)
#define sqr(x) ((x) * (x))

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

string str = "welcome to code jam";

char s[500];

int mod = 10000;

int table[600][30];

int getans(int p, int c) {
	if (c == 19)
		re 1;
	if (p == n)
		re 0;

	int &ans = table[p][c];
	if (ans != -1)
		re ans;
	ans = 0;	
	if (s[p] == str[c])
		ans = getans(p + 1, c + 1);
	ans += getans(p + 1, c);
	ans %= mod;
	re ans;
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int tc;
	cin >> tc;

	gets(s);
	rep(u, tc) {
		gets(s);
		n = strlen(s);
		memset(table, 255, sizeof(table));
		cout << "Case #" << u + 1 << ": ";
		printf("%04d", getans(0, 0));
		cout << endl;
	}

	return 0;	
}