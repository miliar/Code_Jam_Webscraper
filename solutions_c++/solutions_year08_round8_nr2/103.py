#include <iostream>
#include <vector>
using namespace std;

vector<string> colors;
int index(string color) {
  for (int i=0; i<colors.size(); i++) {
    if (colors[i] == color) return i;
  }
  colors.push_back(color);
  return colors.size() - 1;
}

int main() {
  int cases;
  cin >> cases;
  for (int caseno=1; caseno<=cases; caseno++) {
    colors.clear();
    int n;
    cin >> n;
    vector<pair<int, pair<int, int> > > v;
    for (int i=0; i<n; i++) {
      string color;
      int a, b;
      cin >> color >> a >> b;
      int col = index(color);
      v.push_back(make_pair(col, make_pair(a,b)));
    }
    colors.push_back("1234567890123");
    v.push_back(make_pair(colors.size()-1, make_pair(-1, -1)));
    colors.push_back("1234567890124");
    v.push_back(make_pair(colors.size()-1, make_pair(-1, -1)));

    int m=colors.size();
    int best = -1;
    for (int i=0; i<m-2; i++) {
      for (int j=i+1; j<m-1; j++) {
        for (int k=j+1; k<m; k++) {
          vector<pair<int, int> > w;
          for (int h=0; h<v.size(); h++) {
            if (v[h].first == i 
              || v[h].first == j
              || v[h].first == k)
            {
              if (v[h].second.first > 0) {
                w.push_back(v[h].second);
              }
            }
          }
          sort(w.begin(), w.end());

          int curr = 0;
          int p = 0;
          int cnt = 0;
          while (p < w.size() && curr < 10000) {
            if (p >= w.size() || w[p].first > curr + 1) break;
            int maxp = -1, maxx = -1;
            while (p < w.size() && w[p].first <= curr + 1) {
              if (maxx == -1 || maxx < w[p].second) {
                maxp = p;
                maxx = w[p].second;
              }
              p++;
            }
            curr = maxx;
            cnt++;
          }
          if (curr >= 10000) {
            if (best == -1 || cnt < best) best = cnt;
          }
        }
      }
    }

    cout << "Case #" << caseno << ": ";
    if (best == -1) cout << "IMPOSSIBLE";
    else cout << best;
    cout << endl;
  }
}
