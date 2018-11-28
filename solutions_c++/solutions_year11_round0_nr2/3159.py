#include <iostream>
#include <string>

using namespace std;

#define DBG 0

void do_case(int t) {
  int c;
  cin >> c;
  char forming[256][256];
  memset(forming, 0, sizeof (forming));
  for (int i = 0; i < c; ++i) {
    unsigned char c1, c2, c3;
    cin >> c1 >> c2 >> c3;
    forming[c1][c2] = c3;
    forming[c2][c1] = c3;
  }
  if (DBG) {
    for (int i = 0; i < 256; ++i) {
      for (int j = 0; j < 256; ++j) {
        if (forming[i][j]) {
          cout << "forming " << char(i) << char(j) << " " << forming[i][j] << endl;
        }
      }
    }
  }
  int d;
  cin >> d;
  char opposed[256];
  memset(opposed, 0, sizeof (opposed));
  for (int i = 0; i < d; ++i) {
    char c1, c2;
    cin >> c1 >> c2;
    opposed[c1] = c2;
    opposed[c2] = c1;
  }
  if (DBG) {
    for (int i = 0; i < 256; ++i) {
      if (opposed[i]) {
        cout << "opposed: " << char(i) << opposed[i] << endl;
      }
    }
  }
  int n;
  cin >> n;
  string line;
  int chars[256];
  memset(chars, 0, sizeof (chars));
  for (int i = 0; i < n; ++i) {
    char c;
    cin >> c;
    if (!line.empty()) {
      char new_c = forming[*line.rbegin()][c];
      if (new_c) {
        --chars[*line.rbegin()];
        *line.rbegin() = new_c;
        ++chars[new_c];
        continue;
      } 
      if (chars[opposed[c]]) {
        line.clear();
        memset(chars, 0, sizeof (chars));
        continue;
      }
    }
    line.push_back(c);
    chars[c]++;
  }
  cout << "Case #" << t << ": [";
  if (!line.empty()) cout << line[0];
  for (int i = 1; i < line.size(); ++i) {
    cout << ", " << line[i];
  }
  cout << "]\n";
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    do_case(t);
  }

  return 0;
}
