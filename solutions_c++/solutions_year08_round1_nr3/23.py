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

void matmul(int m[2][2], int mm[2][2]) {
 int a[2][2] = {0};
 FOR(i,2) FOR(j,2) FOR(k,2) a[i][j] += m[i][k] * mm[k][j];
 FOR(i,2) FOR(j,2) m[i][j]=(2000+a[i][j])%2000;
}

void matpow(int m[2][2], int n) {
 if (n==0) {
  m[0][0]=m[1][1]=1;
  m[1][0] = m[0][1] = 0;
  return;
 }
 if (n==1) return;
 int a[2][2], b[2][2];
 memcpy(a,m,sizeof(a));
 memcpy(b,m,sizeof(b));
 matpow(b, n&1);
 matpow(a, n/2);
 matmul(a,a);
 matmul(a,b);
 memcpy(m,a,sizeof(a));
}

void doit() {
 int n;
 scanf("%i", &n);
 int m[2][2];
 m[0][0]=m[1][1] = 3; m[0][1] = 5; m[1][0] = 1;
 matpow(m,n);
 m[0][0] *= 2;
 m[0][0] += 999; m[0][0] %= 1000;
 if (n==0) printf("001\n");
 else printf("%03i\n", m[0][0]);
}


int main() {
 int c;
 scanf("%i", &c);
 FOR(i,c) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
