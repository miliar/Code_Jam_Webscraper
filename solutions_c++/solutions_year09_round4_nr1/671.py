#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int countInversions (vector<int> vec) {
  int num = 0;
  for (int i = 0; i < vec.size(); i++) {
    if (vec[i] > i) {
      for (int j = i + 1; j < vec.size(); j++) {
        if (vec[j] <= i) {
          //printf ("%d %d\n", i, j);
          for (int k = j - 1; k >= i; k--) {
            int temp = vec[k];
            vec[k] = vec[k+1];
            vec[k+1] = temp;
            num++;
          }
          break;
        }
      }
    }
  }
  return num;
}

int main () {
  int T;
  scanf ("%d", &T);
  
  for (int t = 1; t <= T; t++) {
    int N;
    scanf ("%d", &N);
    vector<int> numZeros  = vector<int> (N, 0);
    getchar();
    
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        char c = getchar();
        if (c == '1')
          numZeros[i] = j;
      }
      getchar();
    }
    
    printf ("Case #%d: %d\n", t, countInversions(numZeros));
  }
}
