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

string res,chg,kal;
int T,C,D,N,i,j,t;

int main(){
   scanf("%d",&T);
   REP(t,1,T){
      scanf("%d",&C);
      REP(i,1,C) cin >> res;
      scanf("%d",&D);
      REP(i,1,D) cin >> chg;
      scanf("%d",&N); getchar();
      vector<char> lis;
      while (N--){
         char c = getchar(); //putchar(c);
         if (C>0 && (c==res[0]||c==res[1]) && lis.size()>0){
            if (c==res[0] && lis[lis.size()-1]==res[1]){lis[lis.size()-1] = res[2]; continue;}
            else if (c==res[1] && lis[lis.size()-1]==res[0]){lis[lis.size()-1] = res[2];continue;}
         }
         if (D>0 && c==chg[0]){
            unsigned int i = 0;
            while (i <= lis.size()){
               if (i==lis.size()){lis.pb(c); break;}
               if (lis[i]==chg[1]){
                  while (!lis.empty()) lis.pop_back();
                  //while (i != lis.size()) lis.pop_back();
                  //puts("hare");
                  //FORN(i,lis.size()) putchar(lis[i]); putchar('\n');
                  break;
               }
               i++;
            }
            //puts("hare");
         } else if (D>0 && c==chg[1]){
            unsigned int i = 0;
            while (i <=lis.size()){
               if (i==lis.size()){lis.pb(c); break;}
               if (lis[i]==chg[0]){
                  while (!lis.empty()) lis.pop_back();
                  //while (i != lis.size()) lis.pop_back();
                  //puts("hare");
                  //FORN(i,lis.size()) putchar(lis[i]); putchar('\n');
                  break;
               }
               i++;
            }
            
         } else lis.pb(c);
      }
      printf("Case #%d: ",t);
      if (lis.size()==0) printf("[]");
      for(unsigned int i=0;i<lis.size();i++)
         printf("%c%c%c",(i==0)?'[':' ',lis[i],(i==lis.size()-1)?']':',');
      printf("\n");
   }
}
