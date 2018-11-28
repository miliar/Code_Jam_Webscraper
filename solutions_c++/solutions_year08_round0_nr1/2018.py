#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n, m;
string list[100];
int mark[100];
string s;

int main() {
	int N; cin >> N;
	for (int M = 0; M < N; M++) {
		cin >> n;
		getline(cin, s);

		for (int i = 0; i < n; i++)
			getline(cin, list[i]);
		memset(mark, 0, sizeof(mark));
		cin >> m;
		getline(cin, s);

		int cc = 0;
		for (int j,i = 0; i < m; i++) {
			getline(cin, s);
			string *pos = find(list, list + n, s);
			if (pos) {
				int w = pos - list;
				mark[w] = 1;
				for (j = 0; j < n; j++)
					if (mark[j] == 0)
						break;
				if (j == n) {
					cc++;
					memset(mark, 0, sizeof(mark));
					mark[w] = 1;
				}
			}
		}
		cout << "Case #" << (M+1) << ": " << cc << endl;
		
	}
	return 0;
}