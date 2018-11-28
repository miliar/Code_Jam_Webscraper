#include <cstdio>
#include <algorithm>

using namespace std;
int fr[1001];
int main(){
    
    int n, p, k, l;
    
    freopen("d:/gcj-a.txt", "w", stdout);
    
    scanf("%d", &n);
    
    for ( int tt = 1; tt <= n; ++tt ){
        scanf("%d %d %d", &p, &k, &l);
        for ( int i = 0; i < l; ++i )
            scanf("%d", &fr[i]);
        sort( fr, fr + l );
        
        int kp = 0, mul = 1, ans = 0;
        for ( int i = l - 1; i >= 0; --i ){
            if ( kp == k ) { kp = 0; mul++; };
            ans += mul * fr[i];
            kp++;
        }
        printf("Case #%d: %d\n", tt, ans);
        
    }
    
}
