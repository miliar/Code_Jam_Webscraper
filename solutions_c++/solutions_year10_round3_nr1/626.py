#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <list>
#include <stack>
#include <string>
#include <queue>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

int main()
{
  int T;
  cin >> T;
  REP(cs, T) {
    int N;
    cin >> N;
    vector<int> A(N), B(N);
    REP(i, N) cin >> A[i] >> B[i];

    int ans = 0;
    REP(i, N) {
      FOR(j, i+1, N) {
        if ((A[i] < A[j] && B[i] > B[j]) ||
            (A[i] > A[j] && B[i] < B[j])) {
          ans++;
        }
      }
    }
    cout << "Case #" << cs+1 << ": " << ans << endl;
  }
  
  return 0;
}


