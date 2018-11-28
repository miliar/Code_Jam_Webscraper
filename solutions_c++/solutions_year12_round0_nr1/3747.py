#pragma comment(linker, "/stack:167772960")

#include <iostream>
#include <cstdio>
#include <vector>
#include <deque>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <ctime>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define FORN(i, k, n) for(int i = (int)(k); i <= (int)(n); i++)
#define FORD(i, n, k) for(int i = (int)(n); i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define fi first
#define se second

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef pair<int, int> pii;

const long double pi = 3.1415926535897932384626433832795;
const long double eps = 0.0000000001;
const int INF = 1E9;
const int MAXN = 51000;

int n;
string s, s2, encode;
//char encode[26];

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	encode = "yhesocvxduiglbkrztnwjpfmaq";

	cin >> n;
	getline(cin, s);
	forn(i, n) {
		getline(cin, s);
		forn(j, s.size())
			if (s[j] != ' ') 
				s[j] = encode[s[j] - 'a'];
		cout << "Case #" << i + 1 << ": " << s << '\n';
	}

    return 0;
}