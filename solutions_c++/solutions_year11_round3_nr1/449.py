#include <iostream>
#include <vector>
#include <string>

using namespace std;

int testcase;
int n, m;
vector<string> a;

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> n >> m;
    a.clear();
    for (int i = 0; i < n; ++i) {
      string temp;
      cin >> temp;
      a.push_back(temp);
    }

    for (int i = 0; i < n-1; ++i) {
      for (int j = 0; j < m-1; ++j) {
        if (a[i][j] == '#' && a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#') {
          a[i][j] = a[i+1][j+1] = '/';
          a[i][j+1] = a[i+1][j] = '\\';
        }
      }
    }

    int flag = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (a[i][j] == '#') {
          flag = 1;
          break;
        }
      }
    }
    cout << "Case #" << tn << ":" << endl;
    if (flag == 1) {
      cout << "Impossible" <<endl;
    } else {
      for (int i = 0 ; i < n ;i  ++ ) {
        cout << a[i] << endl;
      }
    }
  }
  return 0;
}
