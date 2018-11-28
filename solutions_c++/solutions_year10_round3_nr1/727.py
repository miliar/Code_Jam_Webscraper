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

//////////////////////////////////////////////////////////////////////////////////////////////////

// Constantes
const double pi=acos(-1.0);
const double eps=1e-11;

// Divers
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T min(T &a,T b){if(a<=b) return a; else return b;}
template<class T> inline T max(T &a,T b){if(a>=b) return a; else return b;}
template<class T> inline void setMin(T &a,T b){if(b<a) a=b;}
template<class T> inline void setMax(T &a,T b){if(b>a) a=b;}
template<class T> inline void echange(T* t, int i, int j){T s = t[i]; t[i] = t[j]; t[j] = s;}

// Fonction de comparaison pour le tri
template<class T> inline bool comp(T a, T b) {return a>b;}
template<class T> inline bool comp_p(T a, T b) {return a.first<b.first;}
template<class T> inline bool comp_p_dec(T a, T b) {return a.first>b.first;}

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
    int n;
    in >> n;
    pair<int, int> t[1001];

    for (int i=0; i<n; i++) {
      int p, q;
      in >> p >> q;
      //pair<int, int> pe=make_pair(p,q);
      t[i].first=p;
      t[i].second=q;
    }
    
    sort(t, t+n, comp_p<pair<int, int> >);

    int cpt=0;
    
    for(int i=0; i<n; i++) {
      for (int j=i; j<n; j++) {
	if(t[i].second>t[j].second)
	  cpt++;
      }
    }
    
    out << "Case #" << test+1 << ": " << cpt << endl;
    
  }
}

