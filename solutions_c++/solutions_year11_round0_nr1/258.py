#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int Abs(int a){
    if( a >= 0 ) return a;
    return -a;
}
int Max(int a,int b){
    if( a >= b ) return a;
    return b;
}

int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,n,cas,d;
    int s0,s1,t0,t1;
    char st[3],pre;
    scanf("%d",&t);
    for (cas = 1; cas <= t; ++cas){
        scanf("%d",&n);
        s0 = s1 = 1;
        t0 = t1 = 0;
        pre = 'a';
        for (int i = 0; i < n; ++i){
            scanf("%s%d",st,&d);
            if( st[0] == 'O' ){
                t0 += Abs(d-s0)+1;
                s0 = d;
            }else{
                t1 += Abs(d-s1)+1;
                s1 = d;
            }
            if( pre != st[0] ){
                if( st[0] == 'O' ){
                    if( t0 <= t1 ) t0 = t1+1;
                }else{
                    if( t1 <= t0 ) t1 = t0+1;
                }
                pre = st[0];
            }
        }
        int ans = Max(t0,t1);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
