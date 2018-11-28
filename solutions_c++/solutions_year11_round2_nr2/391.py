//
// Round 1b  problem B
//
// Usually built with g++ 4.4.5 on Linux
// Sometimes uses GMP for big integers
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

double solve( unsigned int dist,
	      vector<int> posn,
	      vector<int> m)
{
     unsigned int n = posn.size();
     vector<double> low(n);
     vector<double> high(n);
     vector<double> time(n);
     unsigned int i;

     for (i=0; i<n; i++) {
	  low.at(i)  = posn.at(i) - m.at(i)/2.0 * dist;
	  high.at(i) = posn.at(i) + m.at(i)/2.0 * dist;
	  time.at(i) = (m.at(i)-1)/2.0 * dist;
     }

loop:
     for (i=0; i<n; i++) {
	  cerr << setw(8) << low.at(i)  << " ";
	  cerr << setw(8) << high.at(i) << "  -- time ";
	  cerr << setw(8) << time.at(i) << " ";
	  cerr << endl;
     }
     cerr << endl;

     for (i=0; i<n-1; i++) {
	  if (high.at(i) > low.at(i+1)) {
	       double overlap = high.at(i) - low.at(i+1);
	       if (time.at(i) > time.at(i+1)) {
		    cerr << "Adjust 1..." << endl;
		    double time_delta = time.at(i) - time.at(i+1);
		    if (time_delta > overlap) {
			 high.at(i+1) += overlap;
			 low.at(i+1)  += overlap;
			 time.at(i+1) += overlap;
		    } else {
			 high.at(i+1) += time_delta;
			 low.at(i+1)  += time_delta;
			 time.at(i+1) += time_delta;
		    }
		    goto loop;
	       } else if (time.at(i) < time.at(i+1)) {
		    cerr << "Adjust 2..." << endl;
		    double time_delta = time.at(i+1) - time.at(i);
		    if (time_delta > overlap) {
			 high.at(i) -= overlap;
			 low.at(i)  -= overlap;
			 time.at(i) += overlap;
		    } else {
			 high.at(i) -= time_delta;
			 low.at(i)  -= time_delta;
			 time.at(i) += time_delta;
		    }
		    goto loop;
		    
	       } else {
		    cerr << "Adjust 3..." << endl;
		    low.at(i) = low.at(i) - overlap/2.0;
		    high.at(i) = high.at(i+1) + overlap/2.0;
		    time.at(i) = time.at(i) + overlap/2.0;

		    for (unsigned int j=i+1; j<n-1; j++) {
			 low.at(j) = low.at(j+1);
			 high.at(j) = high.at(j+1);
			 time.at(j) = time.at(j+1);
		    }
		    n--;
		    goto loop;
	       }
	  }
     }
	  
     double t= time.at(0);
     for (unsigned int j=0; j<n; j++) {
	  if (time.at(j) > t) t = time.at(j);
     }

     return t;
}

int main( int argc, char ** argv )
{
     unsigned int nn;
     unsigned int i,j;
     unsigned int c;
     unsigned int d;

     cin >> nn;

     for (i=1; i<=nn; i++) {
	  
	  cin >> c;
	  cin >> d; // dist

	  vector<int> p(c);
	  vector<int> m(c);

	  for (j=0; j<c; j++) {
	       cin >> p.at(j);
	       cin >> m.at(j);
	  }

	  double x = solve( d, p, m);

	  cout << "Case #" << i << ": ";
	  
	  cout << setprecision(10) << x << endl;
     }

     return 0;
}
