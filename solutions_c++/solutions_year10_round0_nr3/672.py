#include <iostream>
#include <vector>
#include <cassert>

typedef unsigned long long ulong;

struct cycle
{
   cycle () : shift (0), rides (0), rides_tot (0), profit (0) {};

   unsigned shift;
   ulong rides;
   ulong rides_tot;
   ulong profit;
};

typedef std::vector <cycle> cycles;
typedef std::vector <ulong> groups;

unsigned board (groups const &g, ulong max_load, unsigned &shift)
{
   if (shift == g.size ())
      return 0;
   ulong const l = g [shift];
   return l > max_load ? 0 : l + board (g, max_load - l, ++shift);
}

bool do_cycle (groups const &g, ulong max_load, unsigned shift, ulong rides_left, cycle &c)
{
   for ( ; ; )
   {
      if (c.rides == rides_left)
         return true;

      ulong load = board (g, max_load, shift);
      ++c.rides;
      if (shift == g.size ())
      {
         load += board (g, max_load - load, shift = 0);
         c.profit += load;
         c.shift = shift;
         return c.rides == rides_left;
      }

      c.profit += load;
   }
}

ulong run_rc (groups const &g, ulong R, ulong k, unsigned shift)
{
   cycles cy (g.size ());

   ulong rides_tot = 0, p = 0;
   for ( ; ; )
   {
      cycle &c = cy [shift];
      if (c.rides)
      {
         ulong full_cycle_rides = rides_tot - c.rides_tot;
         ulong full_cycles = (R - rides_tot) / full_cycle_rides;
         ulong rides_tail = R - rides_tot - full_cycles * full_cycle_rides;
         ulong rrc = run_rc (g, rides_tail, k, shift);
         return p
                + full_cycles * (p - c.profit)
                + rrc;
      }

      bool over = do_cycle (g, k, shift, R - rides_tot, c);
      {ulong cp = c.profit; c.profit = p; p += cp;}

      c.rides_tot = rides_tot;
      rides_tot += c.rides;
      shift = c.shift;

      if (over)
         return p;
   }
}

ulong PROFIT111()
{
   ulong R, k, N, s = 0;
   std::cin >> R >> k >> N;
   groups g (N);
   for (ulong n = 0; n < N; ++n)
   {
      std::cin >> g [n];
      s += g [n];
   }

   if (s <= k)
      return R * s;

   return run_rc (g, R, k, 0);
}

int main ()
{
   unsigned T;
   std::cin >> T;
   for (ulong c = 1; c <= T; ++c)
      std::cout << "Case #" << c << ": " << PROFIT111 () << "\n";
}
