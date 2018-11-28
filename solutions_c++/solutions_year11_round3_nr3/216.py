#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

long long nod(long long a, long long b) {
  long long prelast = a;
  long long last = b;
  while(prelast % last) {
    long long tmp = last;
    last = prelast%last;
    prelast = tmp;
  }
  return last;
}

long long nok(long long a, long long b) {
  return (long long)(a*1.0*b/nod(a,b)+0.5);
}

int main() {
  ifstream cin("C-small-attempt0 (1).in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ":";
    cout << " ";
    int N,L,H;
    cin >> N >> L >> H;
    vector<int> F(N);
    for(int i = 0; i < N; i++)
      cin >> F[i];
    int res = 0;
    bool b = false;
    for(int i = L; i <= H; i++) {
      for(int j = 0; j < N; j++) {
        if((F[j]%i != 0) && (i%F[j] != 0)) {
          b = true;
          break;
        }
      }
      if(b)
        b = false;
      else {
        res = i;
        break;
      }
    }
    if(res == 0)
      cout << "NO";
    else
      cout << res;
    cout << endl;
  }
}
