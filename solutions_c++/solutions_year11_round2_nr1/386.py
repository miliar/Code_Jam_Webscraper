//
// Round 1b  problem A
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

vector<double> solve( vector<string> v )
{
     unsigned int n = v.size();
     unsigned int i,j,k;

     vector<double> wp(v.size());
     vector<double> owp(v.size());
     vector<double> oowp(v.size());
     vector<double> rpi(v.size());

     for (i=0; i<n; i++) {
	  unsigned int w=0;
	  unsigned int p=0;
	  for (j=0; j<n; j++) {
	       if (v.at(i)[j] == '0') {
		    p++;
	       } else if (v.at(i)[j] == '1') {
		    p++; w++;
	       }
	  }
	  wp.at(i) = (double) w / double (p);
     }

     for (i=0; i<n; i++) {
	  unsigned int np=0;
	  for (j=0; j<n; j++) {
	       if (v.at(i)[j] != '.') {
		    unsigned int w=0;
		    unsigned int p=0;
		    for (k=0; k<n; k++) {
			 if (k==i) {
			 }
			 else if (v.at(j)[k] == '0') {
			      p++;
			 } else if (v.at(j)[k] == '1') {
			      p++; w++;
			 }
		    }
		    owp.at(i) += (double) w / (double) p;
		    np++;
	       }

	  }
	  owp.at(i) /= np;
     }

     for (i=0; i<n; i++) {
	  unsigned int np=0;
	  for (j=0; j<n; j++) {
	       if (v.at(i)[j] != '.') {
		    np++;
		    oowp.at(i) += owp.at(j);
	       }
	  }
	  
	  oowp.at(i) /= np;
     }

     for (i=0; i<n; i++) {
	  rpi.at(i) = 0.25 * wp.at(i) + 0.5 * owp.at(i) + 0.25 * oowp.at(i) ;
     }
     
     return rpi;
}

int main( int argc, char ** argv )
{
     unsigned int nn;
     unsigned int i,j;
     unsigned int r ;
     string s;

     cin >> nn;

     for (i=1; i<=nn; i++) {
	  
	  cin >> r;

	  vector<string> v;
	  for (j=0; j<r; j++) {
	       cin >> s;
	       v.push_back(s);
	  }

	  vector<double> vv = solve(v);

	  cout << "Case #" << i << ":" << endl;

	  for (j=0; j<r; j++) {
	       cout << setprecision(10) << vv.at(j) << endl;
	  }
     }

     return 0;
}
