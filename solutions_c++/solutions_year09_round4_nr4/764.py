#include <stdio.h>
#include <math.h>

int n ;
double x[3], y[3], r[3] ;


double dual_r(int ex){
    int ind[2] ;
    int i, j ;
    
    i = 0 ;
    for( j=0 ; j<3 ; j++ ){
        if( j == ex )
            continue ;
        ind[i++] = j ;
    }
    
    double dx = x[ind[0]] - x[ind[1]] ;
    double dy = y[ind[0]] - y[ind[1]] ;
    return (sqrt(dx*dx+dy*dy) + r[ind[0]] + r[ind[1]])/2 ;
}


int main(void){
    int T ;
    
    scanf("%d", &T) ;
    for( int i_cases=1 ; i_cases<=T ; i_cases++ ){
        scanf("%d", &n) ;
        for( int i=0 ; i<n ; i++ )
            scanf("%lf%lf%lf", &x[i], &y[i], &r[i]) ;
            
        if( n==1 ){
            printf("Case #%d: %f\n", i_cases, r[0]) ;
            continue ;            
        }
        
        if( n == 2 ){
            if( r[0] > r[1] )
                printf("Case #%d: %f\n", i_cases, r[0]) ;
            else
                printf("Case #%d: %f\n", i_cases, r[1]) ;
            continue ;
        }
        
        double ans = 999999999 ;
        for( int i=0 ; i<3 ; i++ ){
            double dual = dual_r(i) ;
            double _ans = r[i] ;
            if( _ans < dual )
                _ans = dual ;
                
            if( ans > _ans )
                ans = _ans ;
        }
        printf("Case #%d: %f\n", i_cases, ans ) ;
    }
    
    
    return 0 ;
}

