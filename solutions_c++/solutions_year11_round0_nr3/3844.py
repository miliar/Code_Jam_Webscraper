#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <memory.h>
#include <cctype>
#include <bitset>
#include <limits>

#define cs c_str()
#define ALL(V) V.begin(),V.end()
#define FORN(i,N) for (i=0;i<(int)N;i++)
#define REP(i,a,b) for (i = (int) a; i<= (int) b; i++)
#define REP_D(i,a,b) for (i = (int) a; i>=(int) b; i--)
#define ITER(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)
#define pqueue priority_queue
#define ll long long
#define pb push_back
#define ii pair<int,int>
#define HINF 1000000000
#define INF 2000000000
#define mp make_pair
#define ff first
#define ss second
#define MAX 2000000
using namespace std;

const double eps = 1e-7;

int x[1005],T,N,i,t;
int main(){
   scanf("%d",&T);
   REP(t,1,T){
      scanf("%d",&N);
      FORN(i,N) scanf("%d",&x[i]);
      
      int res = -INF,batas = 1<<N,sum1,sum2,bil,ct,pile1,pile2;
      FORN(i,batas){
         sum1 = sum2 = pile1 = pile2 = 0;
         bil = i;
         FORN(ct,N){
            if (bil & 1){
               sum1 += x[ct]; pile1 = pile1 ^ x[ct];
            } else {
               sum2 += x[ct]; pile2 = pile2 ^ x[ct];
            }
            bil = bil >> 1;
         }
         if (pile1==pile2 && sum1>0 && sum2 > 0) res = max(res,max(sum1,sum2));
      }
      printf("Case #%d: ",t);
      if (res==-INF) printf("NO\n");
         else printf("%d\n",res);
   }
}
