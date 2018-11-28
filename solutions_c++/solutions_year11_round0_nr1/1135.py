#include <stdio.h>
#include <algorithm>
using namespace std;

char op[5];
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    int n,ti=0,p,po=1,pb=1,to=0,tb=0,tt;
    scanf("%d", &n);
    for(int i=0; i<n; ++i) {
      scanf("%s%d",op,&p);
      if(op[0]=='O') to=ti=max(abs(po-p)+to, ti)+1, po=p;
      else tb=ti=max(abs(pb-p)+tb, ti)+1, pb=p;
      
//      printf("%d %d %d %d %d\n", i, po, to, pb, tb);
    }
    printf("Case #%d: %d\n", cas, ti);
  }
  return 0;
}

