#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <string.h>
#include <memory.h>
using namespace std;
template <class T> void OUT(T x, int n){  for(int i = 1; i <= n; ++i)  cout << x[i] << ' ';    cout << endl;    }
template <class T> void OUT(T x, int n, int m){  for(int i = 1; i <= n; ++i)    OUT(x[i], m);    cout << endl;    }
template <class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
#define  eps 1e-8
#define  LL long long
inline LL mod(LL x, LL y) { return x - floor(1.0 * x / y+eps) * y; }
#define  out(x) (cout << #x << " = " << x << endl)
#define  Set(a,b)  memset(a,b,sizeof(a))
#define  Sqr(x) ((x) * (x))
#define  pi  acos(-1.0)
const int maxn = 1000005,INF = (1<<29);
int n,m;

struct node{
    int s,e,v;
}seg[maxn];

bool comp(node a,node b){
    if(a.v==b.v) return a.s<b.s;
    else return a.v<b.v;
}
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,t,T,x,y,sum,index,v;
    cin>>T;
    for(t=1;t<=T;t++){
        int s,r,tt,B,E;
        scanf("%d%d%d%d%d",&x,&s,&r,&tt,&n);
        int pre=0,m=0;
        for(i=0;i<n;i++){
            scanf("%d%d%d",&B,&E,&v);
            if(pre!=B){
                seg[m].s=pre;
                seg[m].e=B;
                seg[m++].v=0;

                seg[m].s=B;
                seg[m].e=E;
                seg[m++].v=v;
                pre=E;
            }
            else {
                seg[m].s=B;
                seg[m].e=E;
                seg[m++].v=v;
                pre=E;
            }
        }
        if(pre!=x){
                seg[m].s=pre;
                seg[m].e=x;
                seg[m++].v=0;
        }
//        out(m);
        sort(seg,seg+m,comp);
        double ans=0,Time=tt,a,b,c;
        for(i=0;i<m;i++){
//            out(i);
//            cout<<seg[i].s<<" "<<seg[i].e<<" "<<seg[i].v<<endl;
            a=(seg[i].e-seg[i].s)*1.0/(seg[i].v+r);
//            out(a);
//            out(Time);
            if(a>Time){
                b=Time*(seg[i].v+r);
                c=(seg[i].e-seg[i].s)*1.0-b;
                ans+=c/(seg[i].v+s)+Time;
                Time=0;
            }
            else {
                ans+=a;
                Time-=a;
            }
//            out(ans);
        }
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
