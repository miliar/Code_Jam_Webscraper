#include <stdio.h>
int main(){ int c,n,k; scanf("%i ", &c); for (int i=1;i<=c;i++)  scanf("%i %i ", &n, &k), printf("Case #%i: %s\n", i, ((k+1)&((1<<n)-1)) ? "OFF":"ON"); }
