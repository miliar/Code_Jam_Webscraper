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

char x[55][55];
int T,B,K;

   int di[] = {+0,+0,+1,+1};
   int dj[] = {+0,+1,+0,+1};
   
int transform(){
   int i,j,k;
   REP(i,1,B) REP(j,1,K) if (x[i][j]=='#'){
      FORN(k,4) if (x[i+di[k]][j+dj[k]]!='#') return 0;
      x[i][j] = '/';
      x[i][j+1] = '\\';
      x[i+1][j] = '\\';
      x[i+1][j+1] = '/';
   }
   return 1;
}

int main(){
   int i,j,t = 0;
   scanf("%d",&T);
   while (T--){ t++;
      FORN(i,55) FORN(j,55) x[i][j] = '.';
      scanf("%d %d",&B,&K); getchar();
      REP(i,1,B){
         REP(j,1,K) x[i][j] = getchar();
         getchar();
      }
      printf("Case #%d:\n",t);
      if (transform()){
         REP(i,1,B){
            REP(j,1,K) putchar(x[i][j]);
            putchar('\n');
         }
      } else printf("Impossible\n");
   }
}
