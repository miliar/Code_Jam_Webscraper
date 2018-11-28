#include <iostream.h>
#include <vector>

using namespace std;

long long sumap(long long a, long long b) { return (a|b)&(~(a&b)); }

long long f(vector<int> c){
   long long max = -1; long long mask = 1;
   int n=c.size();
   for(int i=1; i<(2<<(n-1))-1; i++){
      long long ps=0, pp=0;
      for(int j=0; j<n; j++){
         if( i&(mask<<j) ) pp=sumap(pp, c[j]);
         else ps=sumap(ps, c[j]);
      }
      if (ps==pp){
         long long ss=0;
         for(int j=0; j<n; j++) if( !(i&(mask<<j)) ) ss+=c[j];
         if(ss>max) max=ss;         
      }        
   }
   return max;
}

int main(){
    int t, ci, n;
    cin >> t;
    vector<int> c;  
    for(int i=0; i<t; i++){
       cin >> n;
       c.clear();
       for(int j=0; j<n; j++){
          cin >> ci; 
          c.push_back(ci);
       }
       long long r = f(c);
       if( r == -1 )  printf("Case #%d: NO\n", i+1);
       else printf("Case #%d: %lld\n", i+1, r);
    }
}
