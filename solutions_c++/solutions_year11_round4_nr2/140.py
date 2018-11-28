#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

class SS{
    public:
        long long sx,sy,s;
        SS(long long _sx=0,long long _sy=0,long long _s=0) {
            sx = _sx; sy = _sy; s = _s;
        }
        SS operator+(const SS& t) const {
            return SS(sx+t.sx,sy+t.sy,s+t.s);
        }
        SS operator-(const SS& t) const {
            return SS(sx-t.sx,sy-t.sy,s-t.s);
        }
};

long long c[600][600];
SS sum[600][600];
char str[600];

SS g(int i,int j) {
    return SS(i*c[i][j],j*c[i][j],c[i][j]);
}

int main() {
    int TT,tt,n,m,i,j,k,D,md;
    SS s;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d %d",&n,&m,&D);
        for( i=1; i<=n; i++ ) {
            scanf("%s",str);
            for( j=1; j<=m; j++ ) {
                c[i][j] = D+str[j-1]-'0';
            }
            c[i][0] = c[i][m+1] = 0;
        }
        for( i=0; i<=m+1; i++ ) {
            c[0][i] = c[n+1][i] = 0;
        }
        for( i=0; i<=n; i++ ) {
            for( j=0; j<=m; j++ ) {
                sum[i][j] = SS();
            }
        }
        for( i=1; i<=n; i++ ) {
            for( j=1; j<=m; j++ ) {
                sum[i][j] = sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+g(i,j);
            }
        }
        md = 0;
        for( i=1; i<=n; i++ ) {
            for( j=1; j<=m; j++ ) {
                for( k=2; i+k<=n && j+k<=m; k++ ) {
                    s = sum[i+k][j+k]-sum[i-1][j+k]-sum[i+k][j-1]+sum[i-1][j-1]
                        -g(i+k,j+k)-g(i,j+k)-g(i+k,j)-g(i,j);
                    if(2*s.sx==(2*i+k)*s.s && 2*s.sy==(2*j+k)*s.s) {
                        if(k+1>md) md = k+1;
                    }
                }
            }
        }
        if(md==0) {
            printf("Case #%d: IMPOSSIBLE\n",tt+1);
        }else {
            printf("Case #%d: %d\n",tt+1,md);
        }
        fflush(0);
    }
    return 0;
}
