#include <cstdio>

int main() {
  int d;
  scanf("%d",&d);
  for(int i=1;i<=d;++i) {
    int n,k;
    scanf("%d %d",&n,&k);
    int mask=(1<<n)-1;
    printf("Case #%d: %s\n",i,((k&mask)==mask)?"ON":"OFF");
  }
  return 0;
}
