#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int s, q, qry[1024], sol[1024][1024];


int solve () {
  map<string, int> m;
  string tmp;
  cin >> s;
  getline (cin, tmp);
  for (int i = 0; i < s; ++i) {
    getline (cin, tmp);
    m[tmp] = i+1;
  }
  cin >> q;
  getline (cin, tmp);
  for (int i = 0; i < q; ++i) {
    getline (cin, tmp);
    qry[i] = m[tmp]-1;
  }

  for (int i = 0; i < s; ++i) 
    sol[0][i] = 0;

  for (int j = 0; j < q; ++j) {
    for (int i = 0; i < s; ++i) {
      if (qry[j] == i) sol[j+1][i] = 1024;
      else {
	sol[j+1][i] = sol[j][i];
	for (int k = 0; k < s; ++k) if (k != i){
	  sol[j+1][i] <?= sol[j][k] + 1;
	}
      }
    }
  }

  int best = 1024;
  for (int i = 0; i < s; ++i) best <?= sol[q][i];
  return best;
}

int main () {
  int N; cin >> N;
  for (int i = 1; i <= N; ++i) {
    cout << "Case #" << i << ": " << solve () << endl;
  }
  return 0;
}

