#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <set>

using namespace std;

double weight[200];
int fverd[200], ffalso[200];
char feature[200][100];
char atr[100];

int natr, nanimal, matr;
char tudo[1000123];

set<string> M;

char *parse(char *l, int p) {
  int inc0, inc=-1;

  feature[p][0] = '\0';

  sscanf(l, " ( %lf%n %[^() ]%n", &weight[p], &inc0, feature[p], &inc);
  if(inc!=-1) l+=inc;
  else l+=inc0;
  //printf(" <<%c>>\n", *l);

  if(feature[p][0] == '\0') {
    fverd[p] = ffalso[p] = -1;

    while(*l != ')' && *l != '\0') l++;
    //printf(" >>%c<<\n", *(l+1));
    return l+1;
  } else {
    fverd[p] = ++natr;
    l = parse(l, natr);

    ffalso[p] = ++natr;
    l = parse(l, natr);

    while(*l != ')' && *l != '\0') l++;
    //printf(" //%c//\n", *(l+1));
    return l+1;
  }
}

double calc(int k) {
  if(fverd[k] == -1) return weight[k];

  if(M.find( string(feature[k]) ) != M.end())
    return weight[k] * calc(fverd[k]);
  else return weight[k] * calc(ffalso[k]);
}

int main() {
  int nt,nt0;
  int i, nline;
  char *line;

  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; nt++) {
    natr = 0;
    tudo[0] = '\0';

    scanf(" %d", &nline);
    for(i=0 ; i<nline ; i++) {
      scanf(" %a[^\r\n]", &line);
      sprintf(tudo+strlen(tudo), line);
      free(line);
    }

    parse(tudo, 0);

    printf("Case #%d:\n", nt);

    scanf(" %d", &nanimal);
    while(nanimal--) {
      scanf(" %*s %d", &matr);

      M.clear();
      for(i=0 ; i<matr ; i++) {
	scanf(" %s", atr);
	M.insert(string(atr));
      }

      printf("%.7lf\n", calc(0));
    }
  }

  return 0;
}
