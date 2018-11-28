#include <vector> 
#include <string> 
#include <set> 
#include <algorithm> 
#include <map> 
#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
using namespace std; 
  
#define FOR(it,x) for(it=x.begin();it!=x.end();++it)  
#define SZ(a) int((a).size())  
#define ALL(a) (a).begin(),(a).end()  
#define PB push_back 
#define MP make_pair

int t,M,N,A,x1,y1,x2,y2;

int gcd(int a, int b) {
    if(a % b == 0) {
        y2 = 0;
        y1 = 1;
        return a;
    } else {
        int d = gcd(b, a % b);
        int t;
        t = y2;
        y2 = y1;
        y1 = t-y1*(a / b);
        return d;
    }
}

int abs(int x) {
    return x<0?-x:x;
}

int main() {
    int T,V,i,v,d;
    freopen("B_in.txt","r",stdin);
    freopen("B_out.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++) {
          scanf("%d %d %d",&N,&M,&A);
          for(x1=0;x1<=N;x1++) {
             for(x2=0;x2<=N;x2++) {
                for(y1=0;y1<=M;y1++) {
                    for(y2=0;y2<=M;y2++) {
                        if(x1+y1>0&&x2+y2>0) {
                         if(x1*y2-x2*y1!=A) continue;
                         printf("Case #%d: 0 0 %d %d %d %d\n",t,x1,y1,x2,y2);
                         break;
                        }
                    }
                    if(y2<=M) break;
                }
             if(y2<=M) break;
             }
             if(y2<=M) break;
          }
          if(y2>M)
          printf("Case #%d: IMPOSSIBLE\n",t);
    }
	return 0;
}
