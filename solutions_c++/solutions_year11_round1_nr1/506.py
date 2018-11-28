#define PROBLEM_NAME "A"
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

void init();
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
  init();
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

void init()
{
  // PREPROCESS HERE
}

void solve()
{
  ll n;
  cin >> n;
  ll pd = rint();
  ll pg = rint();
  if (pg == 100 && pd < 100)
  {
    cout << "Broken\n";
    return;
  }
  if (pd > 0 && pg == 0)
  {
    cout << "Broken\n";
    return;
  }
  for (ll d = 1; d <= n; d++)
    if((d*pd)%100 == 0)
    {
      cout << "Possible\n";
      return;
    }
  cout << "Broken\n";
}
