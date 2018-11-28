#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int main(int argc, char *argv[]) {
  long long N ;
  int nn, pd, pg ;
   scanf("%d", &nn) ;
   int kase = 0 ;
   while (scanf("%lld %d %d", &N, &pd, &pg) == 3) {
     int okay = 1 ;
     if (pd > 0 && pg == 0)
       okay = 0 ;
     if (pd < 100 && pg == 100)
       okay = 0 ;
     int gcd = 1 ;
     if (pd % 25 == 0)
       gcd *= 25 ;
     else if (pd % 5 == 0)
       gcd *= 5 ;
     if (pd % 4 == 0)
       gcd *= 4 ;
     else if (pd % 2 == 0)
       gcd *= 2 ;
     int a = pd / gcd ;
     int D = 100 / gcd ;
     if (D > N)
       okay = 0 ;
     if (okay)
       cout << "Case #" << (++kase) << ": Possible" << endl ;
     else
       cout << "Case #" << (++kase) << ": Broken" << endl ;
   }
}
