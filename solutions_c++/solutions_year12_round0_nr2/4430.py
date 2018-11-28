#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int test, test1, i, j, s, p, x, res, a, b, c, n, k;
    cin >> test1;
    
    for ( test = 1; test <= test1; test ++ ) {
        cin >> n >> s >> p;
        res = 0;
        
        for ( i = 1; i <= n; i ++ ) {
            cin >> x;
            j = x / 3;
            k = x % 3;
            a = j;
            b = j;
            c = j;
            
            if ( s > 0 ) {
                 if ( k == 0 ) {
                      if ( j >= p ) {
                           res ++;
                      } else
                      if ( ( j - 1 >= 0 ) && ( j + 1 >= p ) ) {
                           s --;
                           res ++;
                      }
                 }
                 if ( k == 1 ) {
                      if ( j + 1 >= p ) {
                           res ++;
                      }
                 }
                 if ( k == 2 ) {
                      if ( j + 1 >= p ) {
                           res ++;
                      } else
                      if ( j + 2 >= p ) {
                           res ++;
                           s --;
                      }
                 }
            } else {
                 if ( k == 0 ) {
                      if ( j >= p ) {
                           res ++;
                      }
                 }
                 if ( k == 1 ) {
                      if ( j + 1 >= p ) {
                           res ++;
                      }
                 }
                 if ( k == 2 ) {
                      if ( j + 1 >= p ) {
                           res ++;
                      }
                 }
            }
        }
        
        cout << "Case #" << test << ": " << res << "\n";
    }
    
    return 0;
}
    
