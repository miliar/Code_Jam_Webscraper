#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<algorithm>
#include<functional>
#include<map>
#include<set>
#include<utility>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

using namespace std;

#define FOR(i,s,n) for (int i=(int)(s); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(), (c).end()
const int inf(1<<24);

int N, M, A;
bool V;

int main()
{
  int C;
  cin >> C;
  REP(i, C) {
    cin >> N >> M >> A;
    //cerr << "# " << N << " " << M << " " << A << endl;
    int ax1(-1),ax2,ay1,ay2;
    try {
      REP(x1, N+1) REP(y1, M+1) REP(x2, N+1) REP(y2, M+1) {
        if (abs(x1*y2 - x2*y1) == A) {
          ax1 = x1;
          ax2 = x2;
          ay1 = y1;
          ay2 = y2;
          throw 1;
        }
      }
    } catch (int e) {
      ;
    }

    cout << "Case #" << i+1 << ": ";
    if (ax1 < 0) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << 0 << " " << 0 << " "
           << ax1 << " " << ay1 << " "
           << ax2 << " " << ay2 << endl;
    }
  }
  return 0;
}
