#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int ctoi(char c) {
  return (1<< (c - 'a'));
}

vector<int> wtoa(string a) {
  vector<int> r(a.length());
  for(int i=0; i<a.length(); i++) {
    r[i] = ctoi(a[i]);
  }
  return r;
}


vector<int> ptoa(string p, int l) {
  vector<int> r(l, 0);
  int b = 0;
  for(int i=0; i<l; i++) {
    if (p[b] != '(') {
      r[i] = ctoi(p[b++]);
    } else {
      do {
        b++;
        if (p[b] == ')') {
          b++;
          break;
        } else {
          r[i] = ( r[i] | ctoi(p[b]) );
        }
      } while (true);
    }
  }
  return r;
}

int main() {


  int l, d, n;
  cin >> l >> d >> n;

  vector<vector<int> > w;
  for (int i=0; i<d; i++) {
    string word;
    while (word.length() == 0) {
      cin >> word;
    }
    w.push_back(wtoa(word));
  }
  sort(w.begin(), w.end());



  vector<int> p;
  for (int c=0; c<n; c++) {

    string pa;
    while (pa.length() == 0) {
      cin >> pa;
    }
    p = ptoa(pa, l);

    int cc = 0;
    for (int i=0; i<d; i++) {
      int ok = 1;
      for (int j=0; j<l; j++) {
        if ((p[j] & w[i][j]) == 0) {
          ok = 0;
          break;
        }
      }
      cc += ok;
    }
    cout << "Case #" << (c+1) << ": " << cc << endl;
  }

  return 0;
}
