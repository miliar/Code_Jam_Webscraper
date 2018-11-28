#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

class PT{
    public:
        double x,y;
        PT(){}
        PT(int _x,int _y) {
            x = _x;
            y = _y;
        }
        bool operator<(const PT& p) const {
            return x<p.x;
        }
};

PT pt[1000010];

int main() {
    int tt,TT,n,m,i,j,k,t,X,R,S,B,W,E;
    double sum,d,u;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d %d %d %d",&X,&S,&R,&t,&n);
        for( i=0; i<n; i++ ) {
            scanf("%d %d %d",&B,&E,&W);
            pt[i] = PT(W,E-B);
            X-=E-B;
        }
        pt[n++] = PT(0,X);
        sort(pt,pt+n);
        u = 0;
        sum = 0;
        for( i=0; i<n; i++ ) {
            d = pt[i].y/(pt[i].x+R);
            if(d+u>t) d = t-u;
            sum+=(pt[i].y-(pt[i].x+R)*d)/(pt[i].x+S)+d;
            u+=d;
        }
        printf("Case #%d: %.8f\n",tt+1,sum);
    }
    return 0;
}

