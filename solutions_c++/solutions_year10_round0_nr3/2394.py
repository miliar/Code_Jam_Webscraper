#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>
#include <list>
#include <iterator>

using namespace std;

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

int main()
{
  int T;

  cin >> T;
  REP(cs, T) {
    int R, k, N;
    cin >> R >> k >> N;
    vector<int> group(N);
    REP(i, N) cin >> group[i];

    int euro = 0;
    int head = 0;
    REP(round, R) {
      int sum = 0;

      REP(i, N) {
        if (sum + group[(head + i) % N] <= k) {
          sum += group[(head + i) % N];
        } else {
          head = (head + i) % N;
          break;
        }
      }
      euro += sum;
    }
    
    cout << "Case #" << cs+1 << ": " << euro << endl;
  }
  
  return 0;
}

