#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

    int a[5000];
    int n, s, p;
    
    int maxi[50];
    int maxi2[50];
    int TESTN = 1;
    
void solve () {

    int ans = 0;
    
    scanf("%d%d%d", &n, &s, &p);
    for ( int i = 0; i < n; ++i )
        scanf("%d", &a[i]);
    
    sort ( a, a + n );
    
    if ( s > 0 )
    for ( int i = 0; i < n; ++i ) {
        
        if ( maxi2[a[i]] >= p ) {ans++; s--; a[i] = -1; if ( s == 0 ) break;}
    }
    
    if ( s > 0 ) {
    for ( int i = 0; i < n; ++i )
        if ( a[i] != -1 && maxi2[a[i]] >= p ) {
        
          s--;
          a[i] = -1;
          if ( s == 0 ) break;
        }
    }
    
    for ( int i = 0; i < n; ++i )
        if ( a[i] != -1 && maxi[ a[i] ] >= p ) ans++;
        
    printf("Case #%d: %d\n",TESTN, ans);
    TESTN++;
}
int main() {
    
    memset( maxi, -1, sizeof(maxi));
    memset( maxi2 , -1, sizeof(maxi2));
    
    for ( int sum = 0; sum <= 30; ++sum )
    for ( int x = 0; x <= 10; ++x )
            for ( int y = x; y <= x + 2 && y <= 10 ; ++y )
                for ( int z = y; z <= x + 2 && z <= 10; ++z ) {
                    if ( x + y + z != sum ) continue;
                    
                    if ( z - x < 2 ) maxi[sum] = max( maxi[sum], z );
                    
                    if ( z - x == 2 ) maxi2[sum] = max ( maxi2[sum], z );
                }
                
    int t;
    cin>>t;
    
    for ( int i = 0; i < t; ++i ) {
    
        solve();
        
    }
    return 0;
}
