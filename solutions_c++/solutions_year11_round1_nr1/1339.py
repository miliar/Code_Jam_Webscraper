#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  int N, P, G;
  for (int i = 0; i < T; i++)  {
    cout << "Case #" << (i + 1) << ": ";
    cin >> N >> P >> G;

    if (N < 100) {
      // check if we can even construct integer
      bool can = false;
      for (int i = 1; i <= N; i++) {
        if ((i * P) % 100 == 0) {
          can = true;
          break;
        }
      }

      if (!can) {
        cout << "Broken" << endl;
        continue;
      }
    }

    if ((G == 100 && P != 100) || (G == 0 && P != 0)) {
      cout << "Broken" << endl;
      continue;
    }

    cout << "Possible" << endl;
  }
}


