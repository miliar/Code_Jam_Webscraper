#include <algorithm>
#include <cstdio>
#include <iostream>
#include <limits.h>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>

using namespace std;

#define ALL(a)  (a).begin(),(a).end()
#define REP(i, n) for(int i=0; i<(int)(n); i++)
#define FOR(i, s, e) for (int i = (int)(s); i < (int)(e); i++)
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).	end();itr++)
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define INF 999999999
#define ABS(x) ((x) < 0 ? - (x) : (x))
#define SIZE(buff) (sizeof(buff)/sizeof(buff[0]))
#define SORT(c) sort((c).begin(),(c).end())
#define PB push_back
#define MP make_pair
#define DISP(x) cout << #x << " : " << x << endl

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long int LL;

const double PI = acos(-1.0);

char combine[26][26];
bool opposed[26][26];
char tmp[16];
char magic[128];
bool emerge[26];
string base = "QWERASDF";

bool isOppose(stack<char> stk) {
	bool hasBase[8] = {0};

	while (!stk.empty()) {
		char t = stk.top();
		int pos = -1;

		REP(i, 8)
			if (base[i] == t)
				pos = i;
		if (~pos)
			hasBase[pos] = 1;

		stk.pop();
	}

	REP(i, 8) REP(j, 8) {
		if (!hasBase[i] || !hasBase[j])
			continue;
		if (opposed[base[i]-'A'][base[j]-'A'])
			return true;
	}

	return false;
}


int main() {
	freopen("C:/Users/kenji/Desktop/B-large.in", "r", stdin);
	freopen("C:/Users/kenji/Desktop/B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);

	REP(i, t) {
		int c, d, n;

		memset(combine, 0x00, sizeof(combine));
		memset(opposed, 0x00, sizeof(opposed));

		// read combine
		scanf("%d", &c);
		REP(j, c) {
			scanf("%s", tmp);
			combine[tmp[0]-'A'][tmp[1]-'A'] = tmp[2];
			combine[tmp[1]-'A'][tmp[0]-'A'] = tmp[2];
		}
		// read opposed
		scanf("%d", &d);
		REP(j, d) {
			scanf("%s", tmp);
			opposed[tmp[0]-'A'][tmp[1]-'A'] = 1;
			opposed[tmp[1]-'A'][tmp[0]-'A'] = 1;
		}
		// read magic list
		scanf("%d", &n);
		scanf("%s", magic);

		// solve
		stack<char> ret;
		REP(j, n) {
			if (ret.empty()) {
				ret.push(magic[j]);
				continue;
			}

			int pre = ret.top()-'A';
			int next = magic[j]-'A';

			if (combine[pre][next]) {
				ret.pop();
				ret.push(combine[pre][next]);
			}
			else {
				ret.push(magic[j]);
				if (isOppose(ret)) {
					while (!ret.empty())
						ret.pop();
				}
			}
		}

		// print
		string res = "]";
		while (!ret.empty()) {
			res = ret.top() + res;
			ret.pop();
			if (!ret.empty())
				res = ", " + res;
		}
		res = "[" + res;
		printf("Case #%d: %s\n", i+1, res.c_str());
	}

	fflush(stdout);
	cerr << "Done!" << endl;

	return 0;
}
