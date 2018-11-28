#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for ( int i = 0; i < n; i++ ) {
        int N, S, p;
        cin >> N >> S >> p;
        int a[50] = {0};
        for ( int j = 0; j < N; j++ ) {
            int x;
            cin >> x;
            a[x]++;
        }
        int ans = 0;
        for ( int j = max(p*3-2,0); j <= 30; j++ ) {
            ans += a[j];
        }
        if ( p > 1 ) {
            ans += min( S, a[p*3-3]+a[p*3-4] );
        }
        printf( "Case #%d: %d\n", i+1, ans );
    }
    return 0;
}