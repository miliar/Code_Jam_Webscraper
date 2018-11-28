#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int main() {

  int t;
  cin >> t;

  for (int cas = 0;cas < t;cas++) {

    vector<vector<char> > matChange(256,vector<char>(256,0));
    vector<vector<bool> > matDelete(256,vector<bool>(256,false));

    int changes;
    cin >> changes;

    for (int i=0;i<changes;i++) {
      string change;
      cin >> change;
      matChange[change[0]][change[1]] = change[2];
      matChange[change[1]][change[0]] = change[2];
    };

    int deletes;
    cin >> deletes;
    for (int i=0;i<deletes;i++) {
      string change;
      cin >> change;
      matDelete[change[0]][change[1]] = true;
      matDelete[change[1]][change[0]] = true;
    };

    int elements;
    cin >> elements;
    string total;
    cin >> total;

    list<char> res;
    vector<int> present(256,0);

    for (int i=0;i<elements;i++) {
      char cur = total[i];
      bool made = false;
      if (res.size()) {
        if (matChange[res.back()][cur]) {
          int val = matChange[res.back()][cur];
          present[res.back()]--;
          res.pop_back();
          res.push_back(val);
          present[val++]++;
          made = true;
        };
      };
      if (!made) {
        for (int j=0;j<256;j++) {
          if (present[j] && matDelete[j][cur]) {
            res.clear();
            made = true;
            for (int k=0;k<256;k++) {
              present[k] = 0;
            };
            break;
          };
        };
      };
      if (!made) {
        res.push_back(cur);
        present[cur]++;
      };
    };

    cout << "Case #" << cas+1 << ": [";

    while (res.size()) {
      int cur = res.front();
      res.pop_front();
      cout << (char) cur;
      if (res.size()) {
        cout << ", ";
      };
    };
    cout << "]" << endl;

  };

  return 0;

};
