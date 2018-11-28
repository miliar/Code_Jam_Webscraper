#include <iostream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

int minuts(string& s) {
  int t;
  t = 60*(10*(s[0] - '0') + s[1] - '0') + 10*(s[3] - '0') + s[4] - '0';
  return t;
}

int main() {
  int casos;
  cin >> casos;
  for (int k=0; k<casos; ++k) {
    cout << "Case #" << k+1 << ": ";
    int T, NA, NB;
    cin >> T >> NA >> NB;
    vector<pair<int, int> > v(2*(NA + NB));
    int i = -1;
    while (NA--) {
      string s;
      cin >> s;
      v[++i].first = minuts(s);
      v[i].second = 2;
      cin >> s;
      v[++i].first = minuts(s) + T;
      v[i].second = 0;
    }
    while (NB--) {
      string s;
      cin >> s;
      v[++i].first = minuts(s);
      v[i].second = 3;
      cin >> s;
      v[++i].first = minuts(s) + T;
      v[i].second = 1;
    }
    sort(v.begin(), v.end());
    int trensA, trensB, solA, solB;
    trensA = trensB = solA = solB = 0;
    for (i=0; i<v.size(); ++i) {
      if (v[i].second == 2) {
        if (trensA > 0) --trensA;
        else ++solA;
      }
      else if (v[i].second == 0)
        ++trensB;
      else if (v[i].second == 3) {
        if (trensB > 0) --trensB;
        else ++solB;
      }
      else if (v[i].second == 1)
        ++trensA;
    }
    cout << solA << ' ' << solB << endl;
  }
}
