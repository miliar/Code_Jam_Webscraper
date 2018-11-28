//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second


#define N 10000

int l, d, n;

char s[10000];

string word[N];

int main () {
	int i, j, CAS;

	scanf("%d%d%d", &l, &d, &n);

	for (i = 0; i < d; ++i) {
		scanf("%s", s);
		word[i] = s;
	}

	for (int cas = 1; cas <= n; cas++) {

		scanf("%s", s);

		bool open = 0;
		int mask[100];

		mset(mask,0);

		for (i = 0, j = 0; s[i]; ++i) {
			if (s[i] == '(') {
				open = true;
			}
			else if (s[i] == ')') {
				open = false;
				++j;
			}
			else {
				mask[j] |= (1 << (s[i]-'a'));
				if (!open) {
					++j;
				}				
			}
		}

		int res = 0;

		for (i = 0; i < d; ++i) {
			for (j = 0; j < l; ++j) {
				if (! (mask[j] & (1<<(word[i][j]-'a')))) break;
			}
			if (j >= l) ++res;
		}
		
		printf("Case #%d: %d\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


