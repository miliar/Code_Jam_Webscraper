/* CodeJam solution ticket in C++ by domob.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>

static const int MAX_P = 10;

int p;
int miss[1 << MAX_P];


/* Build up a tree of matches.  */

class MatchTree
{
  public:

    int round;
    int price;

    int teamA, teamB;
    MatchTree* treeA;
    MatchTree* treeB;

    int cost[MAX_P + 1];

    MatchTree ()
    {
      for (int i = 0; i <= MAX_P; ++i)
        cost[i] = -1;
    }

    ~MatchTree ()
    {
      if (round != 1)
        {
          delete treeA;
          delete treeB;
        }
    }

    int costForThis (int missed)
    {
      assert (missed >= 0 && missed <= MAX_P);
      if (cost[missed] == -1)
        {
          int c = 0;

          if (isPossible (missed))
            {
              /* I can take this ticket or not.  If I take it, I have the
                 costs here
                 and still the same amount of missing possibility for all
                 matches, so continue.  If I don't take it, I possibly miss
                 each team once, so recurse but with reduced missing
                 allowance.  */

              c = price;
              if (round != 1)
                {
                  c += treeA->costForThis (missed);
                  c += treeB->costForThis (missed);
                }

              if (isPossible (missed + 1))
                {
                  int c2 = 0;
                  if (round != 1)
                    {
                      c2 += treeA->costForThis (missed + 1);
                      c2 += treeB->costForThis (missed + 1);
                    }

                  if (c2 < c)
                    c = c2;
                }
            }
          else
            c = 2000000000;
              
          cost[missed] = c;
        }

      return cost[missed];
    }

    bool isPossible (int missed)
    {
      if (round == 1)
        return miss[teamA] >= missed && miss[teamB] >= missed;

      return treeA->isPossible (missed) && treeB->isPossible (missed);
    }

    void incMissing (int add)
    {
      if (round == 1)
        {
          miss[teamA] += add;
          miss[teamB] += add;
          assert (miss[teamA] >= 0);
          assert (miss[teamB] >= 0);
        }
      else
        {
          treeA->incMissing (add);
          treeB->incMissing (add);
        }
    }

};


/* Solve a single case.  */

void
solve_case ()
{
  scanf ("%d", &p);
  for (int i = 0; i < (1 << p); ++i)
    scanf ("%d", &miss[i]);

  MatchTree** trees;
  int numTrees = (1 << (p - 1));
  int round = 1;

  trees = new MatchTree*[numTrees];
  for (int i = 0; i < numTrees; ++i)
    {
      trees[i] = new MatchTree ();
      trees[i]->round = round;
      trees[i]->teamA = 2 * i;
      trees[i]->teamB = 2 * i + 1;
      scanf ("%d", &trees[i]->price);
    }

  while (numTrees > 1)
    {
      int newTrees = numTrees / 2;
      MatchTree** ntrees;
      ntrees = new MatchTree*[newTrees];
      ++round;
      
      for (int i = 0; i < newTrees; ++i)
        {
          ntrees[i] = new MatchTree ();
          ntrees[i]->round = round;
          ntrees[i]->treeA = trees[2 * i];
          ntrees[i]->treeB = trees[2 * i + 1];
          scanf ("%d", &ntrees[i]->price);
        }

      delete[] trees;
      trees = ntrees;

      numTrees = newTrees;
    }

  printf ("%d", trees[0]->costForThis (0));
  delete[] trees;
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
