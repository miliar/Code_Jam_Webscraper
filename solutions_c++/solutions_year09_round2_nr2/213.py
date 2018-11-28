#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main() {

  int M;
  scanf("%d\n", &M);
  for (int T = 1; T <= M; ++T) {
    string N;
    cin >> N;
    printf("Case #%d: ", T);    
    if (next_permutation(N.begin(),N.end())) {
      cout << N << endl;
    } else {
      int i = 0;
      while (N[i] == '0') ++i;
      cout << N[i];
      N[i] = '0';
      cout << N << endl;
    }
  }

  return 0;
}

