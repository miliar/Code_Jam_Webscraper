#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std ;
int main(int argc, char *argv[]) {
   int R, k, N ;
   scanf("%d", &N) ;
   int kase = 0 ;
   while (scanf("%d %d %d", &R, &k, &N) == 3) {
     long long res = 0 ;
     vector<int> v ;
     vector<long long> triphit ;
     vector<long long> tripres ;
     int a ;
     long long s = 0 ;
     for (int i=0; i<N; i++) {
       scanf("%d", &a) ;
       s += a ;
       v.push_back(a) ;
       triphit.push_back(-1) ;
       tripres.push_back(-1) ;
     }
     int at = 0 ;
     int noloop = 1 ;
     for (long long trip=0; trip < R; ) {
       if (noloop && triphit[at] >= 0) {
	 // cycle
	 long long dur = trip - triphit[at] ;
	 long long more = (R - trip - 1) / dur ;
	 if (more > 0) {
	   res += (res - tripres[at]) * more ;
	   trip += more * (trip - triphit[at]) ;
	 }
	 noloop = 0 ;
       } else {
	 triphit[at] = trip ;
	 tripres[at] = res ;
	 int cap = k ;
	 for (int i=0; v[at] <= cap && i<N; i++) {
	   cap -= v[at] ;
	   res += v[at] ;
	   at = (at + 1) % N ;
	 }
	 trip++ ;
       }
     }
     cout << "Case #" << (++kase) << ": " << res << endl ;
   }
}
