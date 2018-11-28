#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
int main() {
   int T;
   cin >> T;
   
   FOR(t,T) {
      int N, S, p;
      cin >> N;
      cin >> S;
      cin >> p;
      printf("Case #%d: ", t+1);
      int count = 0;
      
      FOR (i, N) {
         int n;
         cin >> n;
         if (n >= p && n/3 + 2 >= p) {
            switch(n%3) {
               case 0:
                  if (n/3 >= p) {
                     count++;
                  } else if (n/3 + 1 >= p && S > 0) {
                     count++;
                     S--;
                  }
                  break;
               case 1:
                  if (n/3 + 1 >= p) count++;
                  break;
               case 2:
                  if (n/3 + 1 >= p) {
                     count++;
                  } else if (S > 0 && n/3 + 2 >= p) {
                     count++;
                     S--;
                  }
                  break;
            }
         }
      }
      printf("%d\n", count);
   }
   return 0;
}

