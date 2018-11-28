// GCJ2008 - Round 2
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
#define FE(i,n) for(i=n-1;i>=0;i--)
int i, j, k;
# define MAX 1000

int main () {
   int cases, ct; cin >> cases;
   F1(ct, cases) {

      int p, k, l, t;
      long long sum;
      int fr[MAX];
      cin >> p >> k >> l;
      F0(i, l) cin >> fr[i];
      sort(fr, fr+l);
      for(i=0, t=l-1, sum=0;i<p && t>=0;i++) {
         for(j=0; j<k && t>=0; j++, t--) {
         sum+=fr[t]*(i+1);
         }
      }
              
      //FE(i, l) cout << " " << fr[i];
      cout << "Case #" << ct << ": " << sum << endl;
   }
   return 0;
}
