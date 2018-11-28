#include <stdio.h>
#include <stdlib.h>

#define ll long long

ll p[1024];
int n;
ll k,r;
int caseno;
int to[1024];
ll val[1024];

#define FOR(i,n) for (int i=0;i<n;i++)

void square() {
 ll to2[1024], val2[1024];
 FOR(i,n) to2[i] = to[to[i]], val2[i] = val[i]+val[to[i]];
 FOR(i,n) to[i]=to2[i];
 FOR(i,n) val[i]=val2[i];
}

void getto(int x) {
 ll tot = 0;
 int i = 0;
 for (i=0;i<n;i++) {
  tot += p[(i+x)%n];
  if (tot > k) { tot -= p[(i+x)%n]; break; }
 }
 to[x] = (x+i)%n;
 val[x] = tot;
}

void doit() {
 scanf("%lli%lli%i", &r,&k,&n);
 FOR(i,n) scanf("%lli", p+i);
 FOR(i,n) getto(i);
 ll ans = 0;
 int pos = 0;
 while (r) {
  if (r & 1) { ans += val[pos]; pos = to[pos]; }
  square(); r/=2;
 }
 printf("Case #%i: %lli\n", ++caseno, ans);
}

int main() {
 int n;
 scanf("%i", &n);
 while(n--)doit();
}

