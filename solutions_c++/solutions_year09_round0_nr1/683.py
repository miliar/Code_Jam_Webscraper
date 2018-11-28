#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define FS first
#define SD second

string slowa[100000];
bool S[20][2256];

int main(){
   int L,D,N;
   cin>>L>>D>>N;
   FOR(i,0,D) cin>>slowa[i];
   FORE(t,1,N){
      string s;
      cin>>s;
      FOR(i,0,L) for(char c = 'a';c<='z';c++) S[i][c] = false;
      int ind = 0;
      FOR(i,0,L){
         if(s[ind]=='('){
            ind++;
            while(s[ind]!=')') S[i][s[ind++]] = true;
            ind++;
         }
         else S[i][s[ind++]] = true;
      }
      int ret = 0;
      FOR(i,0,D){
         bool ok = true;
         FOR(j,0,L) if(!S[j][slowa[i][j]]) ok = false;
         ret+=ok;
      }
      printf("Case #%d: %d\n",t,ret);
   }
}
