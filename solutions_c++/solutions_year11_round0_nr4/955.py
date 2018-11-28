#define PROBLEM_NAME "D"
#define LONG_OUTPUT 0
#define SUBMIT_MODE 1

/*** MODIFY PROG, PROBLEM_NAME AND SUBMIT_MODE ABOVE ***/
/******** SET SUBMIT_MODE TO 1 WHILE SUBMITTING ********/

#if 1

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <climits>
#include <cmath>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void solve();

int rint() {int a; scanf("%d", &a); return a;}

int main()
{
#if SUBMIT_MODE
  char fname[20];
  sprintf(fname, "%s.in", PROBLEM_NAME);
  freopen(fname, "r", stdin);
  sprintf(fname, "%s.out", PROBLEM_NAME);
  freopen(fname, "w", stdout);
#endif
  int t = rint();
  for (int i = 1; i <= t; i++)
  {
    cout << "Case #" << i << (LONG_OUTPUT ? ":\n" : ": ");
    solve();
  }
#if SUBMIT_MODE
  fclose(stdin);
  fclose(stdout);
#endif
  return 0;
}

#endif

/************** WRITE ALL CODE BELOW THIS **************/
/***************** CODE ENTRY: solve() *****************/

void solve()
{
  int a[1010];
  bool vis[1010];
  int n = rint(), res = 0, p, cl;
  memset(vis, 0, sizeof(vis));
  for (int i = 1; i <= n; i++)
    cin >> a[i];
  for (int i = 1; i <= n; i++)
  {
    if (vis[i])
      continue;
    cl = 1;
    p = a[i];
    vis[p] = true;
    while (p != i)
    {
      p = a[p];
      vis[p] = true;
      cl++;
    }
    if (cl > 1)
      res += cl;
  }
  cout << res << ".000000\n";
}
