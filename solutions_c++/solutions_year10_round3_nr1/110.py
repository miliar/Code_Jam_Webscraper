#include<iostream>
#include<cmath>
#include<string>
using namespace std;
const int Maxn=1000+10;
int T,N,A[Maxn],B[Maxn];
int main(){
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
    int t=0;
    scanf("%d", &T);
    while (T--){
          scanf("%d", &N);
          int Ans=0;
          for (int i=1;i<=N;i++)
          scanf("%d%d" , &A[i], &B[i]);
          for (int i=1;i<=N;i++){
              for (int j=i+1;j<=N;j++){
                  if (A[i]>A[j] && B[i]<B[j]) Ans++;else
                  if (A[i]<A[j] && B[i]>B[j]) Ans++;
              }
          }
          printf("Case #%d: %d\n",++t,Ans);
    }
    return 0;
}
