#define PROBLEM_NAME "B"
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

int gr[12][12];

void solve()
{
  int r = rint();
  int c = rint();
  int d = rint();
  char tmp[12];
  for (int i = 0; i < r; i++)
  {
    cin >> tmp;
    for (int j = 0; j < c; j++)
      gr[i][j] = d + int(tmp[j]-'0');
  }
  for (int k = (r < c ? r : c); k > 2; k--)
  {
    for (int i = 0; i < r-k+1; i++)
      for (int j = 0; j < c-k+1; j++)
      {
        int cx = 0, cy = 0;
        int cex = 2*i + k-1;
        int cey = 2*j + k-1;
        for (int ii = i; ii < i+k; ii++)
          for (int jj = j; jj < j+k; jj++)
          {
            bool found = (ii == i || ii == i+k-1) ? true : false;
            found = (found && (jj == j || jj == j+k-1)) ? true : false;
            if (found)
              continue;
            cx += (2*ii - cex)*gr[ii][jj];
            cy += (2*jj - cey)*gr[ii][jj];
          }
        if (cx == 0 && cy == 0)
        {
          cout << k << endl;
          return;
        }
      }
  }
  cout << "IMPOSSIBLE\n";
}
