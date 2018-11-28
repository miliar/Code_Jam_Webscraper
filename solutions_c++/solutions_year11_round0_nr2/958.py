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

queue<char> q;
char tq;
bool tqP;

int charNum(char a)
{
  if (a > 'Z')
    return a-'a'+1;
  return a-'A'+1;
}

int size()
{
  return q.size() + (tqP ? 1 : 0);
}

void solve()
{
  list<char> enemy[28];
  list<pair<char, char> > frnd[28];
  set<char> s;
  char tmp[110];
  int c = rint();
  while (c--)
  {
    cin >> tmp;
    frnd[charNum(tmp[0])].push_back(make_pair(tmp[1], tmp[2]));
    frnd[charNum(tmp[1])].push_back(make_pair(tmp[0], tmp[2]));
  }
  c = rint();
  while (c--)
  {
    cin >> tmp;
    enemy[charNum(tmp[0])].push_back(tmp[1]);
    enemy[charNum(tmp[1])].push_back(tmp[0]);
  }
  cin >> c >> tmp;
  tqP = false;
  for (int i = 0; i < c; i++)
  {
    int l = charNum(tmp[i]);
    bool found = false;
    if (tqP)
    {
      for (list<pair<char, char> >::iterator it = frnd[l].begin(); it != frnd[l].end(); it++)
        if (it->first == tq)
        {
          q.push(it->second);
          tqP = false;
          found = true;
          break;
        }
      if (found)
        continue;
      for(list<char>::iterator it = enemy[l].begin(); it != enemy[l].end(); it++)
        if (*it == tq || s.find(*it) != s.end())
        {
          while (!q.empty())
            q.pop();
          s.clear();
          tqP = false;
          found = true;
          break;
        }
    }
    else
    {
      for(list<char>::iterator it = enemy[l].begin(); it != enemy[l].end(); it++)
        if (s.find(*it) != s.end())
        {
          while (!q.empty())
            q.pop();
          s.clear();
          found = true;
          break;
        }
    }
    if (found)
      continue;
    if (tqP)
    {
      q.push(tq);
      s.insert(tq);
    }
    tqP = true;
    tq = tmp[i];
  }
  if (tqP)
    q.push(tq);
  cout << '[';
  while (!q.empty())
  {
    cout << q.front() << (q.size() == 1 ? "" : ", ");
    q.pop();
  }
  cout << ']' << endl;
}
