#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;
typedef long long ll;

int A[10000], B[10000];
int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; t++){
    int N;
    scanf("%d", &N);
    for(int i=0; i<N; i++) scanf("%d", &A[i]);
    for(int i=0; i<N; i++) scanf("%d", &B[i]);
    sort(A, A+N);
    sort(B, B+N);
    reverse(B, B+N);
    ll ans=0;
    for(int i=0; i<N; i++){
      ans+=ll(A[i])*ll(B[i]);
    }
    printf("Case #%d: %Ld\n", t, ans);
  }
  return 0;
}
