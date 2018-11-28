#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cstdlib>
#include <stdint.h>

#define MAX_M 10000

struct
{
  unsigned interior:1;
  unsigned is_and:1;
  unsigned changable:1;
  unsigned value:1;
} tree[MAX_M];

unsigned m;

inline unsigned getParent (unsigned x)
{
  assert (x > 0);
  return x / 2;
}

inline unsigned getLeft (unsigned x)
{
  unsigned res(2 * (x + 1) - 1);
  assert (res < m);
  return res;
}

inline unsigned getRight (unsigned x)
{
  unsigned res(getLeft(x) + 1);
  assert (res < m);
  return res;
}

inline void calcValue (unsigned i)
{
  assert (tree[i].interior);
  if (tree[i].is_and)
    tree[i].value = (tree[getLeft(i)].value && tree[getRight(i)].value ? 1 : 0);
  else
    tree[i].value = (tree[getLeft(i)].value || tree[getRight(i)].value ? 1 : 0);
}

int cache[MAX_M][2];

unsigned getForTree (unsigned root, unsigned v)
{
  if (tree[root].value == v)
    return 0;

  if (!tree[root].interior)
    return m+1;

  if (cache[root][v] != -1)
    return cache[root][v];

  const unsigned l(getLeft(root)), r(getRight(root));

  unsigned needed_if_and;
  if (v)
    needed_if_and = getForTree(l, 1) + getForTree(r, 1);
  else
    {
      needed_if_and = getForTree(l, 0);
      needed_if_and = std::min (needed_if_and, getForTree(r, 0));
    }

  unsigned needed_if_or;
  if (v)
    {
      needed_if_or = getForTree(l, 1);
      needed_if_or = std::min (needed_if_or, getForTree(r, 1));
    }
  else
    needed_if_or = getForTree(l, 0) + getForTree(r, 0);

  unsigned res(tree[root].is_and ? needed_if_and : needed_if_or);

  if(tree[root].changable)
    {
      if (tree[root].is_and)
        res = std::min (res, needed_if_or + 1);
      else
        res = std::min (res, needed_if_and + 1);
    }

  cache[root][v] = res;
  return res;
}

void solveCase ()
{
  unsigned v;
  std::cin >> m >> v;
  assert (m%2 == 1);

  for (unsigned i(0); i != m; ++i)
    cache[i][0] = cache[i][1] = -1;

  for (unsigned i(0); i != m; ++i)
    {
      tree[i].interior = (i+1 <= (m-1)/2);
      if (tree[i].interior)
        {
          unsigned is_and, changable;
          std::cin >> is_and >> changable;
          tree[i].is_and = is_and;
          tree[i].changable = changable;
        }
      else
        {
          unsigned val;
          std::cin >> val;
          tree[i].value = val;
        }
    }

  for (unsigned i(m-1); i < m; --i)
    if (tree[i].interior)
      calcValue (i);

  unsigned res(getForTree(0, v));

  if (res < m)
    std::cout << res;
  else
    std::cout << "IMPOSSIBLE";
}

int main ()
{
  unsigned n;
  std::cin >> n;

  for (unsigned i(1); i <= n; ++i)
    {
      std::cout << "Case #" << i << ": ";
      solveCase ();
      std::cout << std::endl;
    }

  return EXIT_SUCCESS;
}
