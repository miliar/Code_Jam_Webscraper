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

char move[105],kal[105];
int pos[105];
int o[105],b[105],po,pb,qo,qb,NB,NO,N,T,x,t;

int main(){
   int i,j;
   
   scanf("%d",&T);
   REP(t,1,T){
      printf("Case #%d: ",t);
      scanf("%d",&N); NO = NB = 0; //printf("\n");
      
      REP(i,1,N){
         scanf("%s %d",kal,&x);
         move[i] = kal[0]; pos[i] = x;
         if (move[i]=='O') o[++NO] = pos[i];
            else b[++NB] = pos[i];
      }
   
      qo = 1; qb = 1; po = 1, pb = 1; int time = 0;
      REP(i,1,N){ if (move[i]=='O'){
         while (po != pos[i]){
            time++;
            if (po > pos[i]) po--; else if (po < pos[i]) po++;
            if (pb > b[qb]) pb--; else if (pb < b[qb]) pb++;
         }
         time++; qo++;
        if (pb > b[qb]) pb--; else if (pb < b[qb]) pb++;
      } else {
         while (pb != pos[i]){
            time++;
            if (pb > pos[i]) pb--; else if (pb < pos[i]) pb++;
            if (po > o[qo]) po--; else if (po < o[qo]) po++;
         }   
         time++; qb++;
         if (po > o[qo]) po--; else if (po < o[qo]) po++;
      }
      //printf("%d %d %d %d\n",i,po,pb,time);
      }
      printf("%d\n",time);
   }
}
