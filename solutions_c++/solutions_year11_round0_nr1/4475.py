#include <cstdio>

int P[100];
char R[100];
int N;

void loadNext() {
  fscanf(stdin, "%d", &N);
  for(int i=0; i<N; i++) {
    fscanf(stdin, " %c %d", &(R[i]), &(P[i]));
    //fprintf(stdout, "N: %d i: %d p: %d r: %c\n", N, i, P[i], R[i]);  
  }
  
}

int nextTarget(int from, char robot) {
  if (from > 100) {
    return from;
  }
  if (from == -2) from = -1;
  for(int i=from+1; i<N; i++) {
    if (R[i] == robot) {
      return i;
    }
  }
  return 101;
}

int f() {
  loadNext();
  int apos[2];
  apos[0] =  apos[1] = 1;
  int tind[2];
  tind[0] = tind[1] = -1;
  tind[0] = nextTarget(tind[0], 'O');
  tind[1] = nextTarget(tind[1], 'B');
  int sec=0;
  while(tind[0]<=100 || tind[1]<=100) {
    bool i1 = false;
    for(int i=0; i<2; i++) {
      if (tind[i] > 100) continue;
      if (apos[i] == P[tind[i]]) {
        //button press
        if (tind[i]<tind[1-i] && (i!=1 || !i1)) {
          tind[i] = nextTarget(tind[i], (i==0?'O':'B'));
          //fprintf(stdout, "i: %d button press\n", i);
          i1=true;
        }
        else {
          //fprintf(stdout, "i: %d waiting\n", i);
        }
      }
      else {
        if (apos[i]<P[tind[i]]) {
          //fprintf(stdout, "i: %d step forward\n", i);
          apos[i]++;
        }
        else {
          //fprintf(stdout, "i: %d step backward\n", i);
          apos[i]--;
        }
      }  
    }  
    sec++;
    //fprintf(stdout, "sec: %d p1: %d p2: %d t1: %d t2: %d\n", sec, apos[0], apos[1], tind[0], tind[1]);
  }
  return sec;
}

int main(int argc, char **argv) {
  int T;
  fscanf(stdin, "%d", &T);
  for(int i=0; i<T; i++) {
    int r=f();
    fprintf(stdout, "Case #%d: %d\n", i+1, r);
  }
  return 0;
}
