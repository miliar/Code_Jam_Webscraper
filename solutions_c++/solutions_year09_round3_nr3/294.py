#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;

using std::map;

int main() {

  int N;

  cin >> N;
  cin.ignore();

  for (int i=0; i < N; ++i) {
    int P, Q;
    cin >> P;
    cin >> Q;
    cin.ignore();

    vector<int> releases(Q);

    for (int j=0; j < Q; ++j) {
      cin >> releases[j];
    }
    cin.ignore();

    vector<bool> cells(P+1, true);
    vector<bool> emptycells(P+1, true);
    int current;

    // calculate coins for first ordering;
    long coins = 0;
    for (int j=0; j < Q; ++j) {
      cells[releases[j]]=false;
      // bribe right side
      current = releases[j]+1;
      while (current <= P && cells[current] == true ) {
	coins++;
	current++;
      }
      // bribe right side
      current = releases[j]-1;
      while (current >= 1 && cells[current] == true ) {
	coins++;
	current--;
      }
    }
    long min_coins = coins;
    /*
    cout << "Releasing: ";
    for (int k = 0; k < Q; ++k)
      cout << releases[k] << " ";
    cout << "costs " << coins << endl;
    */
    while ( next_permutation(releases.begin(), releases.end()) ) {
      cells.assign(emptycells.begin(), emptycells.end());
      coins = 0;
      for (int j=0; j < Q; ++j) {
	cells[releases[j]]=false;
	// bribe right side
	current = releases[j]+1;
	while (current <= P && cells[current] == true ) {
	  coins++;
	  current++;
	}
	// bribe right side
	current = releases[j]-1;
	while (current >= 1 && cells[current] == true ) {
	  coins++;
	  current--;
	}
      }
      if ( coins < min_coins )
	min_coins = coins;
      /*
      cout << "Releasing: ";
      for (int k = 0; k < Q; ++k)
	cout << releases[k] << " ";
      cout << "costs " << coins << endl;
      */
    }

    cout << "Case #" << i+1 << ": " << min_coins << endl;

  }

  return 0;
}
