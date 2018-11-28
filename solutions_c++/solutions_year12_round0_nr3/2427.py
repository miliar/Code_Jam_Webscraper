#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T, cas;
  cin >> T;
  cas = 1;
  while (cas <= T) {
    int A, B, dig, sol;
    cin >> A >> B;
    sol = 0;
    int ndig = 0, pot = 1, aux = B;
    while (aux > 0) {
      ndig++;
      pot *= 10;
      aux /= 10;
    }
    pot /= 10;
    for (int i = B; i >= A; --i) {
      aux = i;
      vector<int> fet(ndig-1);
      for (int j = 1; j < ndig; ++j) {
        aux = aux/10 + (aux%10)*pot;
        fet[j-1] = aux;
        if (aux > i and aux <= B) {
          bool trobat = false;
          for (int k = 0; k < j-1 and not trobat; ++k) if (fet[k] == aux) trobat = true;
          if (not trobat) {
            sol++;
          }
        }
      }
    }
    cout << "Case #" << cas << ": " << sol << endl;
    ++cas;
  }
}