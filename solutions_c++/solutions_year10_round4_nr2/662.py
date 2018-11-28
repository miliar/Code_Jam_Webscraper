#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,m[1055],c[15][1055];

int skip (int lvl,int watch,int fr,int to) {
    if (lvl<0) {
       if (m[fr]<n-watch) return -1;
       return 0;
       }
    int ca,cb,da,db;
    int tota,totb;
    ca=skip(lvl-1,watch+1,fr,(fr+to)/2);
    cb=skip(lvl-1,watch+1,(fr+to)/2,to);
    if (ca==-1 || cb==-1) tota=-1;
       else tota=ca+cb+c[lvl][fr/(1<<(lvl+1))];
    da=skip(lvl-1,watch,fr,(fr+to)/2);
    db=skip(lvl-1,watch,(fr+to)/2,to);
    if (da==-1 || db==-1) totb=-1;
       else totb=da+db;
    //printf("lvl: %d - %d (%d,%d) = %d,%d\n",lvl,watch,fr,to,tota,totb);
    //printf("%d,%d + %d,%d[%d]  %d,%d\n",ca,cb,lvl,fr/(1<<(lvl+1)),c[lvl][fr/(1<<(lvl+1))],da,db);
    if (tota==-1 && totb==-1) return -1;
    if (tota==-1) return totb;
    if (totb==-1) return tota;
    return min(tota,totb);
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d",&n);
        for (int j=0; j<(1<<n); j++)
            scanf("%d",&m[j]);
        for (int j=0; j<n; j++)
            for (int k=0; k<(1<<(n-j-1)); k++)
                scanf("%d",&c[j][k]);
        printf("Case #%d: %d\n",i+1,skip(n-1,0,0,1<<n));
        
        }
    
}
