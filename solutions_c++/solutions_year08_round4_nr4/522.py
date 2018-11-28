#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int k;
int perm[10];
int tS;



int comp(char *stt) {
  register int i;
  int ret=1;
  for (i=1;i<tS;i++) {
    if (stt[i]!=stt[i-1]) ret++;
  }
  return ret;
}

int main () {
  int n, t,i;
  char s[1200];
  char st[1200];
  int best,x;

  scanf("%d", &n);
  for (t=1;t<=n;t++) {
    scanf("%d%s",&k, s);
    tS=strlen(s);
    best=1000000;
    for (i=0;i<k;i++) {
      perm[i]=i;
    }
    do {
      for (i=0;i<tS;i++) {
	st[i]=s[k*(i/k)+perm[i%k]];
      }
      st[tS]='\0';
      x=comp(st);
      //printf("%s\n",st);
      if (x<best) best=x;
    } while ( next_permutation(perm, perm+k) );
    printf("Case #%d: %d\n",t,best);
  }

  return 0;
}
