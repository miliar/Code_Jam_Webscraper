#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

set<string> dirs;

int makedir(char* x) {
	int res = 0;
	if (x[strlen(x)-1] == '\n') {
		x[strlen(x)-1] = 0;
	}
	string a = x;

	int i;
	REP(i, a.length()) {
		if (a[i] == '/' && i != 0) {
			if (dirs.find(a.substr(0,i)) == dirs.end()) {
				++res;
				dirs.insert(a.substr(0,i));
			}
		}

		else if (i == a.length() - 1) {
			if (dirs.find(a.substr(0,i+1)) == dirs.end()) {
				++res;
				dirs.insert(a.substr(0,i+1));
			}
		}
	}

	return res;
}

void main() {
	char buf[200];
	int T,N,M;
	int i,j;

	gets(buf);
	sscanf(buf, "%d", &T);

	REP(i,T) {
		dirs.clear();
		gets(buf);
		sscanf(buf, "%d %d", &N, &M);

		REP(j, N) {
			gets(buf);
			makedir(buf);
		}

		int res = 0;
		REP(j,M) {
			gets(buf);
			res += makedir(buf);
		}

		cout << "Case #" << (i+1) << ": " << res << endl;

	}

}