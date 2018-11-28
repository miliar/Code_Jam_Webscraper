#include<iostream>
#include<cmath>
#define EPS 10-7
using namespace std;
__int64 point[501][7];
__int64 a, b, c, d, e, f;

int main(){
    int t, i, j, cas;
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf("%d",&t);
    for( cas = 1; cas <= t; cas++ ){
        int n;
        scanf("%d",&n);
        for( i = 1; i <= n; i++ )
        for( j = 1; j <= 6; j++ )
        scanf( "%I64d", &point[i][j] );
        a = 0; b = 0; c = 0;
        d = 0; e = 0; f = 0;
        for( i = 1; i <= n; i++ ){
            b+=point[i][4];a+=point[i][1];c+=point[i][2];
            d+=point[i][5];e+=point[i][3];f+=point[i][6];
        }
        __int64 x=b*b+d*d+f*f,y=2*(a*b+c*d+e*f),z=a*a+c*c+e*e;
        printf( "Case #%d:", cas );
        if( x == 0 ){
             if( y == 0 ) printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else if( y > 0 ) printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else{
                 double p=-1*z/y;
                 printf(" 0.00000000 %.8lf\n",p);
             }
        }
        else{
             double mid = -1.0*y/(2*x);
             if(mid<0) printf(" %.8lf 0.00000000\n",sqrt(((double)z)/(n*n)));
             else{
                 double judge = y*y-4*x*z;
                 if( judge > EPS || fabs( judge ) < EPS ){
                      double x1 = (-1*y-sqrt(judge))/(2*x);
                      double x2 = (-1*y+sqrt(judge))/(2*x);
                      if( x1 > EPS || fabs( x1 ) < EPS ) printf(" 0.00000000 %.8lf\n",x1);
                      else printf(" 0.00000000 %.8lf\n",x2);
                 }
                 else{
                      double low = (x*mid*mid+y*mid+z)/(n*n);
                      printf(" %.8lf %.8lf\n",sqrt(low),mid);
                 }
             }
        }
    }
    return 0;
}

