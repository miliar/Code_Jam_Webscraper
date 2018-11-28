
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (i = 0; i < (int)(n); ++i)
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i, j;
	cin >> t;
	forn(i, t) {
		ll n;
		int pd, pg;
		cin >> n >> pd >> pg;

		cout << "Case #" << i + 1 << ": ";
		if (pg == 100 && pd != 100 || pg == 0 && pd != 0) {
			cout << "Broken" << endl;
			continue;
		}

		int ok = 0;
		int k = 1;
		for (j = 1; j <= n; ++j, ++k) {
			int d = j;
			if (pd*d % 100 == 0) {
				ok = 1;
				cout << "Possible";
				break;
			}
			if (k >= 300) break;
		}

		if (!ok)
			cout << "Broken";
		cout << endl;
	}

	return 0;
}