#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
    
    freopen("cbi.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, c=0, n, i, j, k;
    int in[1000];
    
    scanf("%d", &cas);
    while( cas-- ){
        
        scanf("%d", &n);
        for( i=0; i<n; ++i )
            scanf("%d", &in[i]);
        
        for( i=0,j=0; i<n; ++i )
            j ^= in[i];
        
        if( j ) printf("Case #%d: NO\n", ++c);
        else{
            sort(in,in+n);
            for( i=1,j=0; i<n; ++i )
                j += in[i];
            printf("Case #%d: %d\n", ++c, j);
        }
        
    }
    
    return 0;
}
