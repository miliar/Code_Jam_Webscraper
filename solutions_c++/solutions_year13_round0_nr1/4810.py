#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define Abs(x) ((x) >= 0 ? (x) : -(x))
#define Max(a, b) ((a) >= (b) ? (a) : (b))
#define Min(a, b) ((a) <= (b) ? (a) : (b))
#define Size(t) (int(t.size()))
#define Sqr(x) ((x) * (x))

using namespace std;

typedef long long LL;
typedef unsigned int UI;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef set <int> SI;
typedef set <LL> SLL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <VI> VVI;

const double ep = 1e-8;
const double pi = 3.141592654;
const int inf = 0x7fffffff;
const long long llinf = 0x7fffffffffffffffLL;

/*Template written by Mashimaru*/

int test, ti, tj;
char a[10][10];

bool check(char ch)
{
	for (int i = 1; i <= 4; i++) {
		bool all = true;
		for (int j = 1; j <= 4; j++)
			if (a[i][j] != ch && a[i][j] != 'T') {
				all = false;
				break;
			}
		if (all) return true;
	}
	for (int j = 1; j <= 4; j++) {
		bool all = true;
		for (int i = 1; i <= 4; i++)
			if (a[i][j] != ch && a[i][j] != 'T') {
				all = false;
				break;
			}
		if (all) return true;
	}
	bool all = true;
	for (int i = 1; i <= 4; i++)
		if (a[i][i] != ch && a[i][i] != 'T') {
			all = false;
			break;
		}
	if (all) return true;
	all = true;
	for (int i = 1; i <= 4; i++)
		if (a[i][5 - i] != ch && a[i][5 - i] != 'T') {
			all = false;
			break;
		}
	if (all) return true;
	return false;
}

bool finish()
{
	for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			if (a[i][j] == '.')
				return false;
	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &test);
	for (int numCase = 1; numCase <= test; numCase++) {
		for (int i = 1; i <= 4; i++) scanf("%s", a[i] + 1);
		bool X = check('X');
		bool O = check('O');
		if (!X && !O) {
			if (finish()) {
				printf("Case #%d: Draw\n", numCase);
			} else {
				printf("Case #%d: Game has not completed\n", numCase);
			}
		} else {
			printf("Case #%d: %c won\n", numCase, X ? 'X' : 'O');
		}
	}
	return 0;
}