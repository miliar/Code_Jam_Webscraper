#include <iostream>
#include <string>
#include <cstring>

using namespace std;

char cc[256][256];
bool dd[256][256];
char res[256];
int cnt[256];

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    memset(cc, 0, sizeof(cc));
    memset(dd, false, sizeof(dd));
    memset(cnt, 0, sizeof(cnt));

    int c; cin >> c;
    for (int i = 0; i < c; i++) {
      string s; cin >> s;
      cc[s[0]][s[1]] = cc[s[1]][s[0]] = s[2];
    }

    int d; cin >> d;
    for (int i = 0; i < d; i++) {
      string s; cin >> s;
      dd[s[0]][s[1]] = dd[s[1]][s[0]] = true;
    }

    int n; cin >> n;
    string s; cin >> s;

    int size = 0;
    for (int i = 0; i < n; i++) {
      res[size++] = s[i];
      cnt[s[i]]++;

      bool combined = false;
      while (true) {
        if (size < 2) break;
        char a = res[size-1];
        char b = res[size-2];
        if (cc[a][b] != 0) {
          size -= 2;
          cnt[a]--; cnt[b]--;
          res[size++] = cc[a][b];
          cnt[cc[a][b]]++;
          combined = true;
          continue;
        }
        break;
      }

      if (!combined) {
        char a = res[size-1];
        for (int i = 0; i < size-1; i++) if (dd[a][res[i]]) {
          size = 0;
          break;
        }
      }
    }

    cout << "Case #" << tt << ": [";
    for (int i = 0; i < size; i++) {
      if (i > 0) cout << ", ";
      cout << res[i];
    }
    cout << "]" << endl;
  }

  return 0;
}

