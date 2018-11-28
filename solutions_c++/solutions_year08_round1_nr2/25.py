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


int malted[2048];
vector<int> likes[2048];
int maltflav[2048];
int nf, nc;

void doit() {
 scanf("%i %i", &nf, &nc); nf++;
 memset(maltflav,-1,sizeof(maltflav));
 memset(malted,0,sizeof(malted));
 FOR(i,2048) likes[i].clear();

 FOR(i,nc) {
  int k;
  scanf("%i", &k);
  while (k--) {
   int x, y;
   scanf("%i %i", &x, &y);
   if (y==1) maltflav[i] = x;
   else likes[i].push_back(x);
  }
 }
 FOR(zzz,2222) {
  FOR(i,nc) {
   FORI(j,likes[i]) if (!malted[likes[i][j]]) goto happyface;
   if (maltflav[i] == -1) {
    printf(" IMPOSSIBLE\n");
    return;
   }
   malted[maltflav[i]] = 1;
   happyface:;
  }
 }
 FOR(i,nf) if(i) printf(" %i", malted[i]);
 printf("\n");
}


int main() {
 int c;
 scanf("%i", &c);
 FOR(i,c) {
  printf("Case #%i:", i+1);
  doit();
 }
}
