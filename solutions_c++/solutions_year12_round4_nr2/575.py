#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <cmath>
#include <ios>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <vector>
#include <utility>
#include <numeric>
#include <algorithm>

#define PRT(x) #x << ' ' << (x) << ' '
#define PRTPT(x,y) '(' << (x) << ',' << (y) << ')' << ' '
#define LNG(x) (sizeof(x)/sizeof(*(x)))
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int T;
int N;
int W, L;
int R[1000];
int Rorg[1000];
bool swpflg=false;

void solve()
{
  if(W < L) { swap(L, W); swpflg = true; }else{swpflg = false; }
  memcpy(Rorg, R, sizeof(R));
  sort(R, R+N);
  vector<pair<int, int> > res(N);
  int ypos=-R[N-1];
  int xpos=-R[N-1];
  int xwidth=R[N-1];
  for(int i=N-1; i >= 0; --i)
  {
    if(L < ypos + R[i])
    {
      xpos += 2*xwidth;
      xwidth = R[i];
      ypos = -R[i];
      assert(xpos + R[i] <= W);
    }
    if(swpflg) { res[i] = MP(ypos+R[i], xpos+xwidth); }
    else       { res[i] = MP(xpos+xwidth, ypos+R[i]); }
    ypos += 2*R[i];
  }
  // cerr << "\n";
  // for(int i=0; i < N; ++i)
  // {
  //   cerr << PRT(R[i]) << PRT(Rorg[i]) << ' ' << res[i].first << ' ' << res[i].second << "\n";
  // }
  for(int i=0; i < N; ++i)
  {
    auto X = equal_range(R, R+N, Rorg[i]);
    // cerr << " Found:(" << X.first - R << X.second - R << ") ";
    auto itr = X.first;
    for(; itr != X.second; ++itr)
    {
      const ssize_t si = itr - R;
      if(res[si].first != -1) {
        cout << ' ' << res[si].first << ' ' << res[si].second;
        res[si].first = res[si].second = -1;
        break;
      }
    }
    assert(itr != X.second);
  }
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(8);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cerr << X << "\n";
    cin >> N;
    cin >> W >> L;
    for(int i=0; i<N; ++i)
    {
      cin >> R[i];
    }
    cout << "Case #" << X << ": ";
    solve();
    cout << "\n";
  }
  return 0;
}
