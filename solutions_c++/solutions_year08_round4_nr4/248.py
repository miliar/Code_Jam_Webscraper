#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////

int k;
char r[1005];
char t[1005];
VI p;

void solve(){
   scanf("%d\n",&k);
   scanf("%s\n",r);
   int d=strlen(r);
   p.clear();
   FOR(i,k) p.PB(i);
   int ret=978654321;
   do{
     for(int q=0;q<d;q+=k){
       FOR(i,k){
           t[q+i]=r[q+p[i]];           
       }       
     }
     int x=1;
     FR(i,1,d){
       if(t[i]!=t[i-1]) x++;
     }
     ret=min(ret,x);
   }while(next_permutation(ALL(p)));
   printf(" %d\n",ret);
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


