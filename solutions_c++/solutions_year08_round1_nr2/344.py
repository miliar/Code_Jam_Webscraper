#include<cstdio>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
#include<sstream>

using namespace std;

#define pf printf
#define sf scanf
#define co continue
#define re return
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

int n, m;

struct node{
       vector<int> c, t;
};

vector<node> V;

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    int cases = 1;
    for( sf("%d", &t); t--; ) {
         V.clear();
         sf("%d", &n);
         sf("%d", &m);
         V.clear();
         int i, j,k;
         for(i=0;i<m;i++) {
           int T;
           sf("%d", &T);
           node A; A.c.clear(); A.t.clear();
           for(j=0;j<T;j++) {
             int a, b; 
             sf("%d %d", &a, &b);
             A.c.pb(a); A.t.pb(b);
           }
           V.pb(A);
         }
         int res = 0;
         int cnt = 10000;
         for(i=0;i<(1<<n);i++) {
           for(j=0;j<m;j++) {
             for(k=0;k<V[j].c.size();k++) {
                int a = V[j].c[k];
                int b = V[j].t[k];
                
                if( (b == 1 && (i & (1<<(a-1)  ) ) ) ) break;
                if( (b == 0 && !(i & (1<<(a-1)) ) ) ) break;
                
             }
             if( k == V[j].c.size() ) break;
           }
           if( j == m ) {
             int p = 0;
             for(j=0;j<n;j++) if( i & (1<<j) )  p++;
             if( p < cnt ) cnt = p, res = i;
           }
         } 
         printf("Case #%d:", cases++);
         if( cnt == 10000 )
          printf(" IMPOSSIBLE");
         else {
         for(i=0;i<n;i++)
           printf(" %d", (res & (1<<i)) ? 1 : 0 );
         }
         pf("\n");
    }
    return 0;
}

