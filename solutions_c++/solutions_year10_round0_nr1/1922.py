#include <stdio.h>
#include <iostream>
#include <string>

#define FOR(a,b,c) for ( int a = b ; a < c ; a++ )

using namespace std;

typedef unsigned long long ULL;

ULL n,k;

//Rapida potencia
template< class Int>
Int fastPow( Int a , int b){
    if ( b == 1 ) return a;
    if ( b&1 ) return a*fastPow(a,b-1);
    return fastPow(a*a,b/2);
}

string binario(ULL n){
   if (n == 1) return "1";
   if (n == 0) return "0";
   return binario(n/2).append(binario(n%2));
}

bool isOn(){
   ULL ans,moduled;
   ans = fastPow<ULL>((ULL)2,n);
   moduled = k%ans;
   string bin = binario(moduled);
   if (bin.size() != n) return 0;
   FOR(i,0,bin.size()){
      if (bin[i] != '1')
         return 0;
   }
   return 1;
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,1,casos+1){
      cin >> n >> k;
      printf("Case #%d: %s\n",caso,isOn()?"ON":"OFF");
   }
   fflush(stdout);
   return 0;
}

