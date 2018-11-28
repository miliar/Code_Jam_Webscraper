#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,n) for(int i=0, _n = n; i < _n; i++) 

int main () {
    int numtest, count = 0;
    cin >> numtest;
    while (count++ < numtest) {
          int ans = 0, u = 0; // ans = dap an, u = so ngac nhien da phan phat
          int n, t, p;
          cin >> n >> t >> p;
          REP(i,n) {
               int sum;    
               cin >> sum;
               if (sum <= 3) {
                   if (p == 0) { ans ++; continue; }
                   if (p == 1 && sum > 0) { ans ++; continue; }
                   if (u == t) continue;
                   if (p == 2 && sum >= 2) {
                         ans ++;
                         u++;
                   }
                   continue;                   
               } 
               
               if ((sum+2)/3 >= p) {ans++; continue; }
               if (u == t) continue;
               if ((sum+4)/3 >= p ) {
                   ans++;
                   u++;         
               }    
          }
          cout << "Case #" << count << ": " << ans << endl;
    }
    //system ("pause");
    return 0;
}
