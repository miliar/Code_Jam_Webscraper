#include<cstdio>
#include<iostream>
#include<vector>
#include<cctype>
#include<string>
#include<sstream>
#include<algorithm>
#include<cstring>

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()

using namespace std;

#define MAXN 15
int A[MAXN];
int main(){
  int T,CASE = 1;
  scanf("%d",&T);
  while(T--){
    int N,ans = 0;
    scanf("%d",&N);
    REP(i,N) scanf("%d",A+i);
    REP(i,(1<<N)-1){
      if(i==0) continue;
      int t = i,sum1 = 0,sum2 = 0;
      int rsum1 = 0,rsum2 = 0; 
      REP(j,N){
	if(t & 1){
	  sum1 ^= A[j];
	  rsum1 += A[j];
	}
	else {
	  sum2 ^= A[j];
	  rsum2 += A[j];
	}
	t>>=1;
      }
      if(sum1 == sum2) ans = max(ans,max(rsum1,rsum2));
    }
    if(!ans) printf("Case #%d: NO\n",CASE++);
    else printf("Case #%d: %d\n",CASE++,ans);
  }
  return 0;
}
