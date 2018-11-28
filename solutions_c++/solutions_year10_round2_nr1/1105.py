#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, t, T;
map<string, set<string> > M;

vector<string> split(string s) {
	int len = s.size();
	string t = string("");
	vector<string> res;
	for (int i = 0; i < len; i++) {
		if (s[i] == "/"[0]) {
			if (t.size() > 0) {
				res.push_back(t);
			}
			t = "";
		} else {
			t += s[i];
		}
	}
	if (t.size() > 0) {
		res.push_back(t);
	}
	return res;
}

char s[500];

int main(void) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int i, j, k;
	string cur;
	vector<string> v;
	
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d", &n, &m);
		M.clear();
		for (i = 0; i < n; i++) {
			scanf("%s", s);
			v = split(s);
			cur = string("/");
			for (j = 0; j < v.size(); j++) {
				M[cur].insert(v[j]);
				cur += v[j];
			}
		}
		
		cur = "/";
		int sol = 0;
		for (i = 0; i < m; i++) {
			scanf("%s", s);
			v = split(s);
			cur = string("/");
			for (j = 0; j < v.size(); j++) {
				if (!M[cur].count(v[j])) {
					M[cur].insert(v[j]);
					sol++;
				}
				
				cur += v[j];
			}
		}
		
		printf("Case #%d: %d\n", t, sol);
	}
	
	exit(0);
}