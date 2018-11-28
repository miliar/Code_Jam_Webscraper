#include <cstdio>
#include <iostream>
#include <algorithm>

int gcds(int a, int b, int k, int l) {
  if (a < b) {
    int t = b; b = a; a = t;
  }
  if (b == 0) return k;
  if (a/b>1) return l%2;
  return(gcds(b,a%b,k,l+1));
}

int main(void) {
  int tc;
  scanf(" %d",&tc);
  for(int c=1;c<=tc;c++) {
    int a1,b1,a2,b2;
    int v=0;
    scanf(" %d %d %d %d",&a1,&a2,&b1,&b2);
    for(int a=a1;a<=a2;a++)
      for(int b=b1;b<=b2;b++) {
	v+= gcds(a,b,0,1);
      }
    printf("Case #%d: %d\n",c,v);
  }
  return(0);
}
