#include <iostream>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <string>

#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x)

using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef string::iterator si;

typedef unsigned long long ull;
typedef long long ll;

//const long long inf = (1LL <<60) + 0x3c;
const int inf = (1 <<30) + 0x3c;

bool solve(int testcase) {
	int ret = 0;
	int S, Q;
	set<string> eng;

	char buf[2000];
	if(scanf("%d", &S) != 1)
		assert(false);
	fgets(buf, 2000, stdin);
	for(int i = 0; i < S; ++i) {
		fgets(buf, 2000, stdin);
		if(buf[strlen(buf)-1] == '\n')
			buf[strlen(buf)-1] = 0;
		eng.insert(buf);
	}

	set<string> cureng = eng;

	if(scanf("%d", &Q) != 1)
		assert(false);
	fgets(buf, 2000, stdin);
	for(int i = 0; i < Q; ++i) {
		char buf[2000];
		fgets(buf, 2000, stdin);
		if(buf[strlen(buf)-1] == '\n')
			buf[strlen(buf)-1] = 0;
		cureng.erase(buf);
		if(cureng.empty()) {
			++ret;
			cureng = eng;
			cureng.erase(buf);
		}
	}

	printf("Case #%d: %d\n", testcase + 1, ret);
	return true;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n && solve(i); ++i);
	return 0;
}
