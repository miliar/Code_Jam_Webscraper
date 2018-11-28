/* 
 * File:   main.cpp
 * Author: Bill
 *
 * Created on 2009年9月13日, 下午6:14
 */

#include <stdlib.h>
#include <cstdio>
#include <cmath>

/*
 * 
 */


const int MaxN = 601 ;
int T ;
int N ;
int x[MaxN] , y[MaxN] , z[MaxN] , vx[MaxN] , vy[MaxN] , vz[MaxN] ;
double tx , ty , tz , kx , ky , kz ;

void solve(){
    scanf("%d",&N);
    tx = ty = tz = 0 ;
    kx = ky = kz = 0 ;
    for( int i = 0 ; i < N ; ++i ){
        scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
        tx += x[i] ;
        ty += y[i] ;
        tz += z[i] ;
        kx += vx[i] ;
        ky += vy[i] ;
        kz += vz[i] ;
    }
    tx /= N ;
    ty /= N ;
    tz /= N ;
    kx /= N ;
    ky /= N ;
    kz /= N ;
    /*
     *  xt = tx + kx*t
     *  yt = ty + ky*t
     *  zt = tz + kz*t
     *
     *  dis = sqrt(
     */

    double a = kx*kx + ky*ky + kz*kz ;
    double b = 2*(kx*tx+ky*ty+kz*tz) ;
    if( fabs(a) < 1e-7 ){
            double ans = 0 ;
            double xt = tx;
            double yt = ty;
            double zt = tz;
            double dis = sqrt( xt*xt + yt*yt + zt*zt );
            printf("%.10lf %.10lf\n",dis,ans);
            return ;
    }
    double ans = -b / 2 / a ;
    if( ans < 1e-7 ) ans = 0 ;
    double xt = tx + kx*ans ;
    double yt = ty + ky*ans ;
    double zt = tz + kz*ans ;
    double dis = sqrt( xt*xt + yt*yt + zt*zt );
    printf("%.10lf %.10lf\n",dis,ans);
}
int main(int argc, char** argv) {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

