#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <assert.h>
#include <bitset>
#include <functional>
#include <utility>
#include <iomanip>
#include <cctype>
#include <gmp.h>
#include <gmpxx.h>
//#include <ext/hash_set>
//#include <ext/hash_map>

using namespace std;
// using namespace __gnu_cxx;


typedef unsigned long long int ll;
//typedef mpz_class mpz; // compilationg++ truc.cpp -lgmpxx -lgmp



int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    int n, k;
    in >> n >> k;
    
    char t[n][n];
    for (int i=0; i<n; i++) {
      for (int j=0; j<n; j++) {
	in >> t[i][j];
      }
    }

    for(int i=0; i<n; i++) {
      int k1=n-1;
      for(int j=n-1; j>=0; j--) {
	if (t[i][j]!='.') {
	  t[i][k1]=t[i][j];
	  if(j<k1) t[i][j]='.';
	  k1--;
	}	
      }
    }

//     for (int i=0; i<n; i++) {
//       for (int j=0; j<n; j++) {
// 	cout << t[i][j] << " ";
//       }
//       cout << endl;
//     }
    bool blue=false;
    bool red=false;

    for (int i=0; i<n; i++) {
      char c='.';
      int cpt=0;
      for (int j=0; j<n; j++) {
	//if (i==5) cout << "cpt : " << cpt << endl;
	if (t[i][j]==c && c!='.') {
	  cpt++;
	}
	else {
	  c=t[i][j];
	  cpt=1;
	}
	if (cpt>=k && c=='B') {blue=true; break;}
	if (cpt>=k && c=='R') {red=true; break;}
      }
    }

    for (int j=0; j<n; j++) {
      char c='.';
      int cpt=0;
      for (int i=0; i<n; i++) {
	if (t[i][j]==c && c!='.') {
	  cpt++;
	}
	else {
	  c=t[i][j];
	  cpt=1;
	}
	if (cpt>=k && c=='B') {blue=true; break;}
	if (cpt>=k && c=='R') {red=true; break;}
      }
    }

    bool no=false;

    for(int i=0; i<n; i++) {
      for (int j=0; j<n; j++) {
	no=false;
	for (int p=0; p<k; p++) {
	  if(i+p<n && j+p<n) {
	    if (t[i+p][j+p]!=t[i][j]) {
	      no=true;
	      break;
	    }
	  }
	}
	if ((!no) && i+k-1<n && j+k-1<n) {
	  if(t[i][j]=='B') blue=true;
	  if(t[i][j]=='R') red=true;
	}
	
      }
    }

    
    no=false;

    for(int i=0; i<n; i++) {
      for (int j=0; j<n; j++) {
	no=false;
	for (int p=0; p<k; p++) {
	  
	  if(i+p<n && j-p>=0) {
	    

	    if (t[i+p][j-p]!=t[i][j]) {
	      
	      no = true;
	      break;
	    }
	    
	  }
	}

	
	if((!no) && i+k-1<n && j-k+1>=0) {
	    
	  if(t[i][j]=='B') blue=true;
	  if(t[i][j]=='R') red=true;
	}
	
      }
    }

    if (red && blue)
      out << "Case #" << test+1 << ": Both" << endl;
    if (red && (!blue))
      out << "Case #" << test+1 << ": Red" << endl;
    if ((!red) && blue)
      out << "Case #" << test+1 << ": Blue" << endl;
    if ((!red) && (!blue))
      out << "Case #" << test+1 << ": Neither" << endl;
  }
}

