#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORI(i,s) FOR(i,(signed)s.size())

int gettime() {
 int h,m;
 scanf("%d:%d",&h,&m);
 return 60*h+m;
}
 int tra[66666], trb[66666];
void doit() {
 int t;
 int na, nb;
 scanf("%i%i%i", &t, &na, &nb);
 memset(tra,0,sizeof(tra));
 memset(trb,0,sizeof(trb));
 FOR(i,na) {
  int t1 = gettime(); int t2=gettime();
  tra[t1]--; trb[t2+t]++;
 }
 FOR(i,nb) {
  int t1 = gettime(); int t2=gettime();
  trb[t1]--; tra[t2+t]++;
 }
 FOR(i,66600) tra[i+1] += tra[i];
 FOR(i,66600) trb[i+1] += trb[i];
 int aa=0, ab=0;
 FOR(i,66600) aa >?= -tra[i];
 FOR(i,66600) ab >?= -trb[i];
 printf("%i %i\n", aa, ab);
}

int main() {
 int c;
 scanf("%i", &c);
 FOR(i,c) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
