#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)

#define MAXN 2000
#define MAXS 60

char data[MAXN][MAXS];
void create(int _case) {
    int n;
    scanf("%d",&n);
    FOR(q,n)
        scanf("%s", data[q]);

    printf("a = %s-%s\n", data[1] , data[0]);
    FOR(q,n) if (q>1) printf("a = gcd(abs(a), abs(%s-%s))\n", data[q],
            data[0]);
    printf("a = mod(-%s, abs(a))\n", data[0]);
    printf("print \"Case #%d: \",a,\"\\n\"\n", _case);



}

int main(){
  int t;
  scanf("%d", &t);
  FOR(q,t) create(q+1);
  printf("quit");
}
