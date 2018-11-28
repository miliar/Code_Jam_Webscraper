//#pragma comment(linker, "/STACK:16777216")
#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define pb push_back
#define f first
#define s second
#define mp make_pair
#define y0 y32479
#define y1 y95874

typedef long long ll;
typedef long double ld;

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-9;
const int INF = (int)1e9;
const int N = (int)1e5 + 10;

int t, n = 4;
char a[5][5];

bool ok(int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < n;
}

bool full() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (a[i][j] == '.')
				return false;
	return true;
}

bool check(char c) {
	for (int i = 0; i < n; i++) {
		int kol1 = 0, kol2 = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] == c)
				kol1++;
			else if (a[i][j] == 'T')
				kol2++;
		if (kol1 == 3 && kol2 == 1) return true;
		if (kol1 == 4) return true;
	}
	for (int j = 0; j < n; j++) {
		int kol1 = 0, kol2 = 0;
		for (int i = 0; i < n; i++)
			if (a[i][j] == c)
				kol1++;
			else if (a[i][j] == 'T')
				kol2++;
		if (kol1 == 3 && kol2 == 1) return true;
		if (kol1 == 4) return true;
	}
	int kol1 = 0, kol2 = 0;
	for (int i = 0; i < n; i++)
		if (a[i][i] == c)
			kol1++;
		else if (a[i][i] == 'T')
			kol2++;
	if (kol1 == 3 && kol2 == 1) return true;
	if (kol1 == 4) return true;
	kol1 = 0;
	kol2 = 0;
	for (int i = 0; i < n; i++)
		if (a[i][n - i - 1] == c)
			kol1++;
		else if (a[i][n - i - 1] == 'T')
			kol2++;
	if (kol1 == 3 && kol2 == 1) return true;
	if (kol1 == 4) return true;
	return false;
}

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cout.flags(ios::fixed);
	cout.precision(2);
	ios_base::sync_with_stdio(0);
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> a[i][j];
		if (check('X'))
			cout << "Case #" << tt + 1 << ": X won\n";
		else if (check('O'))
			cout << "Case #" << tt + 1 << ": O won\n";
		else if (full())
			cout << "Case #" << tt + 1 << ": Draw\n";
		else
			cout << "Case #" << tt + 1 << ": Game has not completed\n";
	}
	return 0;
}


