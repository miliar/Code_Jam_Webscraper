#include <algorithm>
#include <iostream>
#include <map>
#include <stdio.h>
#include <numeric>
#include <set>
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

char org[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ' };
char mod[] = { 'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x',
		's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q', ' ' };
//qh
//bz
int main() {
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int T, count = 1;
	string str;
	cin >> T;
	getline(cin, str);
	while(T--) {
		getline(cin, str);
		string res;
		FOR(i, 0, sz(str)) {
			FOR(j, 0, 27) {
				if (str[i] == mod[j])
					res += org[j];
			}
		}
		cout << "Case #" << count++ << ": " << res << endl;
	}
	return 0;
}
