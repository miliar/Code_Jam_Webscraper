#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
using namespace std;
#define INF (1<<28)
int D,I,M,n,a[110],f[110][300];

int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%d%d%d%d",&D,&I,&M,&n);
    for (int i=0; i<n; i++) scanf("%d",&a[i]);
    for (int i=0; i<n; i++){
      for (int j=0; j<=255; j++) f[i][j]=INF;
      f[i][a[i]]=D*i;
    }
    int b[300];
    for (int i=0; i<256; i++){
      f[0][i] = min(f[0][i],abs(a[0]-i));
      b[i] = f[0][i];
    }
 //   for (int i=0; i<20; i++) printf("%d ",f[0][i]); printf("\n");

    if (M>0){
      for (int j=0; j<256; j++){
        for (int k=0; k<256; k++){
          if (j==k) continue;
          b[j] = min(b[j], f[0][k] + I*((abs(j-k)+M-1)/M));
        }
      }
      for (int j=0; j<256; j++) f[0][j] = b[j];
    }
    //  for (int i=0; i<20; i++) printf("%d ",f[0][i]); printf("\n");

    for (int i=1; i<n; i++){
      int b[300];
      for (int j=0; j<256; j++){
        for (int k=max(0,j-M); k<=min(255,j+M); k++){
          f[i][j] = min(f[i][j], f[i-1][k]+abs(j-a[i]));
        }
        b[j] = f[i][j];
      }
      if (M>0){
        for (int j=0; j<256; j++){
          for (int k=0; k<256; k++){
            b[j] = min(b[j], f[i][k] + I*((abs(j-k)+M-1)/M));
          }
        }
        for (int j=0; j<256; j++) f[i][j] = b[j];
      }

      for (int j=0; j<256; j++){
        f[i][j] = min(f[i][j], f[i-1][j]+D);
      }
    }
    int ans=INF;
    for (int i=0; i<n; i++){
      for (int j=0; j<256; j++){
        ans = min(ans, f[i][j]+D*(n-i-1));
      }
    }
    printf("Case #%d: %d\n",tt,ans);
  }
  return 0;
}
