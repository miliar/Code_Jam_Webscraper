#include <cstdlib>
#include <iostream>
#include <bitset>
using namespace std;

int main(void) {
   int n ;
   cin >> n;
   char c ;
   for ( int j = 1 ; j <= n ; j++) {
   unsigned int x = 0;
   unsigned int o = 0;
   for (int i = 0 ; i < 16 ; i++) {
      cin >> c ; 
      x <<= 1 ;
      o <<= 1 ;
      x += ( c == 'X' ? 1 : 0) ;
      o += ( c == 'O' ? 1 : 0) ;
      x += ( c == 'T' ? 1 : 0) ;
      o += ( c == 'T' ? 1 : 0) ;
      //cout << c << endl ;
   }
    /*bitset<16> y(x);
    bitset<16> z(o);
    cout << y << endl;
    cout << z << endl; */
    bool found = false;
    unsigned int x3 = 0x0000000F ;
    unsigned int x4 = 0x0000000F ;
    unsigned int diag1 = 0x00008421 ;
    unsigned int diag2 = 0x00001248 ; 
    if (((x & diag1) == diag1) || ((x & diag2) == diag2)) {
           cout << "Case #" << j << ": X won" << endl;
           continue ;
    }
    if (((o & diag1) == diag1) || ((o & diag2) == diag2)) {
           cout << "Case #" << j << ": O won" << endl;
           continue ;
    }
    unsigned int xx = x;
    unsigned int oo = o;
    for (int i = 0; i < 4; i++ ) {
       if (found) { break ; }
       unsigned int x1 = x & 0x000000F;
       //bitset<16> test(x1);
       //cout << "  " << test  << endl;
       unsigned int x2 = o & 0x000000F;
       //bitset<16> test2(x2);
       //cout << "  " << test2  << endl;
       x3 &= x1 ;
       x4 &= x2 ;
       x >>= 4;
       o >>= 4;
       if (x1 == 0x0000000F) {
           cout << "Case #" << j << ": X won" << endl;
           found = true ;
           break ;
       }
       if (x2 == 0x0000000F) {
           cout << "Case #" << j << ": O won" << endl;
           found = true ;
           break ;
       }
    }
    if (!found) {
       if (x3 > 0) {
           cout << "Case #" << j << ": X won" << endl;
           found = true ;
       }
       if (x4 > 0) {
           cout << "Case #" << j << ": O won" << endl;
           found = true ;
       }
    }
    
    if (!found) {
       if ((xx | oo) == 0x0000FFFF) {
       cout << "Case #" << j << ": Draw" << endl;    
       } else {
       cout << "Case #" << j << ": Game has not completed" << endl; 
       }
    }
   }
   //cout << "test" << endl;
   return 0;
}
