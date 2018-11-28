#include <cstdio>
#define REP(i,n) for(int i = 0; i<n; i++)
using namespace std;

int gcd(int a, int b){
  if(!b)return a; else return gcd(b,a%b);
} 

int main(){
  int cases;
  scanf("%d",&cases);
  REP(CID,cases){
    long long N;
    int pD,pG;
    scanf("%lld%d%d",&N,&pD,&pG);
    int K = pD, L = 100-pD;
    int D = gcd(K,L);
    K/=D;
    L/=D;
    if(K+L<=N && (pD == 100 || pG != 100) && (pD == 0 || pG != 0))
      printf("Case #%d: Possible\n", CID+1);
    else printf("Case #%d: Broken\n", CID+1);
  }
}
