#include <iostream>
#include <cstdio>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)

int ml[111], mr[111], a[111][30], b[111][111];
int p[111];
int n, k;

int check(int u, int v){
    For(i,1,k) if (a[u][i]>=a[v][i]) return false;
    return true;
}

int findpath(int u){
    For(v,1,n) if (b[u][v] && !p[v]){
        p[v]=u;
        if (mr[v]==0)            
            return v;
        int t = findpath(mr[v]);
        if (t>0) return t;
    }
    return -1;
}

void incr(int u, int v){
    int t=p[v];
    int pp=ml[t];
    ml[t]=v;
    mr[v]=t;
    if (t==u) return;
    incr(u, pp);
}

int main(){
    
    freopen("c.in", "r", stdin);
    freopen("c.out","w", stdout);
    
    int n0ftest;
    scanf("%d", &n0ftest);
    For(test,1,n0ftest){
        scanf("%d%d", &n, &k);
        For(i,1,n) For(j,1,k) scanf("%d", &a[i][j]);
        
        memset(b, 0, sizeof(b));        
        For(i,1,n) For(j,1,n) b[i][j]=check(i,j);
//        For(i,1,n) For(j,1,n) if (b[i][j]) cout<<i<<" "<<j<<endl;
        
        int res =0;
        memset(ml, 0, sizeof(ml));
        memset(mr, 0, sizeof(mr));
        
        For(i,1,n){
            memset(p, 0, sizeof(p));
            k= findpath(i);
 //           cout<<i<<" "<<k<<endl;
            if (k>0){
                res++;
                incr(i, k);
            }
  //          For(i,1,n) cout<<ml[i]<< "  "<<mr[i]<<endl;
        }
        printf("Case #%d: %d\n", test, n-res);
    }    
    return 0;
}
