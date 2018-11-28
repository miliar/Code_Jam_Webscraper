#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

string w[10000], l[100];
short int bad[10000];
int n, m;

vector<int> pose(string x, char a) {
  vector<int> ans;
  int p = x.find(a);
  while (p != string::npos) {
    ans.push_back(p);
    p = x.find(a, p + 1);
  }
  return ans;
}

int fox(int wi, int li) {
  //cout << "Started fox with " << wi << " word, " << li << " list." << endl;
  int good = 0, ans = 0, ci = -1;
  for (int i = 0; i < n; i++) {
    if (w[i].length() == w[wi].length()) {
      good++;
    } else {
      bad[i] = 1;
    }
  }
  //cout << "Length elimination, there are " << good << " strings remain" << endl;
  while (good > 1) {
    ci++;
    while (ci < 26) {
      bool ok = false;
      for (int i = 0; i < n; i++) {
        if (!bad[i] && w[i].find(l[li][ci]) != string::npos) {
          ok = true;
          break;
        }
      }
      if (ok) break;
      ci++;
    }
    vector<int> gp = pose(w[wi], l[li][ci]);
    if (gp.empty()) {
      ans++;
    }
    for (int i = 0; i < n; i++) {
      if (i != wi && !bad[i] && gp != pose(w[i], l[li][ci])) {
        bad[i] = 1;
        good--;
      }
    }
    //cout << "Letter '" << l[li][ci] << "' elimination, there are " << good << " strings remain" << endl;
  }
  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      cin >> w[i];
    }
    for (int i = 0; i < m; i++) {
      cin >> l[i];
    }
    cout << "Case #" << test << ": ";
    for (int i = 0; i < m; i++) {
      if (i) cout << " ";
      memset(bad, 0, sizeof(bad));
      int sc = fox(0, i), si = 0;
      for (int j = 1; j < n; j++) {
        memset(bad, 0, sizeof(bad));
        int t = fox(j, i);
        if (t > sc) {
          sc = t;
          si = j;
        }
      }
      cout << w[si];
    }
    cout << endl;
  }
  return 0;
}

