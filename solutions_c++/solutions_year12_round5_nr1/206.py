#include <iostream>
#include <cstdio>
#include <algorithm>
#define MAXN 1005
using namespace std;

int testcase,N;
int L[MAXN],P[MAXN],A[MAXN];

bool cmp(int a,int b){
  if(P[a] != P[b]) return P[a] > P[b];
  return a < b;
}

int main(){
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf("%d",&N);
    for(int i=1;i<=N;++i) scanf("%d",&L[i]);
    for(int i=1;i<=N;++i) scanf("%d",&P[i]);
    for(int i=1;i<=N;++i) A[i] = i;
    sort(A+1,A+N+1,cmp);
    printf("Case #%d: ",TC);
    for(int i=1;i<=N;++i) printf("%d ",A[i]-1);
    printf("\n");
  }
}
