/* Time Table solution. */
/* Simply simulate the running and see... */

#include <cassert>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <iostream>

unsigned readTime ()
{
  char chrs[6];

  while (!std::isdigit(chrs[0] = std::cin.get ()));
  for (unsigned i(1); i != 5; ++i)
    chrs[i] = std::cin.get ();
  chrs[6] = '\0';
  
  assert (chrs[2] == ':');
  chrs[2] = '\0';

  return 60 * std::atoi (&chrs[0]) + std::atoi (&chrs[3]);
}

class Event
{
  public:

    bool depart;
    bool atA;
    unsigned time;

    inline Event (bool d, bool a, unsigned t)
      : depart(d), atA(a), time(t)
    {}

    friend inline bool operator< (const Event& e1, const Event& e2)
    {
      return !(e1.time < e2.time || (e1.time == e2.time && !e1.depart));
    }

};

typedef std::priority_queue<Event> evtQueue;

void solveCase ()
{
  unsigned t;
  unsigned na, nb;

  std::cin >> t >> na >> nb;

  evtQueue qu;

  for (unsigned i(0); i != na; ++i)
    {
      qu.push (Event (true, true, readTime ()));
      qu.push (Event (false, false, readTime () + t));
    }

  for (unsigned i(0); i != nb; ++i)
    {
      qu.push (Event (true, false, readTime ()));
      qu.push (Event (false, true, readTime () + t));
    }

  unsigned atA(0), atB(0);
  unsigned neededA(0), neededB(0);

  for (; !qu.empty (); qu.pop ())
    {
      const Event& e(qu.top ());

      if (!e.depart)
        {
          if (e.atA)
            ++atA;
          else
            ++atB;
        }
      else
        {
          unsigned* at(e.atA ? &atA : &atB);
          unsigned* needed(e.atA ? &neededA : &neededB);

          if (*at > 0)
            --(*at);
          else
            ++(*needed);
        }
    }

  std::cout << neededA << " " << neededB;
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
