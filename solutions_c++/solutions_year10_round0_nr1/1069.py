#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)

void solve(int _case){
 char s[2][10]={"OFF","ON"};
 unsigned int x=1;
 unsigned int n,k;
 scanf("%u %u",&n,&k);
 FOR(q,(int)n) {
    x = x && (k%2);
    k/=2;
 }

printf("Case #%d: %s\n", _case, s[x]);

}

int main(){
 int t;
 scanf("%d",&t);
 FOR(q,t) solve(q+1);
}
