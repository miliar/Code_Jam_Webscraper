#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
using namespace std;

struct SEG{
    int b,e,v;
    void set(int _b, int _e, int _v){ b = _b, e = _e, v = _v; }
    bool operator < (const SEG &n)const
    { return v < n.v; }
}seg[31313];
int cnt;
int T, S, R, X, t, N;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        cnt = 0;
        for(int i = 0; i < N ;i++){
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            seg[cnt++].set(b, e, w);
        }
        for(int i = 0; i < N; i++){
            int b = (i == 0) ? 0 : seg[i-1].e;
            if(b < seg[i].b) seg[cnt++].set(b,seg[i].b,0);
        }
        if(seg[N-1].e<X) seg[cnt++].set(seg[N-1].e,X,0);
        sort(seg, seg+cnt);
        
        double lft = t, ans = 0;
        
        for(int i = 0; i < cnt; i++){
//            printf("%d,%d(%d) ", seg[i].b, seg[i].e, seg[i].v);
            double tmp = ((double)seg[i].e-seg[i].b)/(seg[i].v+R);
            if(tmp > lft){
                ans += lft;
                ans += ((double)seg[i].e-seg[i].b-lft*(seg[i].v+R))/(seg[i].v+S);
                lft = 0;
            } else{
                ans += tmp;
                lft -= tmp;
            }
        }
        
        printf("Case #%d: %.10lf\n",cas, ans);
    }
    return 0;
}
