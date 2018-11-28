#include <math.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <deque> 
#include <iostream>

using namespace std;


int bmat[512][512];
int  dp[512][512];
char buffer[512][513];
  
static int getValue(char c, int bit)
{
  int v = c;
  if (v >= 'A') v = v - 'A' + 10;
  else v -= '0';
  return (v & (1 << (3-bit))) == 0;
}

static void check(int i, int j)
{
  if (dp[i][j] < 0 && bmat[i][j] != -1) {
    int lasti = i - 1;
    int lastj = j - 1;
    if (bmat[i][j] ^ bmat[lasti][lastj] || bmat[lasti][lastj] == -1) {
      dp[i][j] = 1;
      return;
    }
    
    int size  = dp[lasti][lastj];
    int mini  = size + 1;
    int minj  = size + 1;

    /* check height */
    int cur = bmat[i][j];
    for (int k = i - 1; k >= 0 && k >= i - size; k--) {
      if ((cur ^ bmat[k][j]) && bmat[k][j] != -1) {
        cur = bmat[k][j];
      } else {
        mini = i - k;
        break;
      }
    }

    /* check vertical */
    cur = bmat[i][j];
    for (int k = j - 1; k >= 0 && k >= j - size; k--) {
      if (cur ^ bmat[i][k] && bmat[i][k] != -1) {
        cur = bmat[i][k];
      } else {
        minj = j - k;
        break;
      }
    }
    dp[i][j] = min(mini, minj);
  }
}

static void cut(int m, int n, int& count, map<int, int>& vmap)
{
  int max_size = 0;
  int max_i    = 0;
  int max_j    = 0;
  for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++) {
      if (max_size < dp[i][j]) {
        max_size = dp[i][j];
        max_i    = i;
        max_j    = j;
      }
    }
  if (vmap.find(max_size) != vmap.end()) 
    vmap[max_size]++;
  else
    vmap[max_size] = 1;
   for (int k = max_size - 1; k >= 0; k--) 
    for (int l = max_size - 1; l>= 0; l--){
        bmat[max_i - k][max_j - l] = -1;
   }
   count -= max_size * max_size;
}

static int solve(int m, int n)
{
  for (int i = 0; i < m ; i++)
    for (int j = 0; j < n / 4; j++) {
      bmat[i][4 * j]      = getValue(buffer[i][j], 0); 
      bmat[i][4 * j + 1]  = getValue(buffer[i][j], 1);
      bmat[i][4 * j + 2]  = getValue(buffer[i][j], 2); 
      bmat[i][4 * j + 3]  = getValue(buffer[i][j], 3);
    }

  int count = m * n;
  map<int, int> vmap;
  while (count > 0) {
    memset(dp, -1, sizeof(dp));
   
    for (int i = 0; i < m; i++)
      if (bmat[i][0] != -1)
        dp[i][0] = 1;
    for (int i = 0; i < n; i++)
      if (bmat[0][i] != -1)
        dp[0][i] = 1;

    for (int i = 0; i < m; i++) 
      for (int j = 0; j < n; j++) {
        check(i, j);
      }

    cut(m, n, count, vmap);
  }

  printf("%d\n", vmap.size());
  for (map<int, int>::reverse_iterator it = vmap.rbegin(); it != vmap.rend();
    ++it) {
    printf("%d %d\n", it->first, it->second);
  }
  vmap.clear();
  return 0;
}


int main()
{
  int T;

  //calcC();
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {

    printf("Case #%d: ", i);
    int m, n;
   

    scanf("%d%d",&m, &n);
    for (int k = 0 ; k < m; k++)
      scanf("%s", buffer[k]);

    solve(m, n);
  }

  return 0;
}
