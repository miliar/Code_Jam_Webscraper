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

#define MOD 1000000007

long long B;

long long fact[80];
long long ncr[80][80];
long long memo[80][80][80][2];
long long memo2[80][80][3240];

long long xcount(int last, int amt, int sum) {
  if(sum >= 3240) return 0;
  if(sum < 0) return 0;
  if(last == B) return amt == 0 && sum == 0;

  long long& ref = memo2[last][amt][sum];
  if(ref != -1) return ref;
  ref = xcount(last + 1, amt - 1, sum - last) +
        xcount(last + 1, amt, sum);
  ref %= MOD;
  return ref;
}

long long mul(long long a, long long b) { return (a * b) % MOD; }

long long solve(int x, int amt, int car, bool zero, long long N) {
//cout << x << ", " << amt << ", " << car << ", " << zero << ", " << N << endl;
  if(car == N) return !zero;
  if(car > N) return 0;
  int dig = (N - car) % B;

  long long& ref = memo[x][amt][car][zero];
  if(ref != -1) return ref;

  ref = 0;
  for(int i = 0; i <= amt; i++) {
    for(int j = 0; j < amt; j++) {
      long long cnt = xcount(1, i, dig + j * B);
      if(cnt == 0) continue;
      if(dig + j * B > N) continue;
      int ncar = (dig + car + j * B) / B;
      if(zero) {
        ref += mul(mul(cnt, x ? mul(ncr[amt - 1][i - 1], fact[i]) : 1),
                    solve(x + 1, i, ncar, false, N / B));
      } else {
        ref += mul(mul(cnt, x ? mul(ncr[amt][i], fact[i]) : 1),
                    solve(x + 1, i, ncar, false, N / B));
      }
      if(i < amt) {
        if(zero) {
          ref += mul(mul(cnt, x ? mul(ncr[amt - 1][i], fact[i + 1]) : 1),
                      solve(x + 1, i + 1, ncar, true, N / B));
        } else {
          ref += mul(mul(cnt, x ? mul(ncr[amt][i + 1], fact[i + 1]) : 1),
                      solve(x + 1, i + 1, ncar, true, N / B));
        }
      }
      ref %= MOD;
    }
  }

  return ref;
}


int main() {
  for(int i = ncr[0][0] = 1; i < 80; i++) {
    for(int j = ncr[i][0] = ncr[i][i] = 1; j < i; j++) {
      ncr[i][j] = (ncr[i - 1][j - 1] + ncr[i - 1][j]) % MOD;
    }
  }
  for(int i = fact[0] = 1; i < 80; i++) {
    fact[i] = (fact[i - 1] * i) % MOD;
  }
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    long long N;
    cin >> N >> B;
    memset(memo, -1, sizeof(memo));
    memset(memo2, -1, sizeof(memo2));
    cout << "Case #" << t << ": " << solve(0, B, 0, false, N) << endl;
  }
  return 0;
}
