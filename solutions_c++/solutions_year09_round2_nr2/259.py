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

int main() {
	char buf[300];
	gets(buf);
	int T = atoi(buf);

	int i;

	REP(i,T) {
		gets(buf);
		string x = buf;
		if (x[x.length()-1] == '\n') {
			x.erase(x.end()-1);
		}

		if (!next_permutation(x.begin(), x.end())) {
			string bb = "0";
			x = bb + x;
			int j = 0;
			while (x[j] == '0')
				++j;
			swap(x[0], x[j]);
		}

		cout << "Case #" << i + 1 << ": " << x << endl;
	}
}
