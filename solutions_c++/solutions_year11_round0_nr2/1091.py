//
// Qualification round 2011  problem B
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

string solve(void)
{
     unsigned int i,j,k;
     unsigned int c,d ;
     unsigned int n;
     string s;

     cin >> c;

     vector<string> v(c);

     for (i=0; i<c; i++) {
	  cin >> v[i];
     }

     cin >> d;

     vector<string> w(d);
     for (i=0; i<d; i++) {
	  cin >> w[i];
     }

     cin >> n;
     cin >> s;

     if (n != s.size()) {
	  cerr << "ERROR s.size() = " << s.size() << " != " ;
	  cerr << n << " = n" << endl;
	  exit(1);
     }

     string a;
     for (i=0; i<s.size(); i++) {
	  
	  char c2= s[i];

	  if (a.size() > 0)
	  {
	       // test whether the last two elements combine
	       char c1 = a[a.size()-1];
	       bool combined=false;
	       for (j=0; j<c; j++) {
		    if ( (c1 == v[j][0] && c2 == v[j][1]) ||
			 (c2 == v[j][0] && c1 == v[j][1]) ) {

			 a = a.substr(0,a.size()-1);
			 a += v[j][2];
			 combined=true;
			 break;
		    }
	       }
	       bool wiped = false;
	       if (!combined) {
		    for (j=0; j<d && !wiped; j++) {
			 for (k=0; k<a.size() && !wiped; k++) {
			      if ( (a[k] == w[j][0] && c2 == w[j][1]) ||
				   (c2 == w[j][0] && a[k] == w[j][1]) ) {
				   
				   a = "";
				   wiped = true;
			      }
			 }
		    }
	       } 

	       if (!wiped && !combined) {
		    a.push_back(c2);
	       }
	  }
	  else
	  {
	       a.push_back(c2);
	  }
     }

     return a;
}

int main( int argc, char ** argv )
{
     unsigned int n;
     unsigned int i,j;
     string s;

     cin >> n;

     for (i=1; i<=n; i++) {
	  
	  // cin >> a >> b >> c ;
	  s = solve();

	  cout << "Case #" << i << ": ";
	  cout << "[";
	  for (j=0; j<s.size(); j++) {
	       if (j) {
		    cout << ", ";
	       }
	       cout << s[j];
	  }
	  cout << "]";
	  cout << endl;
     }

     return 0;
}
