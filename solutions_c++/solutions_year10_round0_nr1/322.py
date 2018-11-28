/* CodeJam solution snapper in C++ by domob.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>

typedef uint32_t intT;


/* Solve a single case.  I simply simulate it, where I keep the
   snapper states as bits within an integer, lower ones mean snappers
   at the front of the chain.  This should be fast enough, I guess.  */

void
solve_case ()
{
  intT n, k;
  scanf ("%u %u", &n, &k);

  intT state = 0;
  for (intT i = 1; i <= k; ++i)
    {
      intT power = 1;
      intT powerMask = 1;
      for (intT j = 1; j <= n; ++j)
        {
          if ((state & powerMask) == 0)
            break;
          powerMask <<= 1;
          power |= powerMask;
        }
      state ^= power;
    }

  intT mask = 1;
  bool lightOn = true;
  for (intT i = 1; i <= n; ++i)
    {
      if ((state & mask) == 0)
        {
          lightOn = false;
          break;
        }
      mask <<= 1;
    }

  printf ("%s", lightOn ? "ON" : "OFF");
}


/* Main routine, handling the different cases.  */

int
main ()
{
  int n;

  scanf ("%d\n", &n);
  for (int i = 1; i <= n; ++i)
    {
      printf ("Case #%d: ", i);
      solve_case ();
      printf ("\n");
    }

  return EXIT_SUCCESS;
}
