#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;
#define REP(i,n) for(int _n=n, i=0;i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define PB push_back

int n, x, rst;

int main() {
  int Ts;
  cin>>Ts;
  FOR(cs, 1, Ts) {
    cin >> n;
    rst = 0;
    REP(i,n) {
      cin >> x;
      if (x != i + 1) rst++;
    }
    cout << "Case #" << cs << ": " << rst << endl;
  }
  return 0;
}
