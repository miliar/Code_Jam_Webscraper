#include<iostream>

using namespace std;

int main() {
   
   unsigned long  t, T;
   int n;
   unsigned long k;

   unsigned long value;

   cin >> T;
   
   for ( t = 0; t < T; t++) {
   
  
   cin >> n; 
   cin >> k;
   value = 1 << n;

   
    cout << "Case #" << t+1 << ": " ;
    if ( k%value == value -1) 
        cout << "ON" << endl;
    else
        cout << "OFF" << endl;
  }
}
 
   
