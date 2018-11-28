#include <stdint.h>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;


vector<int> deck;
vector<int> indexes;
set<int> remaining;


int main()
{
	int T;
	cin >> T;
	for (int testCase=1; testCase<=T; ++testCase) {
		int K, n;
		cin >> K >> n;

		indexes.resize(n);
		for (int i=0; i<n; ++i) cin >> indexes[i];

		deck.assign(K, 0);
		remaining.erase(remaining.begin(), remaining.end());
		for (int i=0; i<K; ++i) remaining.insert(i);

		set<int>::iterator pos = remaining.begin(), nextpos;
		for (int i=1; i<=K; ++i) {
			for (int j=1; j<i; ++j) {
				++pos;
				if (pos == remaining.end()) pos = remaining.begin();
			}
			deck[*pos] = i;
			nextpos = pos; ++nextpos; if (nextpos == remaining.end()) nextpos = remaining.begin();
			remaining.erase(pos);
			pos = nextpos;
		}

		cout << "Case #" << testCase << ":";
		for (int i=0; i<n; ++i) cout << " " << deck[(indexes[i] - 1) % K];
		cout << endl;
	}
	return 0;
}
