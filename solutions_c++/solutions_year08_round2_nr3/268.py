#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

void out(list<int> &l) {
	for(list<int>::iterator li = l.begin(); li != l.end(); ++li) {
		cerr << ' ' << *li;
	}
	cerr << endl;

}

int main(void)
{
	int T;
	cin >> T;
	for(int tt = 0; tt < T; ++tt) {
		int K, n, d;
		vector<int> index, res;

		cin >> K;
		cin >> n;
		for(int k = 0; k < n; ++k) {
			cin >> d;
			index.push_back(d);
		}

		list<int> deck;
		list<int>::iterator pos = deck.end();
		pos = deck.insert(pos, K);
//		out(deck);

		for(int k = K; k > 1; --k) {
			int kk = k;
			while(kk > 1) {
				if(pos != deck.begin()) --pos; else { pos = deck.end(); --pos; }
				--kk;
			}
			pos = deck.insert(pos, k-1);
//			out(deck);
		}

		copy(pos, deck.end(), back_inserter(res));
		copy(deck.begin(), pos, back_inserter(res));
		cout << "Case #" << tt+1 << ":";
		for(int i = 0; i < index.size(); ++i) {
			cout << ' ' << res[index[i]-1];
			
		}
		cout << endl;
	}

	return 0;
}
