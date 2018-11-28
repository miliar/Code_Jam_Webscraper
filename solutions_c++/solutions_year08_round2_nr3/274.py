#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(int argc, char **argv) {
	int numCases;
	cin >> numCases;

	for (int curCase = 0; curCase < numCases; curCase++) {
		vector<int> cards;
		vector<int> indices;
		int numIndices;
		int K;
		cin >> K;
		cin >> numIndices;

		cards.resize(K, 0);
		indices.resize(numIndices);
		for (int i = 0; i < numIndices; i++) {
			cin >> indices[i];
		}

		cards[0] = 1;
		int pos = 0;
		for (int k = 2; k <= K; k++) {
			for (int q = 0; q < k - 1; pos++) {
				if (pos == K) {
					pos = 0;
				}
				if (cards[pos] == 0) {
					q++;
				}
			}
			for (int n = 0; n < K; n++, pos++) {
				if (pos == K) {
					pos = 0;
				}
				if (cards[pos] == 0) {
					cards[pos] = k;
					break;
				}
			}
		}

		cout << "Case #" << curCase + 1 << ": ";
		for (int i = 0; i < numIndices; i++) {
			cout << " " << cards[indices[i] - 1];
		}
		cout << endl;
	}
}
