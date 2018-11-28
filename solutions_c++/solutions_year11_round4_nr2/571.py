//
// Round 2  problem B
//
// Usually built with g++ 4.4.5 on Linux
// Sometimes uses GMP for big integers
//
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
// #include <gmpxx.h>
#include <algorithm>

#include <cstdlib>
#include <math.h>

using namespace std;

void add_square( int &sx, int &sy,
		 int dx, int dy,
		 int w )
{
     //cerr << "Add square - dx " << setw(3) << dx ;
     //cerr << "  dy " << setw(3) << dy << "   ";
     //cerr << "  w = " << setw(2) << w << "   ";

     sx += dx * w;
     sy += dy * w;

     //cerr << "   sx = " << setw(3) << sx << "   ";
     //cerr << "   sy = " << setw(3) << sy << endl;
}

unsigned int find_biggest0( int r, int c, 
			    vector< vector< unsigned int> > &vv,
			    int x, int y)
{
     // offset center
     unsigned int ss=0;
     int sx;
     int sy;
     int u;
     int k;

     sx = 0;
     sy = 0;

     int k_max ;

     k_max = 10000000;
     k_max = min(k_max, x);
     k_max = min(k_max, r-x-1-1);
     k_max = min(k_max, y);
     k_max = min(k_max, c-y-1-1);

     for (k=1; k<=k_max; k++) 
     {
	  add_square( sx, sy, -(2*k-1), -(2*k-1), vv[x-(k-1)].at(y-(k-1)) );
	  add_square( sx, sy, -(2*k-1),  (2*k-1), vv[x-(k-1)].at(y+k) );
	  add_square( sx, sy,  (2*k-1), -(2*k-1), vv[x+k].at(y-(k-1)) );
	  add_square( sx, sy,  (2*k-1),  (2*k-1), vv[x+k].at(y+k) );

	  for (u=-k+1; u<=k; u++) {
	       add_square( sx, sy, -(2*k+1),  (2*u-1), vv[x-k]  [y+u] );
	       add_square( sx, sy,  (2*u-1), -(2*k+1), vv[x+u]  [y-k] );
	       add_square( sx, sy,  (2*k+1),  (2*u-1), vv[x+k+1][y+u] );
	       add_square( sx, sy,  (2*u-1),  (2*k+1), vv[x+u]  [y+k+1] );
	  }

	  //cerr << "sx= " << sx << "   " << " sy = " << sy << endl;
	  if (sx == 0 && sy == 0) ss = k;
     }

     if (ss==0) return 0;
     return 2*ss+2;
}

unsigned int find_biggest1( int r, int c, 
			    vector< vector< unsigned int> > &vv,
			    int x, int y)
{
     //cerr << "find_biggest1" << endl;
     // center center
     unsigned int ss=0;
     int sx;
     int sy;
     int u;
     int k;

     sx = 0;
     sy = 0;

     int k_max ;

     // checked
     k_max = std::min(x,r-x-1);
     k_max = min(k_max, y);
     k_max = min(k_max, c-y-1);

     //cerr << "k_max = " << k_max << endl;
     for (k=1; k<=k_max; k++) 
     {
	  //cerr << "k = " << k << " of " << k_max << endl;
	  //cerr << "x-(k-1) = " << x-(k-1) << endl;
	  //cerr << "y-(k-1) = " << y-(k-1) << endl;
	  //cerr << "x+k = " << x+k << endl;
	  //cerr << "y+k = " << y+k << endl;

	  add_square( sx, sy, -(k-1), -(k-1), vv[x-(k-1)][y-(k-1)] );
	  add_square( sx, sy, -(k-1),  (k-1), vv[x-(k-1)][y+(k-1)] );
	  add_square( sx, sy,  (k-1), -(k-1), vv[x+(k-1)][y-(k-1)] );
	  add_square( sx, sy,  (k-1),  (k-1), vv[x+(k-1)][y+(k-1)] );
	  //cerr << "---" << endl;
	  for (u=-k+1; u<=k-1; u++) {
	       add_square( sx, sy, -(k),  (u), vv[x-k]  [y+u] );
	       add_square( sx, sy,  (u), -(k), vv[x+u]  [y-k] );
	       add_square( sx, sy,  (k),  (u), vv[x+k]  [y+u] );
	       add_square( sx, sy,  (u),  (k), vv[x+u]  [y+k] );
	  }

	  //cerr << "sx= " << sx << "   " << " sy = " << sy << endl;
	  if (sx == 0 && sy == 0) ss = k;
     }

     //cerr << "ss = " << ss << endl;
     if (ss==0) return 0;
     return 2*ss+1;
}

int solve( int r, int c, 
		    vector< vector< unsigned int> > &vv)
{
     //return find_biggest1( r,c,vv,3,3 );

     int s0 = 0 ;
     int s;

     int i,j;
     // odds
     for (i=0; i<r; i++) {
	  for (j=0; j<c; j++) {
	       s = find_biggest0( r, c, vv, i, j );
	       s0 = max(s,s0);
	  }
     }

     for (i=0; i<r; i++) {
	  for (j=0; j<c; j++) {
	       s = find_biggest1( r, c, vv, i, j );
	       s0 = max(s,s0);
	  }
     }

     // evens
     return s0;



}

int main( int argc, char ** argv )
{
     unsigned int nn;
     unsigned int i,j,k;

     unsigned int r;
     unsigned int c;
     unsigned int d;
     string s;

     cin >> nn;

     for (i=1; i<=nn; i++) {
	  
	  cin >> r;
	  cin >> c;
	  cin >> d;

	  vector<vector<unsigned int> > ww(r);
	  for (j=0; j<r; j++) {
	       ww.at(j).resize(c);
	       cin >> s;
	       for (k=0; k<c; k++) {
		    ww.at(j).at(k) = s[k] - '0';
	       }
	  }
	  unsigned int x = solve(r,c,ww);

	  cout << "Case #" << i << ": ";
	  if (x == 0) cout << "IMPOSSIBLE" ;
	  else cout << x;

	  cout << endl;
     }

     return 0;
}
