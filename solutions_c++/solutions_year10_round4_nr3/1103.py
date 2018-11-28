#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int tests;
  cin >> tests;

  for (int test = 0; test < tests; ++test) {
    int r;
    cin >> r;
    vector<vector<int> > a(120, vector<int>(120));
    vector<pair<int, int> > bact;

    for (int i = 0; i < r; ++i) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;

      for (int x = x1; x <= x2; ++x)
        for (int y = y1; y <= y2; ++y) {
          a[y][x] = 1;          
        }
    }

    for (int i = 0; i < a.size(); ++i)
      for (int j = 0; j < a[i].size(); ++j)
        if (a[i][j])
          bact.push_back(make_pair(j, i));

    int result = 0;
    bool alive = false;

    do {
      alive = false;

      vector<vector<int> > b = a;
      vector<pair<int, int> > tmpBact;

      for (int k = 0; k < bact.size(); ++k)
        {
          int i = bact[k].second;
          int j = bact[k].first;

          if (a[i][j] == 1 && (a[i - 1][j] == 0 && a[i][j - 1] == 0))
          {
            b[i][j] = 0;
          } else
          if (a[i][j] == 1 && (a[i - 1][j] == 1 || a[i][j - 1] == 1)) 
          {
            b[i][j] = 1;
            tmpBact.push_back(make_pair(j, i));
          }

          if (a[i][j + 1] == 0 && a[i - 1][j + 1] == 1) 
          {
            b[i][j + 1] = 1;
            tmpBact.push_back(make_pair(j + 1, i));
          }
        }

      a = b;
      bact = tmpBact;
      ++result;
    } while (!bact.empty());

    printf("Case #%d: %d\n", test + 1, result);
  }

  return 0; 
}