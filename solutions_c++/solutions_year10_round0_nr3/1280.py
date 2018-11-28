#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>

using namespace std;
int main() {
  long long T, R, k, N;
  long long q1[1000], q2[1000];
  int c = 1;
  cin>>T;
  while(c <= T) {
    long long euro = 0;
    cin >> R >> k >> N;
    for (int i=0; i<N; ++i) {
      cin >> q1[i];
    }
    for (int r = 0; r < R; ++r) {
      long long sum = 0;
      int ni = 0;
      for (int i=0; i < N && sum+q1[i] <= k; ++i) {
        ni = i;
        sum += q1[i];
      }

      euro += sum;

      for (int i=0; i < (N-(ni+1)); ++i) {
        q2[i] = q1[i+ni+1];
      }
      for (int i=0; i < ni+1; ++i) {
        q2[N-ni-1+i] = q1[i];
      }
      memcpy(q1, q2, sizeof(q1));
    }
    cout << "Case #" << c <<": " << euro;
    cout << endl;
    c++;
  }
}
