#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int tab[51][51];
int newtab[51][51];

int dx[] = {0, 0, 1, 1};
int dy[] = {0, 1, 0, 1};
string S = "/\\/";

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int R, C; cin >> R >> C;
		memset(tab,0,sizeof(tab));
		memset(newtab,0,sizeof(newtab));
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				char ch; cin >> ch;
				if (ch == '#') { tab[i][j] = 1; newtab[i][j] = 1; }
			}
		}
		bool ok = true;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (newtab[i][j] == 1) {
					for (int k = 0; k < 4; k++) {
						int mx = i + dx[k];
						int my = j + dy[k];
						if (mx >= R || my >= C || tab[mx][my] != 1) {
							ok = false;
							break;
						}
					}
					// put
					for (int k = 0; k < 4; k++) {
						int mx = i + dx[k];
						int my = j + dy[k];
						if (k == 0 || k == 3) { newtab[mx][my] = 2;  }
						else { newtab[mx][my] = 3;  }
					}
				}
				if (!ok) break;
			}
			if (!ok) break;
		}
		cout << "Case #" << t << ":\n";
		if (!ok) { cout << "Impossible\n"; continue; }
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (newtab[i][j] == 0) cout << ".";
				else if (newtab[i][j] == 2) cout << "/";
				else cout << "\\";
			}
			cout << "\n";
		}
	}
	return 0;
}