#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

#define FOR(i,n) for(i=0;i<n;i++)

using namespace std;

int gcd(int a,int b){ if (!b) return a; else return gcd(b,a%b); }

bool possible(long long N,int Pd,int Pg){
  if(Pg==100) return Pd==100;
  if(Pg==0) return Pd==0;
  return 100/gcd(100,Pd)<=N;
}

int main(int argc, char *argv[]){
  long long N;
  int T,t,Pd,Pg;
  scanf("%d",&T);
  FOR(t,T){
    scanf("%lld%d%d",&N,&Pd,&Pg);
    printf("Case #%d: ",t+1);
    if(possible(N,Pd,Pg)) printf("Possible");
    else printf("Broken");
    printf("\n");
  }
  return 0;
}
