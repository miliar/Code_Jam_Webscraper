#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

typedef vector<int>	vi;
typedef vector<vi>	vvi;
typedef vector<string>	vs;
typedef stringstream	ss;
typedef long long	ll;
typedef pair<int, int>	ii;
typedef pair<double, double>	dd;
typedef pair<int, double>	id;
typedef pair<double, int>	di;
typedef	map<string, int>	dict;

#define sz(v)		((int)v.size())
#define	fn(n, i)	for (int i = 0; i < (n); ++i)
#define	fv(v, i)	for (int i = 0; i < sz(v); ++i)
#define pb(a)		push_back(a)
#define	all(v)		v.begin(), v.end()

char buff[2048];
int used[200];

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	dict eng;
	ss str;
	int S;
	cin >> S;
	cin.getline(buff, 2047);
	fn(S, test) {
		int ans = 0;
		int n, m;
		cin >> n;
		cin.getline(buff, 2047);
		fn (n, i) {
			cin.getline(buff, 2047);
			eng[buff] = i;
		}
		cin >> m;
		cin.getline(buff, 2047);
		int l = 0;
		memset(used, 0, sizeof(used));
		fn (m, i) {
			cin.getline(buff, 2047);
			int c = eng[buff];
			if (used[c] == 0) {
				used[c] = 1;
				++l;
				if (l == n) {
					ans++;
					l = 1;
					memset(used, 0, sizeof(used));
					used[c] = 1;
				}
			}
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
	}

	return 0;
}
