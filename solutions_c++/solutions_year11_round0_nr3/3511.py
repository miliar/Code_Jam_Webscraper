#include <stdio.h>
using namespace std;

int Min(long ii, long jj){
    if (ii<jj) return ii;
    else return jj;
}

int main(){
    long T, C, N, Sum, Minn, kk, Ans;
    int ii,jj,tot(0);
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    scanf("%d", &T);
    while (T>0){
          tot ++; T--; Minn = 9999999; Ans = 0; Sum = 0;
          scanf("%d", &N);
          for (ii=0; ii<N; ii++){
              scanf("%d", &kk);
              Sum += kk;
              Ans = Ans xor kk;
              //printf("%d", Ans);
              Minn = Min(kk, Minn);
          }
          if (Ans != 0) printf("Case #%d: NO\n", tot);
          else printf("Case #%d: %d\n", tot, Sum-Minn);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
