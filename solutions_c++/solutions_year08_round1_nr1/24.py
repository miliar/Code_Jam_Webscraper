#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORI(i,s) FOR(i,s.size())
#define BEND(x) (x).begin(),(x).end()
#define ll long long

void doit() {
 int n;
 vector<ll> a, b;
 scanf("%i", &n);
 FOR(i,n) { int k; scanf("%i", &k); a.push_back(k); }
 FOR(i,n) { int k; scanf("%i", &k); b.push_back(k); }
 sort(BEND(a)); sort(BEND(b));
 ll ans = 0;
 FOR(i,n) ans += a[i] * b[n-i-1];
 printf("%lli\n", ans);
}


int main() {
 int c;
 scanf("%i", &c);
 FOR(i,c) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
