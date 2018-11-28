#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
  ifstream cin("B-large (2).in");
  ofstream cout("out.txt");
  int C, N, K, B, T;
  cin >> C;
  for(int c = 0; c < C; c++) {
    cin >> N >> K >> B >> T;
    vector<pair<int, int> > s (N);
    for(int i = 0; i < N; i++)
      cin >> s[i].first;
    for(int i = 0; i < N; i++)
      cin >> s[i].second;
    int swaps = 0;
    for(int need = 0; need < K; need++) {
      for(int i = N-need-1; i >= 0; i--) {
        if(B-s[i].first <= T*s[i].second) {
          swaps += N-need-1-i;
          s.erase(s.begin()+i);
          break;
        }
      }
    }

    cout << "Case #" << c+1 << ": ";
    if(s.size() != N-K)
      cout << "IMPOSSIBLE";
    else
      cout << swaps;
    cout << endl;
  }
}
