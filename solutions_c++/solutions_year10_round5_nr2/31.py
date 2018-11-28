#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
using namespace std;
 
int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
#define zmax(a,b) (((a)>(b))?(a):(b))
#define zmin(a,b) (((a)>(b))?(b):(a))
#define zabs(a) (((a)>=0)?(a):(-(a)))
#define iif(c,t,f) ((c)?(t):(f))
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

long long gcd(long long a, long long b) {
  return a ? gcd(b % a, a) : b;
}

long long A[100];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";

    long long L; cin >> L;
    int N; cin >> N;
    for(int i = 0; i < N; i++) {
      cin >> A[i];
    }
    long long g = A[0];
    for(int i = 1; i < N; i++) {
      g = gcd(g, A[i]);
    }
    if(L % g != 0) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    sort(A, A + N);
    reverse(A, A + N);
    vector<long long> v(1, 0);
    int cnt = 0;
    for(int i = 1; cnt < A[0] && v.size() < 1000000; i++) {
      long long x = 1000000000000000LL;
      for(int j = 0; j < N; j++) {
        if(A[j] <= i) {
          x = min(x, 1 + v[i - A[j]]);
        }
      }
      v.push_back(x);
      if(i >= A[0] && x == 1 + v[i - A[0]]) {
        cnt++;
      } else {
        cnt = 0;
      }
    }
    long long num = 0;
    if(L < v.size()) {
    } else {
      num = L - v.size() + 1;
      if(num % A[0]) num = num / A[0] + 1;
      else num = num / A[0];
    }
    if(v[L - A[0] * num] == 1000000000000000LL) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << num + v[L - A[0] * num] << endl;
    }
  }
  return 0;
}
