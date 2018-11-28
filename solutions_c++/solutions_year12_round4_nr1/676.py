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
int d[10000];
int l[10000];
int D;

map<pair<int, int>, int> Cache;

int search(int dlast, int i)
{
  const int irange=d[i] + min(l[i], d[i] - dlast);
  if(irange >= D) { return D; }
  auto itr = Cache.find(MP(dlast, i));
  if(itr != Cache.end()) { return itr->second; }
  int okj = -1;
  int range = -1;
  for(int j=i+1; d[j] <= irange && j < N; ++j)
  {
    const int jrange = search(d[i], j);
    if(range < jrange) { range = jrange; okj = j; }
  }
  cerr << PRT(i) << PRT(okj) << PRT(range) << "\n";
  int retval;
  if(range >= D) { retval = D; }else{ retval = -1; }
  Cache[MP(dlast, i)] = retval;
  return retval;
}

bool solve()
{
  Cache.clear();
  return D <= search(0, 0);
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(8);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> N;
    for(int i=0; i<N; ++i)
    {
      cin >> d[i] >> l[i];
    }
    cin >> D;
    cout << "Case #" << X << ": " << (solve() ? "YES" : "NO") << "\n";
  }
  return 0;
}
