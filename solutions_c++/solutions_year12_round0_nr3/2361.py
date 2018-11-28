#include<algorithm>
#include<cstdio>
#include<vector>
#include<cmath>
#include<cstring>
#define INF 2000000000
#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define FORD(i, a, b) for(int i = (a); i >= (b); i--)
#define PI pair<int, int>
#define ST first
#define ND second
#define CLR(a, b) memset(a, b, sizeof(a))
#ifdef DEBUG
  #define DBG printf
#else
  #define DBG
#endif
using namespace std;

int ex[] = {10, 100, 1000, 10000, 100000, 1000000, 10000000};

int lenof(int x){
  int p = 10000000;
  int res = 7;
  while( x/p == 0) {p/=10; res--;}
  return res;
}

int main(){
  int t, A, B;
  scanf("%d",&t);
  int casenum = 0;
  while(t--){
    casenum++;
    int res = 0, k, len;
    scanf("%d %d",&A, &B);
    for(int i = A; i <= B; i++){
      k = i;
      len = lenof(i);
      REP(j, len){
        k = i / ex[j] + (i % ex[j]) * ex[len - j - 1];
        //printf("\n");
        //printf("(%d %d %d), %d %d\n", len, ex[j], ex[len-j-1],i, k);
        if( k == i) break;
        if( lenof(k) == lenof(i) && k > i && k >= A && k <= B){
          res++;
          //printf("%d %d\n",k, i);
        }
      }
    }
    printf("Case #%d: %d\n",casenum, res);
  }

  return 0;
}
