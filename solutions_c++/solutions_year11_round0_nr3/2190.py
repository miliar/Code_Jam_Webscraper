#include <cstdio>
#include <cstring>
#include <functional>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 10;

int x[MAXN];
int sum , xsum;
int n;

int caseNumber;


void read() {
        scanf ( "%d" , &n );
        xsum = sum = 0;

        for (int i = 1; i <= n; ++i) {
                scanf ( "%d" , x + i );
                sum += x[i];
                xsum ^= x[i];
        }
}


void solve() {
        if ( xsum != 0 ) {
                printf ( "Case #%d: NO\n" , ++caseNumber );
                return;
        }
        printf ( "Case #%d: %d\n" , ++caseNumber , sum - *min_element ( x + 1 , x + n + 1 ) );
}

int main() {
        int t;
        scanf ( "%d" , &t );

        while ( t-- ) {

                read();
                solve();
        }

        return 0;
}
