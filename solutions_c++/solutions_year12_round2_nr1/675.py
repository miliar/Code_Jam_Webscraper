#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())



int main()
{
  int i,j,k,l; char buf[1000];
  int keeses; scanf("%d",&keeses);

  for(int kees=1;kees<=keeses;kees++) {
   int n; scanf("%d",&n);
   vi J(n); int X=0; 
   for(j=0;j<n;j++) { scanf("%d",&J[j]); X+=J[j]; }
   vi S = J; sort(S.begin(),S.end());
   double dX=X;

   printf("Case #%d:",kees);
   for(j=0;j<n;j++) { 

     //printf(" %.8lf",100*max(0.0,2.0/n-(double(J[j])/X))); 
     double hi=1.0,lo=0.0;
     for(i=0;i<100;i++) {
       double ik = (hi+lo)/2.0;
       double nodig=ik;
       for(k=0;k<n;k++) if(k!=j) {
         double r = (J[j]+dX*ik-J[k])/dX;
         if(r>0) nodig+=r;
       }
       if(nodig>1.0) {
         hi=ik;
       } else {
         lo=ik;
       }
     }

     printf(" %.8lf",100*hi);
   }
   printf("\n");

  }



  return 0;
}
