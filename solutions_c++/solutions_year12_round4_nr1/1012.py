#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <queue>

using namespace std;

typedef long long huge;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef pair<int, int> pi;
typedef vector<pair<int, int> > vpi;

#define oo 0x3f3f3f3f
#define fn(_i, _n) for(int (_i) = 0; (_i) < (_n); (_i)++)
#define fi(_n) fn(i, (_n))
#define fj(_n) fn(j, (_n))
#define fk(_n) fn(k, (_n))
#define foreach(_x) for(typeof((_x).begin()) it = (_x).begin(); it != (_x).end(); it++)
#define pb(_x) push_back((_x))
#define sz(_x) ((int)(_x).size())
#define all(_x) (_x).begin(), (_x).end()
#define rall(_x) (_x).rbegin(), (_x).rend()
#define mp(_x, _y) make_pair((_x), (_y))
#define fill(_x, _y) memset((_x), (_y), sizeof(_x))
#define zero(_x) fill(_x, 0)
#define shl(_n) (1<<(_n))
#define lshl(_n) (1LL<<(_n))

#define MAX 10100
int N, d[MAX], l[MAX], memo[MAX];

int faz(int n)
{
  int &home = memo[n];

  if (home < 0)
  {
    home = 0;
    for(int i = n-1; i >= 0; i--)
    {
      if (d[n]-d[i] > l[i])
        continue;
      faz(i);
      if (d[n]-d[i] <= memo[i])
        home = max(home, min(d[n]-d[i], memo[i]));
    }
  }

  return home;
}

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    fill(memo, -1);
    scanf("%d", &N);
    fi(N)
      scanf("%d %d", d+i, l+i);
    scanf("%d", &d[N]);
    l[N] = d[N]-d[N-1]+1;

    memo[0] = min(d[0], l[0]);
    faz(N);
    /*
    fi(N+1)
      printf("[%d]", memo[i]);
    */

    printf("Case #%d: %s\n", caso, memo[N] > 0 ? "YES" : "NO");
  }

  return(0);
}

