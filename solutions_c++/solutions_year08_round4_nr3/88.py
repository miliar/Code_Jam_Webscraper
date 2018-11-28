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

int t,N;
int x[1000000];
int y[1000000];
int z[1000000];
int p[1000000];

int abs(int x) {
    return x<0?-x:x;
}

int main() {
    int T,V,i,j,ok;
    freopen("C_in.txt","r",stdin);
    freopen("C_out.txt","w",stdout);
    scanf("%d",&T);
    double st,en,md,v,d;
    for(t=1;t<=T;t++) {
          scanf("%d",&N);
          for(i=0;i<N;i++) {
              scanf("%d %d %d %d",x+i,y+i,z+i,p+i);
          }
          st = 0;
          en = 3000000;
          while(en-st>1e-7) {
               md = (en+st)*0.5;
               ok = 1;
               for(i=0;i<N;i++) {
                  for(j=i+1;j<N;j++) {
                     d = abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j]);
                     if(d>md*(p[i]+p[j])) ok=0;
                  }
               }
               if(ok) en=md;
               else st=md;
          }
          printf("Case #%d: %lf\n",t,md);
    }
	return 0;
}
