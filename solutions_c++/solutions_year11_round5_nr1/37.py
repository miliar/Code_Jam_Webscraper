#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define EPS 1E-8

inline int SG(double x) {
    if(x>-EPS && x<EPS) return 0;
    return x>0?1:-1;
}

class PT{
    public:
        double x,y;
        PT(){}
        PT(double _x,double _y) {
            x = _x; y = _y;
        }
};

PT lt[1000000];
PT ut[1000000];

int main() {
    int TT,tt,n,m,G,i,j,k;
    double W,sum,ds,x,dd,s,dy,dy2,y,dx,L,R,M;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%lf %d %d %d",&W,&n,&m,&G);
        for( i=0; i<n; i++ ) {
            scanf("%lf %lf",&lt[i].x,&lt[i].y);
        }
        for( i=0; i<m; i++ ) {
            scanf("%lf %lf",&ut[i].x,&ut[i].y);
        }
        sum = 0;
        for( i=1; i<m; i++ ) {
            sum+=(ut[i].y+ut[i-1].y)*(ut[i].x-ut[i-1].x)/2;
        }
        for( i=1; i<n; i++ ) {
            sum-=(lt[i].y+lt[i-1].y)*(lt[i].x-lt[i-1].x)/2;
        }
        printf("Case #%d:\n",tt+1);
        for( i=1; i<G; i++ ) {
            ds = sum/(double)G*i;
            L = 0;
            R = W;
            for( j=0; j<50; j++ ) {
                M = (L+R)/2;
                s = 0;
                for( k=1; k<m; k++ ) {
                    if(ut[k].x>M) {
                        y = (ut[k].y-ut[k-1].y)*(M-ut[k-1].x)/(ut[k].x-ut[k-1].x)+ut[k-1].y;
                        s+=(y+ut[k-1].y)*(M-ut[k-1].x)/2;
                        break;
                    }else {
                        s+=(ut[k].y+ut[k-1].y)*(ut[k].x-ut[k-1].x)/2;
                    }
                }
                for( k=1; k<n; k++ ) {
                    if(lt[k].x>M) {
                        y = (lt[k].y-lt[k-1].y)*(M-lt[k-1].x)/(lt[k].x-lt[k-1].x)+lt[k-1].y;
                        s-=(y+lt[k-1].y)*(M-lt[k-1].x)/2;
                        break;
                    }else {
                        s-=(lt[k].y+lt[k-1].y)*(lt[k].x-lt[k-1].x)/2;
                    }
                }
                if(s>ds) {
                    R = M;
                }else {
                    L = M;
                }
            }
            printf("%.8f\n",(R+L)/2);
        }
    }
    return 0;
}
