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

ll T,N,l,h,x[10000+5];

ll solve(){
   ll i,j;
   REP(j,l,h){
      bool acc = 1;
      REP(i,1,N){
         bool ok = (x[i]%j==0 || j%x[i]==0);
         if (!ok) acc = 0;
      }
      if (acc) return j;
   }
   return 0;
}
int main(){
   ll i,j,t = 0;
   scanf("%lld",&T);
   while (T--){
      scanf("%lld %lld %lld",&N,&l,&h);
      REP(i,1,N) scanf("%lld",&x[i]);
      printf("Case #%lld: ",++t);
      ll res = solve();
      if (res) printf("%lld\n",res);
         else puts("NO");
   }
}
