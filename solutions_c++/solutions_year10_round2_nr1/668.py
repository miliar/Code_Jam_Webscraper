#include <iostream>
#include <cstdio>
#include <map>
#include <string>
using namespace std;

string created[101];
map<string, int> listed;
char str[150];
int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);
	int tn, curt;
	cin >> tn;
	for(curt = 1; curt <= tn; ++curt) {
		int n, m;
		cin >> n >> m;
		int i, j;
		string path;
		listed.clear();
		for(i = 0; i < n; ++i) {
			cin >> path;
			listed[path] = 1;
		}
		int ans = 0;

		for(i = 0; i < m; ++i){
			cin >> path;
			str[0] = path[0];
			for(j = 1; j < path.length(); ++j) {
				str[j] = path[j];
				if(path[j] == '/' || j == path.length() - 1) {
					str[j+1] = '\0';
					if (path[j] == '/') str[j] = '\0';
					string tstr(str);
					if(listed.find(tstr) == listed.end()) {
						ans++;
						listed[tstr] = 1;
					}
					if(path[j] == '/') str[j] = '/';
				}
			}
		}

		cout << "Case #" << curt << ": " << ans << endl;
	}
	return 0;
}