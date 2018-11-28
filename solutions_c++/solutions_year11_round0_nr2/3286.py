#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <string.h>

#define U(x) (x - 'A')
using namespace std;

int main() {
  int T; 
  cin >> T;
  for (int test = 1; test <= T; test++) {
    // Init logic
    int i, C, D, N;
    int com[100][100];
    bool op[100][100];
    int e[100], a[100], ac = 0;
    memset(com, 0, sizeof(com));
    memset(op, 0, sizeof(op));
    string t;

    // Input logic
    cin >> C;
    for (i = 0; i < C; i++) {
      cin >> t;
      com[t[0] - 'A'][t[1] - 'A'] = t[2];
      com[t[1] - 'A'][t[0] - 'A'] = t[2];
    }
    cin >> D;
    for (i = 0; i < D; i++) {
      cin >> t;
      op[t[0] - 'A'][t[1] - 'A'] = true;
      op[t[1] - 'A'][t[0] - 'A'] = true;
    }
    cin >> N;
    cin >> t;
    for (i = 0; i < N; i++) {
      e[i] = t[i] - 'A';
    }

    // Business logic
    for (i = 0; i < N; i++) {
      a[ac++] = e[i];
      //cout << "Handling element: " << (char)(e[i] + 'A') << endl;
      //cout << "AFTER APPEND: ";
      //for (int j = 0; j < ac; j++) {
        //cout << (char)(a[j] + 'A') << ", ";
      //}
      //cout << endl;
      if (ac > 1) {
        if (com[a[ac - 2]][a[ac - 1]]) {
          a[ac - 2] = U(com[a[ac - 2]][a[ac - 1]]);
          ac -= 1;
        }
      }
      //cout << "AFTER COMPOSE: ";
      //for (int j = 0; j < ac; j++) {
        //cout << (char)(a[j] + 'A') << ", ";
      //}
      //cout << endl;
      for (int j = 0; j < ac - 1; j++) {
        if (op[a[j]][a[ac - 1]]) {
          ac = 0;
          break;
        }
      }
      //cout << "AFTER OPPOSING: ";
      //for (int j = 0; j < ac; j++) {
        //cout << (char)(a[j] + 'A') << ", ";
      //}
      //cout << endl;
    }

    // Print logic
    cout << "Case #" << test << ": [";
    for (i = 0; i < ac; i++) {
      if (i > 0) {
        cout << ", ";
      }
      cout << (char)(a[i] + 'A');
    }
    cout << "]" << endl;
  }
  return 0;
}

