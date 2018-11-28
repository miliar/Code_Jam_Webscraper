#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int casenum=1; casenum<=T; casenum++) {
    int K;
    cin >> K;

    vector<int> deck;
    deck.push_back(K);
    for (int k=K-1; k>0; k--) {
      vector<int> ndeck;
      ndeck.push_back(k);

      int n = (int)deck.size();
      int start = n - k;
      if (start < 0) {
	start += (-start / n) * n + n;
      }
      assert(start >= 0);
      start = start % n;

      for (int i=start; i<n; i++) {
	ndeck.push_back(deck[i]);
      }
      for (int i=0; i<start; i++) {
	ndeck.push_back(deck[i]);
      }

      deck = ndeck;
    }

    /*
    for (int i=0; i<(int)deck.size(); i++) {
      cout << deck[i] << " ";
    }
    cout << endl;
    */

    cout << "Case #" << casenum << ": ";

    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
      int d;
      cin >> d;
      cout << deck[d-1] << " ";
    }
    cout << endl;
  }
}
