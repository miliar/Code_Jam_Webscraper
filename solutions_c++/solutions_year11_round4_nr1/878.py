#include<cstdio>
#include<cmath>
#include<cstring>
#include<time.h>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
using namespace std;

struct Node{
    int v, s;
};
bool cmp( Node s, Node t ){ return s.v<t.v; }

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cs = 0, T, x, w, r, t, n;
    Node p[100008];
    scanf("%d",&T);
    while( T-- ){
        scanf("%d%d%d%d%d",&x,&w,&r,&t,&n);
        int pn = 0, u, v, sum = 0;
        for(int i=0; i<n; i++){
            scanf("%d%d%d",&u,&v,&p[i].v);
            p[i].s = abs(u-v);
            sum += abs(u-v);
        }
        p[n].v = 0; p[n].s = x-sum;
        sort( p, p+n+1, cmp );

        double tn = 0, tt = t;
        for(int i=0; i<=n; i++){
            double v = p[i].v, s = p[i].s;
            //cout<<v<<" "<<s<<endl;
            if( s<=tt*(v+r) ){
                tn += s/(v+r);
                tt -= s/(v+r);
            }
            else{
                if( tt>0 ){
                    tn += tt;
                    s -= (v+r)*tt;
                    tt = 0;
                }
                tn += s/(v+w);
            }
        }
        printf("Case #%d: %.8f\n",++cs,tn);
    }
    return 0;
}
