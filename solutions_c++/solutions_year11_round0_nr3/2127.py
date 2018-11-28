#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		int S = 0;
		vector<int> bag;
		while (N--) {
			int candy;
			cin >> candy;
			bag.push_back(candy);
			S += candy;
		}
		sort(bag.begin(), bag.end());
		vector<int>::iterator it,it2;
		/*for (it = bag.begin(); it != bag.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;*/

		int xorSum = 0;
		int xorSum2 = 0;
		bool found = false;
		for (it = bag.begin(); it != bag.end(); it++) {
			xorSum = xorSum ^ (*it);

			it2=it;
			it2++;
			xorSum2 = 0;
			for (;it2!=bag.end();it2++) {
				xorSum2 = xorSum2 ^ (*it2);
			}

			if (xorSum2==xorSum) {
				found = true;
				break;
			}
		}

		cout << "Case #" << t << ": ";
		if (found) {
			cout << S-xorSum;
		} else {
			cout << "NO";
		}
		cout << endl;

	}
}
