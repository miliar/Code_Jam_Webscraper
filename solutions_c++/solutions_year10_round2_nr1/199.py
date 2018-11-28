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

#define L 300

set < string > have[L];
set < string > need[L];
set < string >::iterator it;
int n, m;

void parse(string s, set < string > S [])
{
	string cur = "/";
	int len = 0;
	for (int i = 1; i < s.length(); ++i)
	{
		if (s[i] == '/') {
			S[len++].insert(s.substr(0, i));
		}
	}
	S[len++].insert(s);
}

int main () {
	int i, j, len, CAS;
	char s[1000];

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		scanf("%d%d", &n, &m);

		for (i = 0; i < L; ++i) {
			need[i].clear(); have[i].clear();
		}

		for (i = 0; i < n; ++i) {
			scanf("%s", s);
			parse(s, have);
		}

		for (i = 0; i < m; ++i) {
			scanf("%s", s);
			parse(s, need);
		}

		int res = 0;

		for (len = 0; len < L; ++len) {
			for (it = need[len].begin(); it != need[len].end(); ++it)
			{
				if (have[len].insert(*it).second) ++res;
			}
		}
		
		printf("Case #%d: %d\n", cas, res);
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}


