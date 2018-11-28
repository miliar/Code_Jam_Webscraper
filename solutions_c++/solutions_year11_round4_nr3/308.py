@* Introduction.
This is a solution to Expensive problem from CodeJam 2011 written in CWEB.

I believe this problem is much simpler than it first appears.  Just
from the numbers it's clearly about primes ($10^{12}$ pretty much
indicates this).  Also the maximum input is pretty high, so the result
can't have to do with any sort of enumeration or walking.

Looking at the input data, it's pretty clear what's going on has to do
with the excess prime values.  Let us say our diners are just the
first $n$ powers of two.  In that case, the best case is the largest
guy comes in first, for a value of 1.  If the smallest guy comes in
first, the value is $n$.  So the total spread then is $n-1$.

It's pretty clear the only special case is the 1 case.

@ The basic outline of our solution is here:

@(c.cpp@>=
#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>
using namespace std ;
const int MAXSQRTN = 2000000 ;
int s[MAXSQRTN] ;
int main(int argc, char *argv[]) {
    int N ;
    cin >> N ;
    for (int kase=1; kase<=N; kase++) {
      @<Read one case@> ;
      @<Solve one case@> ;
      cout << setprecision(9) << "Case #" << kase << ": " << r << endl ;
    }
}

@ Reading a case; we use slow |cin| to do this.

@<Read one case@>=
long long n ;
cin >> n ;

@ Solving: we find all primes less than or equal to the square of the
value.  We can do this with a quick sieve.

@<Solve one case@>=
memset(s, 1, sizeof(s)) ;
int r = 0 ;
if (n == 1)
   r = 0 ;
else {
   r = 1 ; // does 1 come in first or not.
   for (long long i=2; i*i<=n; i++) {
      if (s[i]) { // prime
         for (long long j=i*i; j*j<=n; j+=i)
            s[j] = 0 ;
         int p = 0 ;
         long long td = n ;
         while (td >= i) {
            p++ ;
            td /= i ;
         }
         r += p - 1 ;
     }
   }
}
