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
int M[1000];
int m[1000][10];

bool solve()
{
  for(int i=0; i < N; ++i)
  {
    vector<bool> visited(N, false);
    vector<vector<bool> > mUsed(N, vector<bool>(N, false));
    queue<int> Q;
    Q.push(i);
    while(!Q.empty())
    {
      const int j = Q.front();
      Q.pop();
      cerr << "popped" << PRT(j) << "\n";
      visited[j] = true;
      for(int t=0; t<M[j]; ++t)
      {
        const int k = m[j][t];
        // j -> k
        cerr << PRT(j) << PRT(M[j]) << PRT(k) << PRT(mUsed[j][k]) << PRT(visited[k]) << "\n";
        if(mUsed[j][k]) { continue; }
        if(visited[k]) { return true; }
        visited[k] = mUsed[j][k] = mUsed[k][j] = true;
        Q.push(k);
      }
    }
  }
  return false;
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
      cin >> M[i];
      for(int j=0; j < M[i]; ++j)
      {
        cin >> m[i][j];
        --m[i][j];
      }
    }
    cout << "Case #" << X << ": " << (solve() ? "Yes" : "No") << "\n";
  }
  return 0;
}
