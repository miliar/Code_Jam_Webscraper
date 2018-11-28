#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <list>
#include <stack>
#include <queue>

using namespace std;

int solve()
{
  int inputs;
  char color;
  int button;
  int b_steps = 0;
  int o_steps = 0;
  int b_pos = 1;
  int o_pos = 1;

  cin >> inputs;

  while (inputs >0) {
    --inputs;
    cin >> color >> button;
    if (color == 'B') {
      b_steps += abs(b_pos - button);
      if (b_steps <= o_steps)
        b_steps = o_steps+1;
      else
        b_steps++;
      b_pos = button;
    }
    else if (color == 'O') {
      o_steps += abs(o_pos - button);
      if (o_steps <= b_steps)
        o_steps = b_steps+1;
      else
        o_steps++;
      o_pos = button;
    }
    else
      assert(0);
  }
  if (o_steps > b_steps)
    return o_steps;
  return b_steps;
}

int main(int ac, char **av)
{
  int cases;

  cin >> cases;
  for (int i=1; i <= cases; ++i) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}

