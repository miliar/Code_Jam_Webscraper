#include <iostream>
using namespace std;

int main() {
 int t;
 cin >> t;
 for (int i=0; i<t; i++) {
     int n,s,p,r;
     cin >> n >> s >> p;
     int conta = 0;
     for (int j=0; j<n; j++) {
         cin >> r;
         if (r == 1) {
            if (p<=1) conta++;      
         }
         else if (r == 0) {
              if (p == 0) conta++;     
         }
         else {
         if (r/3 >= p) conta++;
         else {
              int min,max;
              if (r%3 == 0) {min = r/3; max = r/3 + 1;}
              else if (r%3 == 1) {min = r/3 + 1; max = r/3 + 1;}
              else {min = r/3+1; max = r/3 + 2;}
              
              if (min >= p) conta++;
              else if (max >= p and s>0) { conta++; s--;}              
         }
         } 
     }
     cout << "Case #" << i+1 << ": " << conta << endl;   
 }   
}
