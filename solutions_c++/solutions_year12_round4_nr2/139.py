#include<cstdio>
#include<cstdlib>
#include<algorithm>
#define MX 1002
using namespace std;
pair<int,int> r[MX];
double xx[MX],yy[MX],x[MX],y[MX];
inline int minn(int aa,int bb) {
    if (aa<bb) return aa; else return bb;
}
inline int maxx(int aa,int bb) {
    if (aa>bb) return aa; else return bb;
}
inline void pitch(int pos, double xt, double yt) {
    xx[r[pos].second] = xt;
    yy[r[pos].second] = yt;
}
inline double sq(double q) {
    return q*q;
}
inline int collide(int posi, int posj) {
    return sq(x[posi]-x[posj])+sq(y[posi]-y[posj]) < sq(r[posi].first+r[posj].first);
}
int main() {
    int i,j,t,tt,n,w,l,fail,check,attempt;
    scanf("%d",&tt);
    for(t=1;t<=tt;t++) {
        scanf("%d",&n);
        scanf("%d",&w);
        scanf("%d",&l);
        for(i=0;i<n;i++) {
            scanf("%d",&r[i].first);
            r[i].second = i;
        }
        sort(r,r+n);
        x[n-1] = 0.0;
        y[n-1] = 0.0;
        pitch(n-1,0.0,0.0);
        x[n-2] = w;
        y[n-2] = l;
        pitch(n-2,w,l);
        srand(789453437);
        fail = 1;
        while(fail) {
            fail = 0;
            attempt = 0;
            for(i=n-3;i>=0;i--) {
                check = 1;
                while(check) {
                    x[i] = ((float)rand()/(float)RAND_MAX)*w;
                    y[i] = ((float)rand()/(float)RAND_MAX)*l;
                    pitch(i,x[i],y[i]);
                    check = 0;
                    for(j=i+1;j<n;j++) {
                        if(collide(i,j)) {
                            check = 1;
                            break;
                        }
                    }
                    if(check) {
                        attempt++;
                        if(attempt >= 30000) {
                            fail = 1;
                            break;
                        }
                    }
                }
                if(fail) {
                    break;
                }
            }
        }
        
        
        printf("Case #%d: ",t);
        for(i=0;i<n;i++) {
            printf("%lf %lf ",xx[i],yy[i]);
        }
        printf("\n");
    }    
}
