#include<iostream>
#include<string>
using namespace std;

int n, k;
bool ok1, ok2;
string a[100];

bool check(char ch)
{
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= n; ++j) {
      if (i+k-1 <= n) {
        bool ok = true;
        for (int o = 0; o < k; ++o) 
          if (a[i+o][j] != ch) {ok = false; break;}
        if (ok) return true;
      }
      if (j+k-1 <= n) {
        bool ok = true;
        for (int o = 0; o < k; ++o)
          if (a[i][j+o] != ch) {ok = false; break;}
        if (ok) return true;
      }
      if ((i+k-1 <= n) && (j+k-1 <= n)) {
        bool ok = true;
        for (int o = 0; o < k; ++o)
          if (a[i+o][j+o] != ch) {ok = false; break;}
        if (ok) return true;
      }
      if ((i+k-1 <= n) && (j-k+1 >= 1)) {
        bool ok = true;
        for (int o = 0; o < k; ++o)
          if (a[i+o][j-o] != ch) {ok = false; break;}
        if (ok) return true;
      }
    }
  return false;
}

void work()
{
  for (int i = 1; i <= n; ++i) {
    int p = n;
    for (int j = n; j >= 1; --j)
      if (a[i][j] != '.') {
        if (j != p) {
          a[i][p] = a[i][j]; a[i][j] = '.';
        }
        --p;
      }
  }
  ok1 = check('B');
  ok2 = check('R');
}
      
int main()
{
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n >> k; getline(cin, a[1]);
    for (int j = 1; j <= n; ++j) {
      getline(cin, a[j]);
      for (int o = n; o >= 1; --o) a[j][o] = a[j][o-1];
    }
    work();
    cout << "Case #" << i << ": ";
    if (ok1 && ok2) cout << "Both" << endl;
    if (ok1 && !ok2) cout << "Blue" << endl;
    if (!ok1 && ok2) cout << "Red" << endl;
    if (!ok1 && !ok2) cout << "Neither" << endl;
  }
  return 0;
}
