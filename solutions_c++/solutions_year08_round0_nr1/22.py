#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int N;
  cin >> N;
  string line;
  for (int c = 1; c <= N; c++) {
    int S, Q;
    cin >> S;
    getline(cin, line);
    map <string, int> ind;
    for (int s = 0; s < S; s++) {
      getline(cin, line);
      ind[line] = s;
    }
    vector <int> best(S);
    cin >> Q;
    getline(cin, line);
    for (int q = 0; q < Q; q++) {
      getline(cin, line);
      map<string,int>::iterator it = ind.find(line);
      if (it != ind.end()) {
	int qs = it->second;
	best[qs] = Q;
	for (int s = 0; s < S; s++)
	  best[qs] <?= best[s]+1;
      }
    }
    printf("Case #%d: %d\n", c, *min_element(best.begin(), best.end()));
  }
}
