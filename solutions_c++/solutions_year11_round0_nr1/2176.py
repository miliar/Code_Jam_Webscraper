using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin();  \
                           x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

const double EPS = 1e-9;
int cmp(double x, double y = 0, double tol = EPS){
  return( x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int time_move(int pos, int move, int &sec_acum, string last_moved, string robot){
  int ans = 0;
  if(last_moved == robot)
    {
      int delta = abs(pos - move) + 1;
      ans = delta;
      sec_acum += delta;
    }
  else
    {
      int delta = abs(pos - move);
      if(delta < sec_acum)
        {
          ans = 1;
          sec_acum = 1;
        }
      else
        {
          delta -= sec_acum;
          ans = delta + 1;
          sec_acum = delta + 1;
        }
    }
  return ans;
}
int main(){
  int N;
  cin >> N;
  for(int c = 1; c <= N; ++c)
    {
      int n;
      cin >> n;
      string robot;
      int move;
      int ans = 0;
      int pos_a = 1, pos_b = 1;
      string last_moved = "";
      int sec_acum = 0;
      for(int i = 0; i < n ; ++i)
        {
          cin >> robot >> move;
          if(last_moved == "") last_moved = robot;
          if(robot == "O")
            {
              ans += time_move(pos_a, move, sec_acum, last_moved, robot);
              pos_a = move;
            }
          else
            {
              ans += time_move(pos_b, move, sec_acum, last_moved, robot);
              pos_b = move;
            }
          last_moved = robot;
        }


      printf("Case #%d: %d\n", c, ans);
    }
  return 0;
}
