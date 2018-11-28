#include<iostream>
#include<cmath>
using namespace std;

int n, temp, t, s, p;

int main() {
    cin >> n;

    for( int cas = 1; cas <= n; cas++ ) {
         cin >> t >> s >> p;
         int r = 0;
         for( int i = 0; i < t; i++ ) {
             cin >> temp;
             if( temp > ( p - 1 ) * 3 ) {
                 r++;
             } else if( temp > max( ( p * 3 ) - 5, 0 ) ) {
                 if( s > 0 ) {
                     r++;
                     s--;
                 }
             }
         }
         cout << "Case #" << cas << ": " << r << endl;
    }    


    return 0;
}
