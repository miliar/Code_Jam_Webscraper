#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void go() {
 int n,k;
 scanf("%i%i",&n,&k);
 if (!(++k % (1<<n))) printf("ON\n");
 else printf("OFF\n");
}
int main() {
 int n;
 scanf("%i", &n);
 for (int i=0;i<n;i++) printf("Case #%i: ", i+1), go();
}
