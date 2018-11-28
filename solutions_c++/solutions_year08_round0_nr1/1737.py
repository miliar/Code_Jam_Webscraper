#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cstdlib>

using namespace std;

int mini[10000][1000], prev[10000][1000];

int main(void)
{
	int n, s, q;
	map<string, int> table;
	vector<int> query;

	cin >> n;
	for(int i = 1; i <= n; ++i) {
		table.clear();
		cin >> s;
		cin.ignore(1024, '\n');
		for(int j = 0; j < s; ++j) {
			string name;
			getline(cin, name);
			table[name] = j;
		}
		query.clear();
		cin >> q;
		cin.ignore(1024, '\n');
		for(int j = 0; j < q; ++j) {
			string name;
			getline(cin, name);
			query.push_back(table[name]);
		}
		memset(mini, 0, sizeof(mini));
		memset(prev, 0, sizeof(prev));
		for(int k = 0; k < q; ++k) {
			for(int l = 0; l < s; ++l) {
				mini[k+1][l] = 100000000;
				for(int m = 0; m < s; ++m) {
					if(m == query[k]) continue;
					if(m == l && mini[k][m] < mini[k+1][l]) {
						mini[k+1][l] = mini[k][m];
						prev[k+1][l] = m;
					} else if(m != l && mini[k][m] + 1 < mini[k+1][l]) {
						mini[k+1][l] = mini[k][m] + 1;
						prev[k+1][l] = m;
					}
				}
			}
		}
		int res = 1000000000;
		for(int l = 0; l < s; ++l) {
			if(mini[q][l] < res) res = mini[q][l];
		}
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
