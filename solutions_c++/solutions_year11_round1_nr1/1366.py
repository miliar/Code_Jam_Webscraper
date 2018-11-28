#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

int N, PD, PG;

int gcd(int m, int n)     	// function definition
{                         	// block begin
   int  r;                	// declaration of remainder

   while (n != 0) {       	// not equal
      r = m % n;          	// modulus operator
      m = n;              	// assignment
      n = r;
   }                      	// end while loop
   return m;              	// exit gcd with value m
}

std::string compute() {
  if (PG==100 && PD!=100)
    return "Broken";
  if (PG==0 && PD!=0)
    return "Broken";
  int g=gcd(100,PD);
  int d = 100 / g;
  assert(g*d == 100);
  if (d>N)
    return "Broken";
  return "Possible";
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin>>N>>PD>>PG;

    cout<<"Case #"<<Ti<<": "<<compute()<<endl;
  }
}
