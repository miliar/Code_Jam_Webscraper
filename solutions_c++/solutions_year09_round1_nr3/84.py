#include <iostream>
#include <string>
using namespace std;

double choose(int n, int k) {
  double ans;
  if(n < k || k < 0) {
    return 0.0;
  } else {
    ans = 1.0;
    for(int i=1; i<=k; i++) {
      ans *= ((double) (n-k+i)) / ((double) i);
    }
    return ans;
  }
}

double probleft(int c, int n, int before, int after) {
  return choose(before, before-after) * choose(c-before, n-(before-after)) / choose(c,n);
}

int main(int argc, char *argv[]) {
  int T,C,N;
  double E[41];
  double p0;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> C >> N;
    E[0] = 0.0;
    for(int i = 1; i <= C; i++) {
      E[i] = 0.0;
      for(int j = 0; j < i; j++) {
        E[i] += probleft(C,N,i,j) * (1.0 + E[j]);
      }
      p0 = probleft(C,N,i,i);
      E[i] = (E[i] + p0) / (1-p0);
    }
    cout << "Case #" << t << ": " << E[C] << endl;
  }
  return 0;
}

