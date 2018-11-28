#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int searchN, queryN;
string searches[110];
string queries[1010];

int cache[1010][110];

int doit(int q, int s) {
	int &ans= cache[q][s];
	if (ans >= 0) return ans;

	if (q == queryN) return 0;

	if (queries[q] != searches[s]) ans = doit(q+1, s);
	else {
		ans = 1<<30;
		for(int s2 = 0; s2 < searchN; s2++) if (s2 != s) {
			ans <?= 1 + doit(q, s2);
		}
	}
	return ans;
}

int main() {
	int cases;
	cin >> cases;

	string line;
	getline(cin,line);
	for(int t=0; t<cases; t++) {
		cin >> searchN;
		getline(cin,line);

		for(int i=0; i<searchN; i++) {
			getline(cin,searches[i]);
		}

		cin >> queryN;
		getline(cin,line);

		for(int q=0; q<queryN; q++) {
			getline(cin, queries[q]);
		}

		int ans=1<<30;
		memset(cache,-1,sizeof(cache));
		for(int s=0; s<searchN; s++) ans <?= doit(0, s);

		cout << "Case #" << (t+1) << ": " << ans << endl;
	}

}
