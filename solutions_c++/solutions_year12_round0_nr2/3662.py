#include <iostream>
#include <cmath>
using namespace std;

int tot[100];
int be[100];
int pbe[100];

int main() {
  int T; cin >> T;
  for (int t=1;t<=T;t++) {
    int N,S,p; cin >> N >> S >> p;
    for (int i=0;i<N;i++) {
      cin >> tot[i];
      be[i] = ceil(tot[i] / 3.0);
      if (tot[i] % 3 == 1 || tot[i] == 0) {
        pbe[i] = be[i];
      } else {
        pbe[i] = be[i] + 1;
      }
      //cout << tot[i] << " : " << be[i] << " : " << pbe[i] << endl;
    }

    int cnt = 0;
    for (int i=0;i<N;i++) {
      if (be[i] >= p) { cnt++; }
      else if (pbe[i] >= p && S > 0) { S--; cnt++; }
    }
    cout << "Case #" << t << ": " << cnt << endl;
  }
}
