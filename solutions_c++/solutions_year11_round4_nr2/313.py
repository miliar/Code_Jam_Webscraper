@* Introduction.
This is the solution to the Spinning Blade problem for Google Code Jam
2011, in CWEB.

The idea in this solution is to compute the center of mass for
different subsets of a plate in constant time.

We can do this by accumulating rectangular counts for the center
of mass around the origin, and then using inclusion/exclusion on
the rectangles to compute the center of mass for the subsection.

We need a structure that accumulates counts.  This structure will
hold the weight at that location, the sum of the weights of the
rectangle marked by this location and the origin, and the
moment of inertia around the origin.  For simplicity we also put
the inertia in there too.

@ The basic outline of our solution is here:

@(b.cpp@>=
#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>
using namespace std ;
const int MAX = 600 ;
struct data {
   double mass, xinertia, yinertia ;
} datas[MAX][MAX], acc[MAX][MAX] ;
int add(data &acc, const data &s) {
    acc.mass += s.mass ;
    acc.xinertia += s.xinertia ;
    acc.yinertia += s.yinertia ;
}
int sub(data &acc, const data &s) {
    acc.mass -= s.mass ;
    acc.xinertia -= s.xinertia ;
    acc.yinertia -= s.yinertia ;
}
int main(int argc, char *argv[]) {
    int n ;
    cin >> n ;
    for (int kase=1; kase<=n; kase++) {
      @<Read one case@> ;
      @<Solve one case@> ;
    }
}

@ Reading a case; we use slow |cin| to do this.  Note that D is
always irrelevant.

@<Read one case@>=
int R, C, D ;
memset(datas, 0, sizeof(datas)) ;
cin >> R >> C >> D ;
D = 0 ;
string s ;
for (int i=1; i<=R; i++) {
    cin >> s ;
    double rowmass = 0 ;
    double rowx = 0 ;
    double rowy = 0 ;
    for (int j=1; j<=C; j++) {
       double t = s[j-1] - '0' + D ;
       datas[i][j].mass = t ;
       datas[i][j].xinertia = i * t ;
       datas[i][j].yinertia = j * t ;
       rowmass += t ;
       rowx += i * t ;
       rowy += j * t ;
       acc[i][j].mass = rowmass + acc[i-1][j].mass ;
       acc[i][j].xinertia = rowx + acc[i-1][j].xinertia ;
       acc[i][j].yinertia = rowy + acc[i-1][j].yinertia ;
    }
}


@ Solving.  For the small size, we can just iterate over sizes until
we find one that works.

@<Solve one case@>=
int r = 0 ;
int sz = R ;
if (sz > C)
   sz = C ;
while (sz >= 3) {
   for (int i=0; i+sz<=R; i++)
      for (int j=0; j+sz<=C; j++) {
         data a ;
         memset(&a, 0, sizeof(a)) ;
         add(a, acc[i+sz][j+sz]) ;
         add(a, acc[i][j]) ;
         sub(a, acc[i+sz][j]) ;
         sub(a, acc[i][j+sz]) ;
	 sub(a, datas[i+1][j+1]) ;
	 sub(a, datas[i+sz][j+1]) ;
	 sub(a, datas[i+sz][j+sz]) ;
	 sub(a, datas[i+1][j+sz]) ;
	 if (a.xinertia * 2 == a.mass * (2*i + 1 + sz) &&
	     a.yinertia * 2 == a.mass * (2*j + 1 + sz)) {
            goto found ;
         }
      }
   sz-- ;
}
found:
if (sz < 3)
   cout << "Case #" << kase << ": " << "IMPOSSIBLE" << endl ;
else
   cout << "Case #" << kase << ": " << sz << endl ;
