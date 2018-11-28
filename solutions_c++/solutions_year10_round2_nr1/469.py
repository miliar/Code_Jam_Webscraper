#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int t, n, m;
vector <vector <pair <string, int> > > v;

int mkdir(int n) {
	char _s[200];
	string s;
	int i, j, k, l;
	int cnt = 0;
	for (i = 0; i < n; i++) {
		scanf("%s", _s);
		j = k = 0;
		while (_s[j] != '\0') {
			s = "";
			for (j++; _s[j] != '/' && _s[j] != '\0'; j++)
				s += _s[j];
			for (l = 0; l < v[k].size(); l++)
				if (v[k][l].first == s) break;
			if (l == v[k].size()) {
				v[k].push_back(make_pair(s, v.size()));
				v.resize(v.size() + 1);
				cnt++;
			}
			k = v[k][l].second;
		}
	}
	return cnt;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int lt, i, j, k;
	scanf("%d", &t);
	for (lt = 1; lt <= t; lt++) {
		scanf("%d%d", &n, &m);
		v.clear();
		v.resize(1);
		mkdir(n);
		printf("Case #%d: %d\n", lt, mkdir(m));
	}
	return 0;
}