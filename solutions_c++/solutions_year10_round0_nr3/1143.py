#include<iostream>

using namespace std;

const int MAXN = 1000;

unsigned long queue[MAXN];
int main() {
   
   int  t, T;
   unsigned long R, k, r ;
   int N, i, j;
   unsigned long total, partial;
   cin >> T;
   
   for ( t = 0; t < T; t++) {
   
       cin >> R; 
       cin >> k;
       cin >> N;

      for (i = 0; i < N; i++) 
           cin >> queue[i];

      total = 0; 
      i = 0;
      for ( r = 0; r < R; r++) {
       
         partial = 0;
         int norepition = 0;
         while  (partial + queue[i] <= k) {
                  partial += queue[i];
                  i = (i + 1)%N;
                  norepition++;
                  if(norepition == N)
                    break;
         }         

      total += partial;

      } 
     
      cout << "Case #" << t+1 << ": " << total << endl;; 
   }

}
