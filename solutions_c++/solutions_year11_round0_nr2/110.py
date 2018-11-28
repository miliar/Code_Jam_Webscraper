#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int main() {
	int T, k, a, i, j, app[30];
	char comb[30][30];
	bool opp[30][30];
	char x, y, z;
	vector<char> list;
	cin >> T;
	for(k=1;k<=T;k++) {
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		cin >> a;
		for(i=0;i<a;i++) {
			cin >> x >> y >> z;
			x -= 'A', y -= 'A';
			comb[x][y] = comb[y][x] = z;
		}
		cin >> a;
		for(i=0;i<a;i++) {
			cin >> x >> y;
			x -= 'A', y -= 'A';
			opp[x][y] = opp[y][x] = 1;
		}
		list.clear();
		memset(app, 0, sizeof(app));
		cin >> a;
		for(i=0;i<a;i++) {
			cin >> x;
			if (list.size()) {
				y = list[list.size()-1];
				if (z = comb[x-'A'][y-'A']) {
					list[list.size()-1] = z;
					app[y-'A']--;
					app[z-'A']++;
					continue;
				}
			}
			list.push_back(x);
			app[x-'A']++;
			for(j=0;j<30;j++) {
				if (app[j] && opp[x-'A'][j]) {
					list.clear();
					memset(app, 0, sizeof(app));
					break;
				}
			}
		}
		cout << "Case #" << k << ": [";
		for(i=0;i<list.size();i++) {
			cout << list[i];
			if (i < list.size()-1) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
