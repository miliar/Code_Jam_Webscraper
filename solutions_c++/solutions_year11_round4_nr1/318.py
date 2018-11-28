@* Introduction.
This is a solution to Airport problem from CodeJam 2011 written in CWEB.

The idea in this problem is we want to catch our flight as quickly as
possible.  We can walk at speed $S$, run at speed $R$.  When we are
on walkway $i$, our speed is $w_i+S$ if we are walking, and
$w_i+R$ if we are running.  All walkway speeds are greater than one.

The maximum duration we can run is $t$.  That's our unit; we want to
make the best use of those $t$ seconds we can.

All input is integers.

For simplicity, we will assume we always walk or run on a whole
walkway.  In practice, we may need to virtually "split" a walkway
into a running section and a walking section, if we do not have
enough time left to walk the whole way.

We can treat the non-walkway portion as though it were a zero-speed
walkway.

Let us imagine we have an infinitesimal time $d$ that we can run.
What's the best place to use that running?  The time to walk on
that infinitesimal section is $d/(w_i+S)$, the time to run on it
is $d/(w_i+R)$, so the difference is $$d(R-S)\over(w_i+S)(w_i+R)$$.
This is higher for lower $w_i$.

So the best way to do this is to run on the faster walkways as
much as possible.

So we read in all the walkways, add a virtual one for the zero speed
walkway, sort them by the speed of the walkway, and then use up
our running time on the fastest walkways first.

@ The basic outline of our solution is here:

@(a.cpp@>=
#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>
using namespace std ;
int main(int argc, char *argv[]) {
    int n ;
    cin >> n ;
    for (int kase=1; kase<=n; kase++) {
      @<Read one case@> ;
      @<Solve one case@> ;
      cout << setprecision(9) << "Case #" << kase << ": " << r << endl ;
    }
}

@ Reading a case; we use slow |cin| to do this.

@<Read one case@>=
int S, R, t, X, N, td,  ;
vector<pair<int, int> > w ;
cin >> X >> S >> R >> t >> N ;
int xrem = X ;
for (int i=0; i<N; i++) {
   int bt, et, wt ;
   cin >> bt >> et >> wt ;
   xrem -= et - bt ;
   w.push_back(make_pair(wt, et-bt)) ;
}
w.push_back(make_pair(0, xrem)) ;

@ Solving:  sort then scan.  For the scan part, we need to determine for
each walkway how much time we can still run on it.  If we run on it, it
takes time $(E-B)/(w_i+R)$.

@<Solve one case@>=
double r = 0.0 ;
double tr = t ;
sort(w.begin(), w.end()) ;
for (int i=0; i<(int)w.size(); i++) {
    double runtime = w[i].second / (double)(w[i].first + R) ;
    if (runtime > tr) // can only run part of it
       runtime = tr ;
    tr -= runtime ;
    r += runtime +
         (w[i].second - (runtime * (w[i].first + R))) /
         (double)(w[i].first + S) ;
}
