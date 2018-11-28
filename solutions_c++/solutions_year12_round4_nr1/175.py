/* CodeJam solution swinging in C++ by domob.  */

/* Dynamic programming to try each possibilities:  State is which vine
   I have and to which length I can strech it.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <utility>
#include <set>
#include <vector>
#include <stdint.h>

typedef unsigned short vineIndT;
typedef unsigned long coordT;

typedef std::pair<vineIndT, coordT> stateT;
typedef std::set<stateT> stateSet;
typedef std::vector<stateT> stateQueue;

typedef std::pair<coordT, coordT> vineT;
typedef std::vector<vineT> vineArr;

stateSet alreadyTried;
stateQueue todo;
vineArr vines;


/* Solve a single case.  */

void
solve_case ()
{
  alreadyTried.clear ();
  todo.clear ();
  vines.clear ();

  vineIndT N;
  std::cin >> N;
  for (vineIndT i = 0; i < N; ++i)
    {
      coordT d, l;
      std::cin >> d >> l;
      vines.push_back (vineT(d, l));
    }

  coordT D;
  std::cin >> D;

  stateT cur(0, vines[0].first);
  todo.push_back (cur);
  alreadyTried.insert (cur);
  while (!todo.empty ())
    {
      cur = todo.back ();
      todo.pop_back ();

      /* Assume that swining back does not make sense.  */

      if (D - vines[cur.first].first <= cur.second)
        {
          std::cout << "YES";
          return;
        }

      for (vineIndT i = cur.first + 1; i < N; ++i)
        {
          const coordT dist = vines[i].first - vines[cur.first].first;
          if (dist > cur.second)
            break;

          coordT nextL = std::min (vines[i].second, dist);
          stateT next(i, nextL);
          if (alreadyTried.find (next) == alreadyTried.end ())
            {
              todo.push_back (next);
              alreadyTried.insert (next);
            }
        }
    }

  // No possibilities remaining.
  std::cout << "NO";
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
