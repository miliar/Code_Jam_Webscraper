#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdio.h>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>

using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define sz(v) (int) v.size()
#define mp make_pair
#define pb push_back

string int_to_str(int x) {
	string str;
	while (x > 0) {
		string lol;
		lol += (x % 10 + '0');
		str = lol + str;
		x /= 10;
	}
	return str;
}
bool ispair(string n, string m) {
	string temp;
	FOR(i, 1, sz(n)) {
		temp = n.substr(i) + n.substr(0, i);
		if (temp == m)
			return true;
	}
	return false;
}

int main() {
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("out2.out", "wt", stdout);
	int T, A, B, count = 1, res;
	cin >> T;
	while (T--) {
		res = 0;
		cin >> A >> B;
		FOR(i, A, B) {
			FOR(j, i + 1, B + 1) {
				if(ispair(int_to_str(i), int_to_str(j))) {
					res++;
					//cout << i << " " << j << endl;
				}
			}
		}
		cout << "Case #" << count++ << ": " << res << endl;
	}
	return 0;
}
