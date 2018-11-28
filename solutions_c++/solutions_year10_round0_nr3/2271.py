#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>


using namespace std;

int main(int argc, char **argv) {

  int i,j,r,k,n,T,v;
  char s[4096],*p;
  int q[1000], qpos=0, spos;

  fgets(s,4095,stdin);
  sscanf(s,"%d",&T);

  for(i=1;i<=T;i++) {
    scanf("%d %d %d\n",&r,&k,&n);
    fgets(s,4095,stdin);
    j=0;
    p=strtok(s," \t\r\n");
    while(j!=n) {
      q[j++] = atoi(p);
      p = strtok(NULL," \t\r\n");
    }
    v = 0;
    qpos = 0;

    //printf("r=%d k=%d n=%d\n",r,k,n);

    int pir;
    while(r) {
      pir = 0;
      spos = qpos;
      while(pir + q[qpos] <= k) {
	pir += q[qpos];
	qpos = (qpos + 1) % n;
	if (qpos == spos) break;
      }
      v += pir;
      r--;
    }

    printf("Case #%d: %d\n",i,v);
  }

  return 0;
}
