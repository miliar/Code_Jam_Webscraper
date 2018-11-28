//
// Round 2  problem A
//
// Usually built with g++ 4.4.5 on Linux
// Sometimes uses GMP for big integers
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <algorithm>
// #include <gmpxx.h>

#include <cstdlib>
#include <math.h>

using namespace std;

struct wway {
     unsigned int b;
     unsigned int e;
     unsigned int w;

     wway( unsigned int b0, unsigned int e0, unsigned int w0) :
	  b(b0), e(e0), w(w0){}
};

bool operator <( const wway &w1, const wway &w2 )
{
     return w1.w < w2.w;
}

unsigned int solve( unsigned int L )
{
     return 0;
}

double solve( unsigned int x,
	      unsigned int s,
	      unsigned int r,
	      unsigned int t,
	      vector<wway> vv)
{
     cerr << "x = " << x << endl;
     cerr << "s = " << s << endl;
     cerr << "r = " << r << endl;

     unsigned int i;
     unsigned int d ;
     d=0;
     for (i=0; i<vv.size(); i++) {
	  d += vv.at(i).e - vv.at(i).b;
     }
     d = x-d;

     vv.push_back( wway(0,d,0) );

     sort(vv.begin(), vv.end());

     for (i=0; i<vv.size(); i++) {
	  cerr << setw(4) << vv.at(i).b << " ";
	  cerr << setw(4) << vv.at(i).e << " ";
	  cerr << setw(4) << vv.at(i).w << " ";
	  cerr << endl;
     }

     double tt = 0;
     double tr = 0;
     for (i=0; i<vv.size(); i++) {
	  wway ww = vv.at(i);
	  if (tr < t) {
	       double sr = ((double) ww.w + (double) + r);
	       double t1 = (ww.e-ww.b) / sr;
	       if (t1+tr <= t) {
		    cerr<< "Run for " << t1 << endl;
		    tr += t1;
		    tt += t1;
	       } else {
		    t1 = t-tr;
		    tr += t1;
		    tt += t1;

		    double dd = (ww.e-ww.b) - t1 * sr;
		    
		    double t2= (dd) / ((double) ww.w + (double) s);
		    tt += t2;
		    cerr << "Run for " << t1 << " and walk for " << t2 << endl;
	       }
	  } else {
	       double t2 = (ww.e-ww.b) / ((double) ww.w + (double) s);
	       cerr << "Walk for " << t2 << endl;
	       tt += t2;
	  }
     }

     return tt;
}

int main( int argc, char ** argv )
{
     unsigned int nn;
     unsigned int i,j;

     cin >> nn;

     for (i=1; i<=nn; i++) {
	  
	  unsigned int x,s,r,t,n;
	  cin >> x;
	  cin >> s;
	  cin >> r;
	  cin >> t;
	  cin >> n;
	  
	  vector<wway> vv;
	  for (j=0; j<n; j++) {
	       unsigned int b,e,w;
	       cin >> b;
	       cin >> e;
	       cin >> w;
	       wway ww(b,e,w);
	       vv.push_back(ww);
	  }

	  double tt = solve( x,s,r,t,vv);

	  cout << "Case #" << i << ": ";
	  cout << setprecision(12) ;
	  cout << setw(20) ;
	  cout << tt;

	  cout << endl;
     }

     return 0;
}
