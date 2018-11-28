#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)
const int MAXN = 2004;

int s[MAXN];
int h[MAXN];

void run(int l, int r, int x){
  if(l+1 == r)
    return;
  l++;
  h[l] = h[r]-(r-l)*x;
  for(; l != r; l = s[l]){
    h[s[l]] = h[r]-(r-s[l])*x;
    run(l, s[l], x+1);
  }
}

int main()
{
  #ifdef __FIO
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif
  int _;
  scanf("%d", &_);
  for(int i0 = 1; i0 <= _; i0++){
    printf("Case #%d: ", i0);
    int n;
    int i, j;
    int t = 1;
    scanf("%d", &n);
    for(i = 1; i < n; i++)
      scanf("%d", &s[i]);
    for(i = 1; i < n; i++)
      for(j = i+1; j < s[i]; j++)
        if(s[j] > s[i])
          t = 0;
    if(t){
      h[1] = 100000000;
      for(i = 1; i != n; i = s[i]){
        h[s[i]] = h[i];
        run(i, s[i], 1);
      }
      for(i = 1; i <= n; i++)
        printf("%d ", h[i]);
      printf("\n");
    }
    else
      printf("Impossible\n");
  }
  return 0;
}
