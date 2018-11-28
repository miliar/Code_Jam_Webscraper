#include <iostream>
#include <algorithm>
using namespace std;

int a[2000],b[2000],n,t,i,j,k,res ;

int main()
{
    freopen("A-large.in","r",stdin) ; 
    freopen("a2.out","w",stdout) ; 
    cin >> t ;
    for ( int tt = 1 ; tt<=t ; ++tt ) {
        cin >> n ; 
        for ( i = 0 ; i < n ; ++i ) cin >> a[i] >> b[i] ; 
        
        res = 0 ; 
        for ( i = 0 ; i < n ; ++ i )
        for (j = 0 ; j < n ; ++j )
        if ( a[i] < a[j] && b[i] > b[j] ) 
        ++res ;
        
        printf("Case #%d: %d\n",tt , res) ;
        }       
    fclose(stdout);
}
