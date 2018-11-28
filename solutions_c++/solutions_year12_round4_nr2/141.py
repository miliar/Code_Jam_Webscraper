#include <iostream>
#include <cstdio>
#define MAXN 1005
using namespace std;

int testcase,N,W,L,R[MAXN],A[MAXN],cur,t,t1,t2;
int loc[MAXN][2];
bool change;

bool cmp(int a,int b){return R[a] > R[b];}

int main(){
  freopen("B-large.in","r",stdin);
  freopen("B.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf("%d%d%d",&N,&W,&L);
    for(int i=0;i<N;++i) scanf("%d",&R[i]);
    change = 0;
    if(W > L){
      change = 1;
      swap(W,L);
    }
    for(int i=0;i<N;++i) A[i] = i;
    sort(A,A+N,cmp);
    memset(loc,0,sizeof(loc));
    cur = t = 0;
    while(cur < N){
      if(t == 0){
        t1 = R[A[cur]];
        loc[A[cur]][change] = 0, loc[A[cur]][!change] = 0;
        t += R[A[cur]];
      }
      else if(t + R[A[cur]] <= L){
        loc[A[cur]][change] = 0, loc[A[cur]][!change] = t + R[A[cur]];
        t += 2*R[A[cur]];
      }
      else break;
      ++cur;
    }
    t = L;
    while(cur < N){
      if(t == L){
        loc[A[cur]][change] = W, loc[A[cur]][!change] = L;
        t -= R[A[cur]];
      }
      else if(t - R[A[cur]] >= 0){
        loc[A[cur]][change] = W, loc[A[cur]][!change] = t - R[A[cur]];
        t -= 2*R[A[cur]];
      }
      else break;
      ++cur;
    }
    t = 0;
    while(cur < N){
      if(t == 0){
        t2 = t1 + 2*R[A[cur]];
        loc[A[cur]][change] = t1 + R[A[cur]], loc[A[cur]][!change] = 0;
        t += R[A[cur]];
      }
      else if(t + R[A[cur]] <= L){
        loc[A[cur]][change] = t1 + R[A[cur]], loc[A[cur]][!change] = t + R[A[cur]];
        t += 2*R[A[cur]];
      }
      else break;
      ++cur;
    }
    while(cur < N){
      t = 0;
      t1 = t2;
      while(cur < N){
        if(t == 0){
          t2 = t1 + 2*R[A[cur]];
          loc[A[cur]][change] = t1 + R[A[cur]], loc[A[cur]][!change] = 0;
          t += R[A[cur]];
        }
        else if(t + R[A[cur]] <= L){
          loc[A[cur]][change] = t1 + R[A[cur]], loc[A[cur]][!change] = t + R[A[cur]];
          t += 2*R[A[cur]];
        }
        else break;
        ++cur;
      }
    }
    printf("Case #%d: ",TC);
    for(int i=0;i<N;++i) printf("%d %d ",loc[i][0],loc[i][1]);
    printf("\n");
  }
  //system("pause");
}
