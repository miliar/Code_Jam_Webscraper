#include <iostream>

using namespace std;

int T, C, D, N, nCase;
int m[3000], d[3000];
int c[30], a[111];

int main() {
  FILE *file = freopen("B-large.in", "r", stdin);
  FILE *file2 = freopen("B-large.out", "w", stdout);
  cin >> T;
  nCase = 1;
  while (T--) {
    for (int i = 0; i < 3000; i++) {
      m[i] = d[i] = 0;
    }
    for (int i = 0; i < 30; i++) {
      c[i] = 0;
    }
    cin >> C;
    for (int i = 0; i < C; i++) {
      char ch[10];
      cin >> ch;
      m[(ch[0] - 'A') * 100 + ch[1] - 'A'] = ch[2] - 'A';
      m[(ch[1] - 'A') * 100 + ch[0] - 'A'] = ch[2] - 'A';
    }
    cin >> D;
    for (int i = 0; i < D; i++) {
      char ch[10];
      cin >> ch;
      d[(ch[0] - 'A') * 100 + ch[1] - 'A'] = 1;
      d[(ch[1] - 'A') * 100 + ch[0] - 'A'] = 1;
    }
    cin >> N;
    char ch[110];
    int last = -1, length = 0;
    cin >> ch;
    for (int i = 0; i < N; i++) {
      if (last == -1) {
        int cur = ch[i] - 'A';
        a[length++] = cur;
        c[cur]++;
        last = cur;
      } else {
        int cur = ch[i] - 'A';
        if (m[last * 100 + cur] > 0) {
          a[length - 1] = m[last * 100 + cur];
          c[last]--;
          last = m[last * 100 + cur];
        } else {
          bool flag = false;
          for (int j = 0; j < 30; j++) {
            if (c[j] > 0) {
              if (d[j * 100 + cur] == 1) {
                flag = true;
                break;
              }
            }
          }
          if (flag) {
            length = 0;
            for (int j = 0; j < 30; j++) {
              c[j] = 0;
            }
            last = -1;
          } else {
            c[cur]++;
            last = cur;
            a[length++] = cur;
            last = cur;
          }
        }
      }
    }
    cout << "Case #" << nCase++ << ": [";
    for (int i = 0; i < length; i++) {
      if (i) {
        cout << ", ";
      }
      char oCh = 'A' + a[i];
      cout << oCh;
    }
    cout << "]" << endl;
  }
}
