#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 2005
using namespace std;

typedef long long int ll;
int testcase,N,A[MAXN],H[MAXN],cnt;
bool cannot;

bool fail(int i,int j,int k){
  return ((ll)(H[j] - H[i]) * (ll)(k-i) > (ll)(H[k] - H[i]) * (ll)(j - i)) || ((ll)(H[j] - H[i]) * (ll)(k-i) == (ll)(H[k] - H[i]) * (ll)(j - i) && j < k);
}

int main(){
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C1.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf("%d",&N);
    memset(H,0,sizeof(H));
    for(int i=1;i<N;++i) scanf("%d",&A[i]);
    cannot = cnt = 0;
    while(1){
      ++cnt;
      if(cnt >= 10000000){
        cannot = 1;
        break;
      }
      for(int i=1;i<N;++i)
        for(int j=i+1;j<=N;++j)
          if(fail(i,j,A[i])){
            ++H[A[i]];
            goto end;
          }
      break;
      end:;
      
    }
    printf("Case #%d: ",TC);
    if(cannot) printf("Impossible\n");
    else{
      for(int i=1;i<=N;++i) printf("%d ",H[i]);
      printf("\n");
    }
  }
 // system("pause");
}
