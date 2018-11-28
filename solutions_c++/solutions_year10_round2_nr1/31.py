#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

vector<string> Parse(const string &s) {
	char buff[256];
	strcpy(buff, s.c_str());
	vector<string> res;
	for (char *curr = strtok(buff, "/"); curr; curr = strtok(0, "/")) res.push_back(curr);
	return res;
}

int n, m;
set<vector<string> > arr;
char buff[256];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		arr.clear();
		scanf("%d%d\n", &n, &m);
		for (int i = 0; i<n; i++) {
			gets(buff);
			arr.insert(Parse(string(buff)));
		}      

		int ans = 0;
		for (int i = 0; i<m; i++) {
			gets(buff);
			vector<string> d = Parse(string(buff));
			vector<string> t;
			for (int i = 0; i<d.size(); i++) {
				t.push_back(d[i]);
				if (arr.find(t) == arr.end()) {
					ans++;
					arr.insert(t);
				}
			}
		}

		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
