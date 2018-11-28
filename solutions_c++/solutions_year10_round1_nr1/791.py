#include<iostream>
//#include<fstream>
#include<sstream>
#include<unistd.h>
#include<complex>
#include<valarray>
#include<numeric>
#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<time.h>
using namespace std;
#define CLR(X) memset(X,0,sizeof(X))

  int T;
  int K, N;
  char t[51][51];
  char q[51][51];

inline int check(int j, int jj, int a, int b){
  int ret=1;
  char x=q[j][jj];
  for(int i=1; i<=K-1; i++) if(x!=q[j+i*a][jj+i*b]) ret=0;
  return ret;
}

int main(){
  char z;
  scanf("%d", &T);
  for(int i=1; i<=T; i++){
    scanf("%d %d", &N, &K);
    CLR(t);
    CLR(q);
    for(int j=0; j<N; j++) {scanf("%c", &z);for(int jj=0; jj<N; jj++) scanf("%c", &t[j][jj]); }
    for(int j=N-1; j>=0; j--) {int p=0; for(int jj=N-1; jj>=0; jj--){
      if(t[j][jj]!='.'){
        q[N-1-j][p++]=t[j][jj];
      }
    }}
    int r=0,b=0;
    for(int j=0; j<N-K+1; j++) for(int jj=0; jj<N; jj++) if(check(j,jj,1,0)){
      if(q[j][jj]=='R') r=1;
      if(q[j][jj]=='B') b=1;
    }
    for(int j=0; j<N; j++) for(int jj=0; jj<N-K+1; jj++) if(check(j,jj,0,1)){
      if(q[j][jj]=='R') r=1;
      if(q[j][jj]=='B') b=1;
    }
    for(int j=0; j<N-K+1; j++) for(int jj=0; jj<N-K+1; jj++) if(check(j,jj,1,1)){
      if(q[j][jj]=='R') r=1;
      if(q[j][jj]=='B') b=1;
    }
    for(int j=N-1; j>=K-1; j--) for(int jj=0; jj<N-K+1; jj++) if(check(j,jj,-1,1)){
      if(q[j][jj]=='R') r=1;
      if(q[j][jj]=='B') b=1;
    }
    if(r&&b) printf("Case #%d: Both\n",i);
    else if(r) printf("Case #%d: Red\n",i);
    else if(b) printf("Case #%d: Blue\n",i);
    else printf("Case #%d: Neither\n",i);
  }
  return 0;
}
