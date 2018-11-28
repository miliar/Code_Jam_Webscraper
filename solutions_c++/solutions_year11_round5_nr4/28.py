#include <cstdio>
#include <cmath>
using namespace std;
int t,tt,i;
char s[64];
long long d;
bool q;
void rec(int l, long long e) {
  if (s[l]==0) {
    d=sqrt(e+1e-8);
    if (d*d==e) puts(s);
    return;
  }
  if (s[l]=='?') {
    s[l]='0'; rec(l+1,e*2);
    if (q) return;
    s[l]='1'; rec(l+1,e*2+1);
    s[l]='?';
  } else rec(l+1,e*2+s[l]-'0');
}
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%s",s);
    printf("Case #%d: ",t);
    q=false; rec(0,0);
  }
  return 0;
}
