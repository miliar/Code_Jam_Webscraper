// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <set>
#include <cstring>
using namespace std;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;

ifstream inp("A.in");
ofstream out("A.out");

int L, D, N;
string a[5002];

int get_count(string &s) {
	// parse it first
	bool valid[20][256];
	memset(valid, false, sizeof(valid));

	int idx = 0, len = s.size(), cur = 0, ret = 0;
	do {
		if (s[idx] == '(') {
			int nx = s.find(')', idx + 1);
			if (nx == string::npos) {
				cerr << "invalid s:" << s << endl;
				exit(-1);
			}
			for (int ii = idx; ii < nx; ii++) {
				valid[cur][s[ii]] = 1;
			}
			idx = nx + 1;
			cur++;
		} else {
			valid[cur][s[idx]] = 1;
			idx++;
			cur++;
		}
	} while (idx < len);

	for (int i = 0; i < D; i++) {
		int flag = 1;
		for (int j = 0; j < L; j++) {
			if (!valid[j][a[i][j]]) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			ret++;
		}
	}

	return ret;
}

int main()
{
	inp >> L >> D >> N;
	for (int i = 0; i < D; i++) {
		inp >> a[i];
	}
	for (int i = 0; i < N; i++) {
		string p;
		inp >> p;
		//deb(p);
		int ans = get_count(p);
		out << "Case #" << (i + 1) << ": " << ans << endl;
	}

	inp.close();
	out.close();
	return 0;
}
