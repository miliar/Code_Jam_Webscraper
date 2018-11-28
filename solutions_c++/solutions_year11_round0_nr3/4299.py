#include <cstdio>
#include <cstdlib>

int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
       int N, minC, xorC, sumC;
       scanf("%d", &N);
       minC=1000000000;
       sumC=xorC=0;
       for (int n=1; n<=N; n++) {
         int C;
         scanf("%d", &C);
	 xorC=xorC^C;
	 sumC+=C;
	 if (C<minC) minC=C;
       }
       printf("Case #%d: ", t);
       if (xorC==0) printf("%d\n", sumC-minC);
       else printf("NO\n");
    }
    return 0;
}
