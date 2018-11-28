#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;
#define FOR(i,n) for(int i=0,_n; i<n; i++)
int ntest;
long long d[10005],l[10005],D,e[10005];
int n;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    FOR(test,ntest){
        printf("Case #%d: ",test+1);
        scanf("%d",&n);
        FOR(i,n){
            scanf("%lld %lld",&d[i],&l[i]);            
        }
        scanf("%lld",&D);
        memset(e,0,sizeof e);
        e[0]=2*d[0];
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if( e[j] >= d[i] ){
                    e[i] = max(e[i],d[i]+min(l[i],d[i]-d[j]) );    
                }
            }
        }
        bool flag=false;
        FOR(i,n){
            if(e[i]>=D) flag=true;
        }
        if(flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
