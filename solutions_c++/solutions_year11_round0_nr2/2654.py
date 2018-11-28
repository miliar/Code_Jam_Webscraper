#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <vector>
#include <iostream>

const char *tok = " \t\r\n";

using namespace std;

char combine[36*3+1];
char oppose[28*2+1];
int nc, no;
vector<char> work;

void comb() {
  int i,l;
  l = work.size();
  for(i=0;i<nc;i++) {
    if (work[l-2] == combine[3*i] && work[l-1] == combine[3*i+1] ||
	work[l-1] == combine[3*i] && work[l-2] == combine[3*i+1]) {
      work[l-2] = combine[3*i+2];
      work.pop_back();
      comb();
      break;
    }
  }
}

void opp() {
  int i,j,l;
  l = work.size();
  for(i=0;i<no;i++)
    for(j=0;j<l-1;j++) {
      if (work[l-1] == oppose[2*i] && work[j] == oppose[2*i+1] ||
	  work[l-1] == oppose[2*i+1] && work[j] == oppose[2*i]) {
	work.clear();
	return;
      }
    }
}

void invoke(char c) {
  work.push_back(c);
  if (work.size() < 2) return;
  comb();
  opp();
}

int main() {
  int T,C,D,N;
  int i,j;
  char *p;
  char s[512];

  scanf("%d\n",&T);

  for(i=1;i<=T;i++) {
    combine[0] = 0;
    oppose[0] = 0;
    work.clear();

    fgets(s,512,stdin);
    p = strtok(s,tok);
    C = atoi(p);

    for(j=0;j<C;j++) {
      p = strtok(NULL,tok);
      strcat(combine,p);
    }

    p = strtok(NULL,tok);
    D = atoi(p);

    for(j=0;j<D;j++) {
      p = strtok(NULL,tok);
      strcat(oppose,p);
    }

    nc = strlen(combine) / 3;
    no = strlen(oppose) / 2;

    p = strtok(NULL,tok);
    N = atoi(p);

    //printf("C=%d D=%d N=%d\n",C,D,N);

    p = strtok(NULL,tok);
    for(j=0;j<N;j++)
      invoke(p[j]);

    printf("Case #%d: [",i);
    for(j=0;j<work.size();j++) {
      printf("%c",work[j]);
      if (j<work.size()-1)
	printf(", ");
    }
    printf("]\n");

  }

  return 0;
}
