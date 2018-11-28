#include <iostream>
#include <map>
#include <vector>
using namespace std;

int a[1010], N;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> a[i];
    sort(a, a+N);

    map<int, vector<int> > s;
    for (int i = 0; i < N; i++) {
      if (s[a[i]-1].size() == 0)
        s[a[i]].push_back(1);
      else {
        int p = N+1, pj = 0;
        for (int j = 0; j < s[a[i]-1].size(); j++)
          if (s[a[i]-1][j] < p) {
            p = s[a[i]-1][j];
            pj = j;
          }
        s[a[i]-1].erase(s[a[i]-1].begin() + pj);
        s[a[i]].push_back(p+1);
      }
    }

    int res = N+1;
    for (map<int, vector<int> >::iterator it = s.begin(); it != s.end(); ++it)
      for (int i = 0; i < it->second.size(); i++)
        res = min(res, it->second[i]);
    cout << "Case #" << c << ": " << (res == N+1 ? 0 : res) << endl;
  }
  return 0;
}
