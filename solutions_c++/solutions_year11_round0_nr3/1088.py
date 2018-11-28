//
// Qualification round 2011  problem C
//
// Usually built with g++ 4.4.5 on Linux
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

int main( int argc, char ** argv )
{
     unsigned int n;
     unsigned int i,j;
     unsigned int r;

     cin >> n;

     for (i=1; i<=n; i++) {
	  
	  cin >> r;
	  vector<unsigned int> v(r);

	  for (j=0; j<r; j++) {
	       cin >> v[j];
	  }

	  unsigned int m=v[0];
	  unsigned int s=0;
	  unsigned int sx=0;
	  for (j=0;j<r; j++) {
	       s += v[j];
	       sx ^= v[j];
	       m = min(m,v[j]);
	  }

	  cout << "Case #" << i << ": ";
	  if (sx == 0) {
	       cout << s - m << endl;
	  }
	  else {
	       cout << "NO" << endl;
	  }
     }

     return 0;
}
