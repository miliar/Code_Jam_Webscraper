#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
    
    freopen("dbi.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, c=0, n, i, j, k;
    int in[1001];
    
    scanf("%d", &cas);
    while( cas-- ){
        
        scanf("%d", &n);
        for( i=1; i<=n; ++i )
            scanf("%d", &in[i]);
        
        for( i=1,j=0; i<=n; ++i )
        if( in[i]!=i )  ++j;
        
        printf("Case #%d: %d.000000\n", ++c, j);
        
    }
    
    return 0;
}
