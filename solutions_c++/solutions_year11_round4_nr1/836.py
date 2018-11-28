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

struct inv
{
  int a, b;
  int s;
  inv(int x, int y, int ss) : a(x), b(y), s(ss)
  {
  
  }
};

void init()
{
}

bool compare(inv first, inv second)
{
  if (first.s < second.s)
    return true;
  return false;
}

void solve()
{
  list<inv> iv;
  int X = rint();
  int S = rint();
  int R = rint();
  double t = rint();
  int N = rint(), b, e, w, x, y, ss;
  iv.push_back(inv(0, X, 0));
  while (N--)
  {
    cin >> b >> e >> w;
    for (list<inv>::iterator it = iv.begin(); it != iv.end(); it++)
      if (it->a <= b && it->b >= e)
      {
        x = it->a;y = it->b;
        iv.erase(it);
        if (x < b)
          iv.push_back(inv(x, b, 0));
        if (e < y)
          iv.push_back(inv(e, y, 0));
        iv.push_back(inv(b, e, w));
        break;
      }
  }
  double tt, d;
  iv.sort(compare);
  double res = 0;
  for (list<inv>::iterator it = iv.begin(); it != iv.end(); it++)
  {
    if (t > 0)
    {
      tt = double(it->b-it->a)/double(R+it->s);
      if (tt < t)
      {
        res += tt;
        t -= tt;
      }
      else
      {
        d = double(it->b-it->a) - t * double(R+it->s);
        res += t + d / double(S+it->s);
        t = 0;
      }
    }
    else
      res += double(it->b-it->a)/double(S+it->s);
  }
  printf("%.7f\n", res);
}
