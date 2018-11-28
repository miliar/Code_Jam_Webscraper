#include <vector> 
#include <string> 
#include <set> 
#include <algorithm> 
#include <map> 
#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
using namespace std; 
  
#define FOR(it,x) for(it=x.begin();it!=x.end();++it)  
#define SZ(a) int((a).size())  
#define ALL(a) (a).begin(),(a).end()  
#define PB push_back 
#define MP make_pair

int t,M,N;
int G[1000000], C[1000000];
int mem[1000000][2], val[1000000][2];

int fans(int n, int v) {
    if(mem[n][v]) return val[n][v];
    int mc = -1, c;
    int a, b, x, ca, cb;
    for(a=0;a<2;a++) {
        for(b=0;b<2;b++) {
             for(x=0;x<2;x++) {
                 if(x==0&&(a|b)==v) {
                     if(!C[n]&&x!=G[n]) continue;
                     ca = fans(2*n+1,a);
                     cb = fans(2*n+2,b);
                     if(ca<0||cb<0) continue;
                     c = ca+cb+(x!=G[n]);
                 } else if(x==1&&(a&b)==v) {
                     if(!C[n]&&x!=G[n]) continue;
                     ca = fans(2*n+1,a);
                     cb = fans(2*n+2,b);
                     if(ca<0||cb<0) continue;
                     c = ca+cb+(x!=G[n]);
                 } else continue;
                 if(mc<0||c<mc) mc=c;
             }
        }
    }
    mem[n][v]=1;
    val[n][v]=mc;
    return mc;
}

int main() {
    int T,V,i,v;
    freopen("A_in.txt","r",stdin);
    freopen("A_out.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++) {
          scanf("%d %d",&M,&V);
          N = (M-1)/2;
          for(i=0;i<M;i++) {
                if(i<N) {
                     scanf("%d %d",G+i,C+i);
                     mem[i][0] = mem[i][1] = 0;
                } else {
                     scanf("%d",G+i);
                     mem[i][0] = mem[i][1] = 1;
                     val[i][G[i]] = 0;
                     val[i][1-G[i]] = -1;
                }    
          }
          v = fans(0,V);
          if(v>=0)
          printf("Case #%d: %d\n",t,v);
          else
          printf("Case #%d: IMPOSSIBLE\n",t);
          /*
          for(i=0;i<M;i++) {
              printf("%d\n",i);
              printf("%d %d\n",mem[i][0],val[i][0]);
              printf("%d %d\n",mem[i][1],val[i][1]);
          }
          */
    }
	return 0;
}
