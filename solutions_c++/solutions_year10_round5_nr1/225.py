#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

const int MAXN  = 2000000;

bool P[MAXN];

void countPrime() {

  int N = MAXN / 2;

  REP(i,N + 1)
    P[i] = true;
  FOR(i,2,N)
    if (P[i]) {

      int a = 2 * i;
      while (a <= N) {
        P[a] = false;
        a += i;
      }
    }

}

bool isPrime(int k) {
  return P[k];
}

int power(int a, int k, int p) {
  if (k == 0)
    return 1;
  if (k % 2 == 0) {
    int res = power(a, k / 2, p);
    res = (res * res) % p;  
    return res;
  }
  else {

    int res = power(a, k - 1, p);
    res = (res * a) % p;
    return res;
  }
}

int rev(int a, int p) {
  int res =  power(a,p - 2, p);
  assert((res * a) % p == 1);
  return res;
}

int divide(int a, int b, int p) {

  while (a < 0)
    a += p;

  while (b < 0)
    b += p;

  return (a * rev(b,p)) % p;
}

bool check(const VI &V, int A, int B, int P) {
  REP(i,V.size() - 1) 
    if ((V[i] * A + B) % P != V[i + 1])
      return false;
  return true;
}

int main() {
  ios_base::sync_with_stdio(0);

  countPrime();

  //cout << isPrime(2) << endl;

  int T;

  cin >> T;

  REP(q,T) {

    int D, K;

    cin >> D >> K;

    cout << "Case #" << q + 1 << ": ";

    VI V(K);

    REP(i,K)
      cin >> V[i];

    if (K == 1) {
      cout << "I don't know.\n";
      continue;
    }

    if (V[0] == V[1]) {
      cout << V[0] << endl;
      continue;
    }

    int mx = -1;
    FORE(it,V)
      mx = max(*it,mx);
  

    if (K == 2) {
      cout << "I don't know.\n";
      continue;
    }

    set<int> R;

    FOR(i,max(2,mx + 1),pow(10, D)) 
      if (isPrime(i)) { //cout << i << endl;
  
        int A = divide(V[1] - V[2],V[0] - V[1], i);        
        int B = (V[1] - A * V[0]);
        while (B < 0)
          B += i;
        B = B % i;
        assert(A >= 0 && B >= 0);
        bool c = check(V, A, B, i);
        if (!c)
          continue;
        int res = (V.back() * A + B) % i;
        R.insert(res);
        if (R.size() > 1)
          break;
      }

    if (R.size() > 1) {
      cout << "I don't know.\n";
      continue;
    }

    int res = *R.begin();
    cout << res << endl;

  }

  return 0;
}
