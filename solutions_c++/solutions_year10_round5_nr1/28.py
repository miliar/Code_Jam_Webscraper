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

#define itype long long

bool isprime[1000000];
itype A[10];

pair<itype, itype> gcd(itype a, itype b) {
  pair<itype, itype> A(1, 0), B(0, 1);
  while(a) {
    itype m = b / a;
    B.first -= m * A.first;
    B.second -= m * A.second;
    b %= a;
    swap(a, b); swap(A, B);
  }
  return B;
}

int mod(itype x, itype p) {
  x %= p;
  if(x < 0) x += p;
  return x;
}

int inv(itype x, itype p) {
  return mod(gcd(x, p).first, p);
}

int main() {
  memset(isprime, 1, sizeof(isprime));
  isprime[0] = isprime[1] = false;
  for(int i = 2; i < 1000000; i++) {
    if(isprime[i]) for(int j = 2 * i; j < 1000000; j += i) {
      isprime[j] = false;
    }
  }
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int D, K;
    cin >> D >> K;
    for(int i = 0; i < K; i++) cin >> A[i];
    int mx = 1;
    for(int i = 0; i < D; i++) mx *= 10;
    itype start = A[0];
    for(int i = 1; i < K; i++) start = max(start, A[i]);

    int sol = -1;
    if(K == 1) {
      sol = -1;
    } else if(K >= 2 && A[K - 1] == A[K - 2]) {
      sol = A[K - 1];
    } else if(K == 2) {
      sol = -1;
    } else for(itype i = start + 1; sol != -2 && i < mx; i++) {
      if(!isprime[i]) continue;

      long long x = mod(A[0] - A[1], i);
      x *= inv(mod(A[1] - A[2], i), i);
      x = mod(x, i);
      long long b = mod(A[0] - A[1] * x, i);

      bool ok = true;
      for(int j = 3; j < K; j++) {
        long long v = A[j];
        v *= x;
        v += b;
        v = mod(v, i);
        if(v != A[j - 1]) ok = false;
      }
      if(!ok) continue;

      long long nxt = mod(A[K - 1] - b, i);
      nxt *= inv(x, i);
      nxt = mod(nxt, i);

      if(sol == -1 || nxt == sol) {
        sol = nxt;
      } else {
        sol = -2;
      }
    }
    
    cout << "Case #" << t << ": ";
    if(sol >= 0) {
      cout << sol << endl;
    } else {
      cout << "I don't know." << endl;
    }
  }
  return 0;
}
