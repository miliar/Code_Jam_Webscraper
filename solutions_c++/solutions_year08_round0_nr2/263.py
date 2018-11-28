#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

int n;
int t;
int na, nb;
int va1[1010];
int va2[1010];
int vb1[1010];
int vb2[1010];
int ilea, ileb;

int mina, minb;

int wczytaj(void) {
 char s[1000];
 scanf("%s",s);
 int ret=0;
 ret = (s[0]-'0') * 10 + (s[1]-'0');
 ret *= 60;
 ret += (s[3]-'0') * 10 + (s[4]-'0');
 return ret;
}

void solve(int casenr) {
 scanf("%d", &t);
 scanf("%d", &na);
 scanf("%d", &nb);
 for(int i=0; i<na; i++) {
  va1[i] = wczytaj();
  va2[i] = wczytaj() + t;
 }
 for(int i=0; i<nb; i++) {
  vb1[i] = wczytaj();
  vb2[i] = wczytaj() + t;
 }
 ilea=ileb=0;
 mina=minb=0;
 for(int tt=0; tt<= 60*30; tt++) {
  for(int i=0; i<na; i++)
  if(va2[i]==tt) ileb++;
  for(int i=0; i<nb; i++)
  if(vb2[i]==tt) ilea++;

  for(int i=0; i<na; i++)
  if(va1[i]==tt) ilea--;
  for(int i=0; i<nb; i++)
  if(vb1[i]==tt) ileb--;
  if (ilea<mina) mina = ilea;
  if (ileb<minb) minb = ileb;
 }
 mina = 0 - mina;
 minb = 0 - minb;
 printf("Case #%d: %d %d\n", casenr, mina, minb);
}

int main(void) {
 scanf("%d",&n);
 for(int yy=0; yy<n; yy++) solve(yy+1);
 return 0;
}
