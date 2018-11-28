/*
    ID:
    PROG:
    LANG:C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int n,T,m,w,r,tot;
double ans,u,t;
struct ele{
    int b,e,v;
}l[2000];
bool cmp(const ele&x,const ele& y){
    return x.v<y.v;
}
int main(){
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    scanf("%d",&T);
    for(int cs=1;cs<=T;++cs){
        scanf("%d%d%d%lf%d",&m,&w,&r,&t,&n);
        l[0].b=l[0].e=l[0].v=0;
        tot=1;
        for(int i=0;i<n;++i){
           int x,y,z;
           scanf("%d%d%d",&x,&y,&z);
           if(x!=l[tot-1].e){
               l[tot].b=l[tot-1].e;
               l[tot].e=x;
               l[tot].v=w;
               ++tot;
           }
           l[tot].b=x;
           l[tot].e=y;
           l[tot].v=z+w;
           ++tot;
        }
        if(m!=l[tot-1].e){
               l[tot].b=l[tot-1].e;
               l[tot].e=m;
               l[tot].v=w;
               ++tot;
        }
        ans=0;
        sort(l,l+tot,cmp);
        for(int i=0;i<tot;++i){
            if(l[i].v==0)continue;
            u=min(t,double(l[i].e-l[i].b)/(l[i].v-w+r));
            ans+=(double(l[i].e-l[i].b)-u*(l[i].v-w+r))/l[i].v+u;
            t-=u;
        }
        printf("Case #%d: ",cs);
        printf("%.7f\n",ans);
    }
    return 0;
}
