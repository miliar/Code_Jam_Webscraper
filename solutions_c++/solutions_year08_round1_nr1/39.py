#include<stdio.h>
#include<stdlib.h>

#define MAXN 900


int T;
int n;

long long int values[2][MAXN];
long long int ans;

int compare(const void *a, const void *b){
  return *(int *)a - *(int *)b;
}

int main(){
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
      scanf("%d", &values[0][i]);
    }
    for(int i = 0; i < n; i++){
      scanf("%d", &values[1][i]);
    }
    qsort(values[0], n, sizeof(values[0][0]), compare);
    qsort(values[1], n, sizeof(values[1][0]), compare);
    ans = 0;
    for(int i = 0; i < n; i++){
      ans += values[0][i] * values[1][n-1-i];
    }
    printf("%d\n", ans);
  }
}
