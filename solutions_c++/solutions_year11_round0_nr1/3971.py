#include <iostream>
#include <vector>
#include <list>
using namespace std;


int main() {

  int t;
  cin >> t;

  for (int i=0;i<t;i++) {
    int n;
    cin >> n;
    list<int> ora;
    list<int> blu;
    vector<int> orablu(n);
    for (int j=0;j<n;j++) {
      string orbl;
      cin >> orbl;
      int pos;
      cin >> pos;
      if (orbl == "O") {
        ora.push_back(pos);
        orablu[j] = 1;
      } else {
        orablu[j] = 2;
        blu.push_back(pos);
      };
    };
    int a = 1;
    int k = 0;
    int b = 1;
    int x = 0;
    while (k < orablu.size()) {
      bool notpressed = true;
      if (ora.size()) {
        if ((a == ora.front()) && (orablu[k] == 1)) {
          k++;
          notpressed = false;
          ora.pop_front();
        } else {
          if (ora.front() > a) {
            a++;
          } else if (ora.front() < a) {
            a--;
          };
        };
      };
      if (blu.size()) {
        if (notpressed && (b == blu.front()) && (orablu[k] == 2)) {
          k++;
          blu.pop_front();
        } else {
          if (blu.front() > b) {
            b++;
          } else if (blu.front() < b) {
            b--;
          }
        };
      };
      x++;
    };

    cout << "Case #" << i+1 << ": " << x << endl;

  };

  return 0;

};
