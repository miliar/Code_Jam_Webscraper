#include <iostream>

using namespace std;
int nextLoc[100000002];
unsigned long long rev[100000002];
int group[1001];

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		unsigned long long res = 0;
		int r, k, n;
		cin >> r >> k >> n;
		for (int j = 0; j < n; ++j) {
			cin >> group[j];
		}

		for (int j = 0; j < n; ++j) {
			nextLoc[j] = -1;
		}
		
		int curr = 0;
		for (int j = 0; j < r; ++j) {
			if (nextLoc[curr] == -1) {
				int old = curr;
				unsigned long long tot = 0; 
				bool flag = false;
				while (tot <= k) {
					if (curr > old+n-1) {
						flag = true;
						break;
					}
					tot += group[curr%n];
					++curr;
				}
				curr %= n;
				if (!flag) {
					if (curr == 0)
						curr = n-1;
					else
						curr--;
					nextLoc[old] = curr;
					rev[old] = tot - group[curr];
				}
				else {
					nextLoc[old] = curr % n;
					rev[old] = tot;
				}
				res += rev[old];
			}
			else {
				res += rev[curr];
				curr = nextLoc[curr];
			}
		}

		cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}

