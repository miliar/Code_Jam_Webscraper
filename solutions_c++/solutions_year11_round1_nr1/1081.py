#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    
    freopen("ABigin.in", "r", stdin);
    freopen("ABigout.txt", "w", stdout);
    
    int i, j, pd, pg, cas, c=0, tmp;
    long long int n;
    
    scanf("%d", &cas);
    while( cas-- ){
        
        
        cin >> n ;
        cin >> pd;
        cin >> pg;
        //cout<< n << pd << pg << endl;
        //printf("%lld %d %d\n", n, pd, pg);
        
        
        if( pd==0 && pg<99 )        printf("Case #%d: Possible\n", ++c);
        else if( pd==0 && pg==100 )   printf("Case #%d: Broken\n", ++c);
        else if( pd!=0 && pg==0 )   printf("Case #%d: Broken\n", ++c);
        else{
            
            i = pd;
            tmp = 1;
            while( i%100!=0 ){
                i += pd;
                ++tmp;
            }
            //printf("%d\n", tmp);
            if( n<tmp   )    printf("Case #%d: Broken\n", ++c);
            else if( pd!=100 && pg==100 )   printf("Case #%d: Broken\n", ++c);
            else    printf("Case #%d: Possible\n", ++c);
            
        }
        
    }
    
    return 0;
}
