#include <stdio.h>
#include <set>
#include <algorithm>

using namespace std;

char str[100];

inline int gcd(int a,int b){
    if(a<0) a=-a;
    if(b<0) b=-b;
    if(!b) return a;
    while((a%=b) && (b%=a));
    return a+b;
}

int main(){
    int TT,tt,n,m,i,j,s,W,H,r,x,y,tx,ty,d;
    set<pair<int,int> > ss;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d %d",&n,&m,&r);
        for( i=0; i<n; i++ ) {
            scanf("%s",str);
            for( j=0; j<m; j++ ) {
                if(str[j]=='X'){
                    x=i*2-1;
                    y=j*2-1;
                }
            }
        }
        W = n-2;
        H = m-2;
        s = 0;
        ss.clear();
        for( i=-100; i<100; i++ ) {
            for( j=-100; j<100; j++ ) {
                if(i==0 && j==0) continue;
                tx = (i%2?W-x:0)+i*W;
                ty = (j%2?H-y:0)+j*H;
                if(tx*tx+ty*ty<=r*r){
                    d = gcd(tx,ty);
                    tx/=d;
                    ty/=d;
                    if(ss.find(make_pair(tx,ty))==ss.end()){
                        s++;
                        ss.insert(make_pair(tx,ty));
                    }
                }
            }
        }
        printf("Case #%d: %d\n",tt+1,s);
    }
    return 0;
}
