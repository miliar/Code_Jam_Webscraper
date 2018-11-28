#include<stdio.h>

int t;

int main() {
  scanf("%d",&t);
  for(int test=1;test<=t;test++) {
    int n;
    int a[1000], b[1000];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%d %d",&a[i], &b[i]);
    int ret = 0;
    for(int i=0;i<n;i++) {
      for(int j=i+1;j<n;j++) {
        if((a[i] > a[j] && b[i] < b[j]) || (a[i] < a[j] && b[i] > b[j]))
          ret++;
        }
    }
    printf("Case #%d: %d\n",test,ret);
  }
  return 0;
}
    
