//
// Qualification round 2011  problem D
//
// Usually built with g++ 4.4.5 on Linux
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <set>
#include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

const unsigned int N_MAX=1000;

vector<double> p(N_MAX+1);
vector<double> e(N_MAX+1);

vector<vector<double> > ps(N_MAX+1);

void setup( )
{
     unsigned int i,j;

     ps[0].resize(1);
     ps[0][0] = 1.0;
     for (i=1; i<=N_MAX; i++) {
	  ps[i].resize(i+1);
	  ps[i][0] = ps[i-1][0]/2;
	  ps[i][i] = ps[i][0];
	  for (j=1; j<i; j++) {
	       ps[i][j] = (ps[i-1][j-1]+ps[i-1][j])/2.0;
	  }
     }

     if (0) {
	  for (i=0; i<7; i++) {
	       for (j=0; j<=i; j++) {
		    cout << setprecision(5) << setw(9) << ps[i][j];
	       }
	       cout << endl;
	  }
     }

     p[0] = 1.0;
     p[1] = 0.0;

     for (i=2; i<=N_MAX; i++)
     {
	  double x = 1.0;
	  double f = 1.0 ;
	  //cout << "x = " << x << endl;
	  for (j=1; j<=i; j++) {
	       f /= j;
	       x -= p[i-j]*f;
	       //cout << "x -= " << p[i-j] << "*"<<f << endl;
	  }
	  //cout<< "p[" << i << "] = " << x << endl;
	  p[i] = x;
     }

     e[0] = 0.0;
     e[1] = 0.0;

     for (i=2; i<=N_MAX; i++) {
	  double x = 1.0;
	  double f = 1.0;
	  for (j=1; j<=i; j++) {
	       f /= j;	       
	       x += p[i-j]*e[i-j]*f;
	  }

	  x /= (1.0-p[i]);
	  e[i] = x;
     }

     if (0){
	  for (i=0; i<=1000; i++) {
	       cout << "p["<<i<<"] = " << setprecision(10) << setw(12) << p[i] ;
	       cout << "   ";
	       cout << "e["<<i<<"] = " << setprecision(7)  << setw(12) << e[i] << endl;
	  }
     }
}

int main( int argc, char ** argv )
{
     unsigned int n;
     unsigned int i,j;
     unsigned int r ;
     string w;

     setup();

     cin >> n;

     cerr << n << endl;

     for (i=1; i<=n; i++) {
	  
	  // cin >> a >> b >> c ;
	  cin >> r;
	  
	  vector<unsigned int> v(r);
	  vector<unsigned int> w(r);

	  for (j=0; j<r; j++) {
	       cin >> v[j];
	  }

	  w=v;
	  sort(w.begin(), w.end());

	  unsigned int t=0;
	  for (j=0; j<r; j++) {
	       if (w[j] != v[j]) t++;
	  }
 
	  cout << "Case #" << i << ": ";
	  cout << t << endl;
     }

     return 0;
}
