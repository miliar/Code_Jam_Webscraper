#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
#include<bitset>
#include<sstream>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<numeric>
#include<complex>
#include<utility>
#include<ext/numeric>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

const int MAX_N = 100;
const int MAX_K = 25;

int A[MAX_N][MAX_K];
bool smaller[MAX_N][MAX_N];

bool visited[MAX_N];

vi order;

int N;

void explore(int n)
{
  visited[n] = 1;
  for(int m = 0; m < N; m++)
    if(smaller[m][n] && !visited[m])
      explore(m);
  order.push_back(n);
}

int memo[1 << 16][MAX_N];

int go(int m, int c)
{
  if(c == N)
    return __builtin_popcount(m);
  int &r = memo[m][c];
  if(r >= 0)
    return r;
  r = go(m | (1 << c), c+1);
  for(int i = 0; i < c; i++)
    if(((m >> i) & 1) && smaller[order[i]][order[c]])
      r = min(r, go(m - (1 << i) + (1 << c), c+1));
  return r;
}

int main()
{
  int T;
  cin >> T; cin.ignore();
  for(int t = 1; t <= T; t++)
    {
      cout << "Case #" << t << ": ";
      memset(smaller, 0, sizeof(smaller));
      int K;
      cin >> N >> K;
      for(int n = 0; n < N; n++)
        for(int k = 0; k < K; k++)
          cin >> A[n][k];
      for(int n = 0; n < N; n++)
        for(int m = 0; m < N; m++)
          {
            int k = 0;
            while(k < K && A[n][k] < A[m][k])
              k++;
            smaller[n][m] = k == K;
          }
      order.clear();
      fill_n(visited, N, 0);
      for(int n = 0; n < N; n++)
        if(!visited[n])
          explore(n);

      /*      
      int r = 0;
      vector<bool> v(N);
      for(int n = 0; n < N; n++)
        if(!v[n])
          {
            r++;
            int cur = n;
            for(int m = n+1; m < N; m++)
              {
                if(smaller[order[cur]][order[m]])
                  {
                    v[m] = 1;
                    cur = m;
                  }
              }
          }
      for(int n = 0; n < N; n++)
        cout << order[n] << " ";
      puts("");
      cout << r << endl;*/

      memset(memo, -1, sizeof(memo));
      cout << go(0, 0) << endl;
    }
}
