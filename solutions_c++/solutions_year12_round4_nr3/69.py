#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;
const int nmax = 2000;
int N;
int x[nmax];
vi y[nmax];
int h[nmax];

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int i, j, j1;
		bool ch;

		cin >> N;
		for (i = 0; i < N - 1; i++) {
			cin >> x[i]; x[i]--;
		}

		cout << "Case #" << it << ":";
		
		for (i = 0; i < N - 1; i++) {
			for (j = i + 1; j < N - 1; j++) {
				if (j < x[i] && x[j] > x[i]) {
					cout << " Impossible";
					goto southpark;
				}
			}
		}

		for (i = 0; i < N - 1; i++) {
			y[x[i]].push_back(i);
		}
		
		h[N - 1] = 1E9;
		for (i = 0; ; i++) {
			ch = 0;

			for (j = N - 1; j >= 0; ) {
				if (y[j].size()) {
					ch = true;
					h[y[j][0]] = h[j] - i * (j - y[j][0]);
// 					cout << " h[" << y[j][0] << "]=" << h[y[j][0]];
					j1 = y[j][0];
					y[j].erase(y[j].begin());
					j = j1;
				} else {
					j--;
				}
			}
// 			cout << endl;
			
			if (!ch) break;
		}
		
		for (i = 0; i < N; i++) cout << ' ' << h[i];
southpark:
		cout << endl;
	}
	
	return 0;
}
