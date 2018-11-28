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
#define LNG(x) (sizeof(x)/sizeof(*(x)))
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define INF 100000000

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int T;
int N;
ll S[512];

int saveflags[4000000];

vector<int> parse(unsigned flag)
{
  vector<int> temp;
  for(size_t i=0; i<N; ++i)
  {
    if(flag & (1<<i)) { temp.PB(S[i]); }
  }
  return temp;
}

void p(unsigned flag)
{
  vector<int> X = parse(flag);
  assert(X.size() != 0);
  cout << X[0];
  for(size_t i=1; i<X.size(); ++i)
  {
    cout << " " << X[i];
  }
  cout << "\n";
}

int getsum(unsigned flag)
{
  vector<int> X = parse(flag);
  int ans=0;
  for(size_t i=0; i<X.size(); ++i)
  {
    ans += X[i];
  }
  return ans;
}

void solve()
{
  memset(saveflags, -1, sizeof(saveflags));
  for(unsigned int flag = 1; flag < (1<<N); ++flag)
  {
    int sum = getsum(flag);
    if(saveflags[sum] > 0) {
      p(saveflags[sum]);
      p(flag);
      return;
    }
    saveflags[sum] = flag;
  }
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(6);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> N;
    for(int i=0; i<N; ++i)
    {
      cin >> S[i];
    }
    cout << "Case #" << X << ":\n";
    solve();
  }
  return 0;
}
