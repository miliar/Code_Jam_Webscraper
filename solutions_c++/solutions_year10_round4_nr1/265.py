#include <iostream>
using namespace std;

string a[512], b[512], tmp;

bool check(int sz) {
  /* cout << "check" << endl;
  for(int i = 0; i < 2*sz-1; i++)
    cout << b[i] << endl; */

  for(int i = 0; i < 2*sz-1; i++) {
    int ct = 0;
    for(int j = 0; j < b[i].size(); j++) {
      if(b[i][j] == ' ') continue;
      if(b[i][j] != 'x' && b[i][b[i].size()-1-2*ct] != 'x' && b[i][j] != b[i][b[i].size()-1-2*ct])
        return false;
      if(b[i][j] != 'x' && b[2*sz-2-i][j] != 'x' && b[i][j] != b[2*sz-2-i][j])
        return false;
      ct++;
    }
  }

  // cout << "check ok" << endl;
  return true;
}

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    int n; cin >> n;
    getline(cin, tmp);
    for(int i = 0; i < 2*n-1; i++) {
      getline(cin, a[i]);
      // a[i] = string(n+min(i, 2*n-2-i), ' ');
      // for(int j = max(n-(i+1), (i+1)-n); j < n+min(i, 2*n-1-i); j+=2)
      //   a[i] = '0'+(rand() % 10);
    }

    int res;
    for(int mid = n; ; mid++) {
      for(int i = 0; i < 2*mid-1; i++) {
        b[i] = string(mid+min(i, 2*mid-2-i), ' ');
        for(int j = max(mid-(i+1), (i+1)-mid); j < mid+min(i, 2*mid-1-i); j+=2)
          b[i][j] = 'x';
        // cout << b[i] << endl;
      }

      bool ok = false;
      for(int i = 0; i+2*n-2 < 2*mid-1 && !ok; i++)
        for(int j = 0; j < b[i].size() && !ok; j++) {
          // if(b[i][j+n-1] == ' ') continue;

          for(int k = 0; k < 2*mid-1; k++)
            for(int l = 0; l < b[k].size(); l++)
              if(b[k][l] != ' ')
                b[k][l] = 'x';
          bool valid = true;
          for(int k = 0; k < 2*n-1 && valid; k++) {
            if(j + a[k].size() > b[i+k].size()) { valid = false; break; }
            for(int l = 0; l < a[k].size(); l++) {
              if(a[k][l] == ' ') continue;
              if(b[i+k][j+l] == ' ' && a[k][l] != ' ') { valid = false; break; }
              b[i+k][j+l] = a[k][l];
            }
          }
          if(!valid) continue;

          if(check(mid)) ok = true;
        }

      if(ok) { res = mid; break; }
    }

    printf("Case #%d: %d\n", c, res*res-n*n);
  }

  return 0;
}
