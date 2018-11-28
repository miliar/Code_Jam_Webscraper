#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cells[100];
int P, Q;

int use(int i) {
	cells[i - 1] = false;
	int j = i - 2;
	while (j >= 0 && cells[j])
		j--;
	int k = i;
	while (k < P && cells[k])
		k++;
	return ((i - 1) - j - 1) + (k - (i - 1) - 1);
}

int main() {
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C-small-attempt3.out", "w", stdout);
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> P >> Q;
		vector<int> qs;
		for (int j = 0; j < Q; j++) {
			int c;
			cin >> c;
			qs.push_back(c);
		}
		sort(qs.begin(), qs.end());
		int mintotal = 1000000000;
		do {
			memset(cells, true, P);
			int total = 0;
			for (int j = 0; j < qs.size(); j++)
				total += use(qs[j]);
			if (total < mintotal)
				mintotal = total;
		} while (next_permutation(qs.begin(), qs.end()) != 0);
		cout << "Case #" << i + 1 << ": " << mintotal << endl;
	}
}