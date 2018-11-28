/* Solution for Universe-Search-Engine problem. */

/* First, while reading in the strings, they are translated to the integers
 * 1..S for ease of handling later.
 *
 * Greedy-Algorithm:
 * Start with the engine appearing latest in the search-term list, and switch
 * to the one appearing latest after the switch when we have to switch.
 */

#include <cassert>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
#include <string>

typedef std::map<std::string, unsigned> stringMap;

typedef std::vector<bool> lstSup;
class EngineList : public lstSup
{
  public:

    unsigned s;
    unsigned stillPossible;

    explicit EngineList (unsigned i);

    void allPossible ();
    bool remove (unsigned i);

};

EngineList::EngineList (unsigned i)
  : lstSup (i), s(i)
{
  assert (size () == s);
  allPossible ();
}

void EngineList::allPossible ()
{
  stillPossible = s;
  for (iterator i(begin ()); i != end (); ++i)
    *i = true;
}

bool EngineList::remove (unsigned i)
{
  if (!operator[] (i))
    return true;

  operator[] (i) = false;
  --stillPossible;

  return stillPossible != 0;
}

unsigned solveCase ()
{
  unsigned s;
  std::string line;
  stringMap keys;

  std::cin >> s;
  std::getline (std::cin, line);
  for (unsigned i(0); i != s; ++i)
    {
      std::getline (std::cin, line);
      keys[line] = i;
    }

  EngineList l(s);
  unsigned switches(0);

  unsigned q;
  std::cin >> q;
  std::getline (std::cin, line);
  for (unsigned i(0); i != q; ++i)
    {
      std::getline (std::cin, line);
      assert (keys.find (line) != keys.end ());
      const unsigned query (keys[line]);
      assert (query < s);

      if (l.remove (query))
        continue;

      l.allPossible ();
      ++switches;
      l.remove (query);
    }

  return switches;
}

int main ()
{
  unsigned n;
  std::cin >> n;

  for (unsigned i(1); i <= n; ++i)
    std::cout << "Case #" << i << ": " << solveCase () << std::endl;

  return EXIT_SUCCESS;
}
