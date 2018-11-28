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
#include <string.h>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 

string W = "welcome to code jam";
char line[1000];
int mem[550][25];

int go(int poz,int ind){
   if(mem[poz][ind]!=-1) return mem[poz][ind];
   if(line[poz]!=W[ind]) return mem[poz][ind] = 0;
   if(ind==0) return mem[poz][ind] = 1;
   int ret = 0;
   FOR(i,0,poz) ret += go(i,ind-1);
   return mem[poz][ind] = ret%10000;
}

int main(){
   int T;scanf("%d\n",&T);
   FORE(t,1,T){
      fgets(line,1000,stdin);
      FOR(i,0,550) FOR(j,0,25) mem[i][j] = -1;
      int ret = 0;
      int l = strlen(line)-1;    
      FOR(i,0,l) ret+=go(i,SZ(W)-1);
      ret = ret%10000;
      stringstream s;
      s<<ret;
      string ss = s.str();
      while(SZ(ss)<4) ss = "0"+ss;
      cout<<"Case #"<<t<<": "<<ss<<endl;
   }


}
