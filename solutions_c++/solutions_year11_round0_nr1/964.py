#define PROBLEM_NAME "A"
#define LONG_OUTPUT false
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
  int n = rint();
  int ap = 1, at = 0, bp = 1, bt = 0, t = 0, p, tm;
  char r;
  while (n--)
  {
    cin >> r >> p;
    if (r == 'O')
    {
      tm = ap-p;
      if (tm < 0)
        tm = -tm;
      if (t-at < tm)
        t = tm+at+1;
      else
        t++;
      at = t;
      ap = p;
    }
    else
    {
      tm = bp-p;
      if (tm < 0)
        tm = -tm;
      if (t-bt < tm)
        t = tm+bt+1;
      else
        t++;
      bt = t;
      bp = p;
    }
  }
  cout << t << endl;
}
