#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

void solve()
{
	char combine[26][26];
	memset(combine, (char) -1, sizeof(combine));
	int C; cin >> C;
	for (int i = 0; i < C; i++) {
		char a, b, c;
		cin >> a >> b >> c;
		combine[a-'A'][b-'A'] = combine[b-'A'][a-'A'] = c - 'A';
	}

	vector <char> opposed[26];
	int D; cin >> D;
	for (int i = 0; i < D; i++) {
		char a, b;
		cin >> a >> b;
		opposed[a-'A'].push_back(b-'A');
		opposed[b-'A'].push_back(a-'A');
	}

	int N; cin >> N;
	int top = 0;
	int result[N];

	for (int i = 0; i < N; ++i) {
		char next; cin >> next; next -= 'A';
		result[top++] = next;

		char comb;
		while (top > 1 && (comb = combine[result[top-1]][result[top-2]]) >= 0) {
			result[top-2] = comb;
			top--;
		}

		if (top > 1) {
			bool exists[26];
			memset(exists, false, sizeof(exists));
			for (int j = 0; j < top; ++j)
				exists[result[j]] = true;

			vector <char> &view = opposed[result[top-1]];
			for (uint j = 0; j < view.size(); ++j) {
				if (exists[(int)view[j]]) {
					top = 0;
					break;
				}
			}
		}
	}

	cout << "[";
	for (int i = 0; i < top-1; i++)
		cout << (char) (result[i] + 'A') << ", ";
	if (top > 0)
		cout << (char) (result[top-1] + 'A');
	cout << "]" << endl;
}

int main()
{
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
