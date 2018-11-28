
#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>
using namespace std;

int
calculateBribes(vector<bool> prison, vector<int> releases)
{
	int minb = 1000000;
	do {
		for (int i = 0; i < prison.size(); i++) {
			prison[i] = true;
		}
		int nb = 0;
		for (vector<int>::iterator it = releases.begin(); it != releases.end(); ++it) {
			int p = *it;
			prison[p] = false;
			if (p + 1 < prison.size()) {
				for(int sp = p + 1; sp < prison.size() && prison[sp]; sp++) {
					nb += prison[sp];
				}
			}
			if (p > 1) {
				for(int bp = p - 1; bp > 0 && prison[bp]; bp--) {
					nb += prison[bp];
				}
			}
		}
		if (nb < minb)
			minb = nb;
	} while(next_permutation(releases.begin(), releases.end()));
	return minb;
}

int
main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int P, Q;
		cin >> P >> Q;
		vector<bool> prison(P + 1, true);
		vector<int> releases;
		for (int r = 0; r < Q; r++) {
			int rc; cin >> rc;
			releases.push_back(rc);
		}
		cout << "Case #" << i + 1 << ": " << calculateBribes(prison, releases) << endl;
		releases.clear();
	}
}
