#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

vector<string> parse(string& path)
{
	vector<string> res;
	path += "/";
	int len = path.size();
	string tmp = "/";
	for (int i = 1; i < len; i++) {
		if (path[i] == '/') res.push_back(tmp);
		tmp += path[i];
	}
	return res;
}
int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, m;
		char path[200];
		scanf("%d%d", &n, &m);

		map<string, int> dirs;
		for (int i = 0; i < n; i++) {
			scanf("%s", path);
			string p = path;
			vector<string> res = parse(p);
			for (int j = 0; j < res.size(); j++) dirs[res[j]] = 1;
		}
		int ans = 0;
		vector<string> needs;
		for (int i = 0; i < m; i++) {
			scanf("%s", path);
			needs.push_back(path);
		}
		sort(needs.begin(), needs.end());
		for (int i = 0; i < needs.size(); i++) {
			vector<string> res = parse(needs[i]);
			for (int j = 0; j < res.size(); j++) {
				if (dirs[res[j]] == 1) continue;
				dirs[res[j]] = 1;
				ans++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}