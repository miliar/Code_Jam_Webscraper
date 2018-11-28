#include <iostream>
#include <vector>
#include <list>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;
typedef unsigned int uint;

int release_prisoner(int P, map<int, int> &used, int tbr) {
  int ccnt = 0;
  int tmp = tbr + 1;
  while ((tmp < P) && (used[tmp] > 0)) { ccnt++; tmp++; }
  tmp = tbr - 1;
  while ((tmp >= 0) && (used[tmp] > 0)) { ccnt++; tmp--; }
  used[tbr] = 0;
  //cout << P << " " << tbr << " " << ccnt << endl;
  return ccnt;
}

void solve_it(int ) {
  int P, Q;
  cin >> P >> Q;
  vector<int> cells(Q);
  for (int i=0; i<Q; i++) cin >> cells[i];
  //cout << P << " " << Q << " ";
  //for (int i=0; i<Q; i++) cout << cells[i];
  //cout << endl;
  vector<int> coins(P);
  int min_coins = -1;
  do {
    map<int, int> used;
    for (int i=0; i<P; i++) used[i] = 1;
    int cnt = 0;
    for (vector<int>::iterator it=cells.begin(); it!=cells.end(); it++)       
      cnt += release_prisoner(P, used, *it - 1);
    if ((min_coins < 0) || (cnt < min_coins)) min_coins = cnt;
    //cout << cnt << endl;
  }
  while (next_permutation(cells.begin(), cells.end()));
  cout << min_coins << endl;
}

int main() {
  int cases;
  cin >> cases;
  for (int i=1; i<=cases; i++) {
    cout << "Case #" << i << ": ";
    solve_it(i);
  }
}
