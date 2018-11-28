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
const int maxn = 105,INF = (1<<29);
int n,m;
char color[2];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,t,T,x,y,sum,index;
    cin>>T;
    for(t=1;t<=T;t++){
        scanf("%d",&n);
        int poso=1,posb=1,preT=0,preo=0,preb=0;
        for(i=0;i<n;i++){
            scanf("%s%d",color,&x);
            if(color[0]=='O'){
                k=abs(x-poso)+preo;
                poso=x;
                preT=max(k+1,preT+1);
                preo=preT;
            }
            else {
                k=abs(x-posb)+preb;
                posb=x;
                preT=max(k+1,preT+1);
                preb=preT;
            }
//            out(preT);
        }
        printf("Case #%d: %d\n",t,preT);
    }
    return 0;
}
