#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <bitset>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}


const int nmax = 1000;

pair<pair<int, int>, int> a[nmax];
int n;

bool ls(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b){
	if (a.fs.fs * b.fs.sc != a.fs.sc * b.fs.fs)
		return a.fs.fs * b.fs.sc < a.fs.sc * b.fs.fs;
	return a.sc < b.sc;
}

void solve(){
	cin >> n;
	forn(i, n)
		cin >> a[i].fs.fs;
	forn(i, n)
		cin >> a[i].fs.sc;
	forn(i, n)
		a[i].sc = i;
	sort(a, a + n, ls);
	forn(i, n)
		cout << a[i].sc << " ";
	cout << endl;
}

int main ()
{
	freopen("input.txt", "rt", stdin);

	int n;
	cin >> n;
	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
