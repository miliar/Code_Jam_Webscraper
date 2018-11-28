#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define PB push_back

typedef vector<char> Vc;
typedef vector<string> Vs;

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int combine;
    cin >> combine;
    Vs comb(combine);
    for (int i = 0; i < combine; ++i) cin >> comb[i];
    
    int opposed;
    cin >> opposed;
    Vs opos(opposed);
    for (int i = 0; i < opposed; ++i) cin >> opos[i];
    
    int n;
    string st;
    cin >> n >> st;
    
    Vc vect;
    
    for (int i = 0; i < n; ++i) {
      int s = vect.size();
      if (s == 0) vect.PB(st[i]);
      else {
        char com = '.';
        for (int j = 0; j < combine; ++j) {
          if ((comb[j][0] == st[i] and comb[j][1] == vect[s - 1]) or
              (comb[j][1] == st[i] and comb[j][0] == vect[s - 1])) {
            com = comb[j][2];
          }
        }
        if (com != '.') vect[s - 1] = com;
        else {
          bool ok = true;
          for (int j = 0; j < opposed; ++j) {
            for (int k = 0; k < s; ++k)
              if ((opos[j][0] == st[i] and opos[j][1] == vect[k]) or
                  (opos[j][1] == st[i] and opos[j][0] == vect[k])) {
                ok = false;
              }
          }
          if (ok) vect.PB(st[i]);
          else vect.clear();
        }
      }
    }
    
    int s = vect.size();
    cout << "Case #" << cas << ": [";
    for (int i = 0; i < s; ++i) {
      if (i > 0) cout << ", ";
      cout << vect[i];
    }
    cout << "]" << endl;
  }
}
