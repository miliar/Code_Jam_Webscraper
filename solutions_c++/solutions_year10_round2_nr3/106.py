#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751



long long NB[512][512];
long long CNP[512][512];

long long Cnp(int n, int p) {
  if(n == 0 && p == 0) return 1;
  if(n < 0 || p < 0 || p > n) return 0;
  if(CNP[n][p] != -1) return CNP[n][p];
  return CNP[n][p] = (Cnp(n-1, p) + Cnp(n-1,p-1)) % 100003;
}

int main() {
  memset(NB, 0, sizeof(NB));
  memset(CNP, -1, sizeof(CNP));
  for(int N = 1; N <= 500; N++) NB[N][1] = 1;
  for(int N = 2; N <= 500; N++) {
    for(int T = 1; T < N; T++) 
      for(int T2 = 1; T2 < T; T2++) 
        NB[N][T] = (NB[N][T] + NB[T][T2] * Cnp(N - T - 1, T - T2 - 1)) % 100003;
  }

  long long SOL[512];
  memset(SOL, 0, sizeof(SOL));
  for(int N = 2; N <= 500; N++) for(int T = 1; T < N; T++) SOL[N] = (SOL[N] + NB[N][T]) % 100003;

  int T, N;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> N;
    cout << "Case #" << i << ": " << SOL[N] << endl;
  }
}
