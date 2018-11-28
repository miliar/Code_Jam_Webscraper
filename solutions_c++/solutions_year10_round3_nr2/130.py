#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    
    //freopen("bl.in","r",stdin);
    //freopen("bl.txt","w",stdout);
    int i ,j, c, cas, rate;
    
    long long int a, b;
    scanf("%d", &cas);
    for( c=1; c<=cas; ++c ){
        cin >> a;
        cin >> b;
        cin >> rate;
        a *= rate;

        if( a >= b ){
            printf("Case #%d: 0\n", c);
            continue;
        }
        
        for( i=1; ; ++i,rate*=rate ){
            a *= rate;
            if( a>=b )
                break;
        }
        printf("Case #%d: %d\n", c, i);
    }
    
    return 0;
}
