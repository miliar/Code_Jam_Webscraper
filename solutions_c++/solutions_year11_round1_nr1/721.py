#include "template.cc"

/* Possible if
     100/gcd(100,Pd) <= N (Pd/100 is a fraction, which must simplify to denominator, i.e. smallest possible D, <= N)
     provided that if we lost any today (Pd<100) then Pg<100
      and similarly if we won any today (Pd>0) then Pg>0
     N>=1 (required because D>0) if Pd!=Pg since D>0
  because there are no constraints on # of wins/losses before today, we can make any percentage overall
*/


bool possible(U N,U Pd,U Pg) {
  if (Pd<100 and Pg==100) return false;
  if (Pd>0 and Pg==0) return false;
  if (N<1) return false; // dataset constraints already say this
  U minD=100/gcd(Pd,100);
  debug(N,Pd,minD);
  return minD<=N;
}

void solve()
{
  U N,Pd,Pg;
  readq(N);
  readq(Pd);
  readq(Pg);
  cout << (possible(N,Pd,Pg) ? "Possible" : "Broken");
}

void init() {}
