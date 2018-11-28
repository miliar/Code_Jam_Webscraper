#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

vector<string> splitParts(string s)
{
	vector<string> ret;
	int i = 1;
	while (i < (int) s.length() && s[i] != '/') i++;
	ret.push_back(s.substr(0, i));
	while (i < (int) s.length()) {
		i++;
		while (i < (int) s.length() && s[i] != '/') i++;
		ret.push_back(s.substr(0, i));
	}
	return ret;
}

bool cmpStrange(const string& a, const string& b)
{
	int numSlashesA = 0, numSlashesB = 0;
	for (int i = 0; i < (int) a.length(); i++) if (a[i] == '/') numSlashesA++;
	for (int i = 0; i < (int) b.length(); i++) if (b[i] == '/') numSlashesB++;
	if (numSlashesA != numSlashesB) return (numSlashesA < numSlashesB);
	return a < b;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int n, m;
		scanf("%d%d", &n, &m);
		set<string> have;
		for (int i = 0; i < n; i++) {
			char temp[1024];
			scanf("%s", temp);
			string s = temp;
			vector<string> vs = splitParts(s);
			for (int j = 0; j < (int) vs.size(); j++)
				have.insert(vs[j]);
		}
		//
		vector<string> need;
		for (int i = 0; i < m; i++) {
			char temp[1024];
			scanf("%s", temp);
			string s = temp;
			vector<string> vs = splitParts(s);
			for (int j = 0; j < (int) vs.size(); j++)
				need.push_back(vs[j]);
		}
		int ans = 0;
		sort(need.begin(), need.end(), cmpStrange);
		for (int i = 0; i < (int) need.size(); i++) {
			if (have.find(need[i]) != have.end()) continue;
			ans++;
			have.insert(need[i]);
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
