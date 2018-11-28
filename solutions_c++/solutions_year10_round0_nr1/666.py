#include <cstdio>
#include <cstring>
#include <cstdlib>

int main() {
    int t, casN, N, K;
    
    scanf("%d", &t);
    for ( casN=1; casN<=t; casN++ ) {
        scanf("%d%d", &N, &K);
        printf("Case #%d: %s\n", casN, ( ( K & ( ( 1<<N ) - 1 ) ) == ( ( 1<<N ) - 1 ) ) ? "ON" : "OFF" );
    }

    //system("Pause");
    return 0;
}
