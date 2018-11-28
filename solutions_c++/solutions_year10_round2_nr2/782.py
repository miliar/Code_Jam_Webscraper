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
    bool imp=false;
    int n, k, b, t;
    in >> n >> k >> b >> t;
    int pos[n]; int v[n];

    for (int i=0; i<n; i++) {
      in >> pos[i];
    }

    for (int i=0; i<n; i++) {
      in >> v[i];
    }

    int cpt=0;
    int kk=0;
    int i;
    for (i=n-1; i>=0 && kk<k; i--) {
      if ((b-pos[i])<=t*v[i]) {
	
	if (n-kk-1>i)
	  cpt+=n-kk-1-i;
	kk++;
      }
      
    }


    if (kk<k)
      out << "Case #" << test+1 << ": IMPOSSIBLE" << endl;
    else 
      out << "Case #" << test+1 << ": " << cpt << endl;

//     int cpt=0;
//     for (int i=n-1; i>=0 && i>=n-k; i--) {

//       if ((b-pos[i])<=t*v[i]) {
// 	continue;
//       }

//       bool tr=false;
//       for(int j=i-1; j>=0; j--) {
       
// 	if ((b-pos[j])<=t*v[j]) {
	  
// 	  cpt+=i-j;
// 	  int vv=v[i]; int p=pos[i];
// 	  v[i]=v[j]; pos[i]=pos[j];

// 	  for (int k=i-1; k>=j; k--) {
// 	    int vv2=v[k]; int p2=pos[k];
// 	    v[k]=vv; pos[k]=p;
// 	    vv=vv2; p2=p;
// 	  }
// // 	  for(int k=0; k<n; k++) {
// // 	    cout << v[k] << " ";
// // 	  }
// // 	  cout << endl;
	    
// 	  tr=true;
// 	  break;
// 	}
//       }
//       if (!tr) {	
// 	imp=true;
// 	break;
//       }
      
//     }

//     if (imp)
//       out << "Case #" << test+1 << ": IMPOSSIBLE" << endl;
//     else 
//       out << "Case #" << test+1 << ": " << cpt << endl;
    
  }
}

