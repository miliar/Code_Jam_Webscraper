#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int n, m;
map<string, int> chd[100000];
int top;

int main (int argc, char * const argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> n >> m;
		chd[0].clear();
		top = 0;
		for (int i = 0; i < n; i++) {
			string s;
			cin >> s;
			if (s.length() == 1) continue;
			s += '/';
			int pre = 0;
			string tmps = "";
			for (int j = 1; j < s.length(); j++) {
				if (s[j] != '/')
					tmps += s[j];
				else {
					if (chd[pre].count(tmps)) {
						pre = chd[pre][tmps];
						tmps = "";
					} else {
						top++;
						chd[top].clear();
						chd[pre][tmps] = top;
						pre = top;
						tmps = "";
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < m; i++) {
			string s;
			cin >> s;
			if (s.length() == 1) continue;
			s += '/';
			int pre = 0;
			string tmps = "";
			for (int j = 1; j < s.length(); j++) {
				if (s[j] != '/')
					tmps += s[j];
				else {
					if (chd[pre].count(tmps)) {
						pre = chd[pre][tmps];
						tmps = "";
					} else {
						ans++;
						top++;
						chd[top].clear();
						chd[pre][tmps] = top;
						pre = top;
						tmps = "";
					}
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
