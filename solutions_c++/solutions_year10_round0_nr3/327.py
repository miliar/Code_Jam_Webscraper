/* CodeJam solution park in C++ by domob.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdint.h>

typedef uint64_t intT;
typedef std::vector<intT> intArr;


/* Solve a single case.  First of all, I transform the input into an easier
   to handle form:  Keep current head-of-queue as index 0..N-1 and store
   in seperate arrays how much the roller coaster will make when the first
   group is index i and how many groups will fit into, namely how i
   will be incremented for one ride.

   With this form, I'll then work later on.  */

void
solve_case ()
{
  intT R, k, N;
  scanf ("%llu %llu %llu", &R, &k, &N);

  intArr groups;
  groups.reserve (N);
  for (intT i = 1; i <= N; ++i)
    {
      groups.push_back (0);
      scanf ("%llu", &groups.back ());
    }

  intArr moneyPerRide;
  intArr groupsPerRide;
  moneyPerRide.reserve (N);
  groupsPerRide.reserve (N);

  for (intT i = 0; i < N; ++i)
    {
      intT curGroups = 0;
      intT curPeople = 0;

      intT j = i;
      // Allow maximum of all people in the queue to ride at once!
      while (curGroups == 0 || j != i)
        {
          if (curPeople + groups[j] > k)
            break;

          curPeople += groups[j];
          ++curGroups;

          ++j;
          j %= N;
        }

      moneyPerRide[i] = curPeople;
      groupsPerRide[i] = curGroups;
    }

  // Simulate the day with these data known.
  intT moneyMade = 0;
  intT curStart = 0;
  for (intT i = 1; i <= R; ++i)
    {
      moneyMade += moneyPerRide[curStart];
      curStart += groupsPerRide[curStart];
      curStart %= N;
    }

  printf ("%llu", moneyMade);
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
