#include <cstdio>
#include <cstring>

int C[1000];
int N;
char l[1001];
int X[1001];
int S[1001];

void loadNext() {
  fscanf(stdin, "%d", &N);
  for(int i=0; i<N; i++) {
    fscanf(stdin, " %d", &(C[i]));
    //fprintf(stdout, "N: %d i: %d p: %d r: %c\n", N, i, P[i], R[i]);  
  }
}

inline int first0() {
  for(int i=0; i<=N;i++) {
    if (!(l[i])) return i;
  }
  return N;
}


int f() {
  loadNext();
  memset(l, 0, N+1);
  
  X[0]=C[0];
  S[0]=0;
  for(int i=1; i<=N; i++) {
    X[i]=X[i-1]^C[i];
    S[i]=S[i-1]+C[i-1];
  }
  unsigned int left=S[N];
  unsigned int x=0;
  int sum=S[N];
  int result=sum+1;
  int ind=first0();
  while(ind < N) {
    memset(l,0,ind);
    l[ind]=1;
    left+=S[ind];
    left-=C[ind];
    x=x^X[ind];
    if (left==x) {
      if (result>left && left>0) result=left;
    }
    //c++;
    if (ind>30) printf("ind: %d left: %d x: %d\n", ind, left, x);
    ind=first0();
  }
  return (sum-result);
}

int main(int argc, char **argv) {
  int T;
  fscanf(stdin, "%d", &T);
  for(int i=0; i<T; i++) {
    int r=f();
    if (r==-1) {
      fprintf(stdout, "Case #%d: NO\n", i+1);
    }
    else {
      fprintf(stdout, "Case #%d: %d\n", i+1, r);
    }
  }
  return 0;
}
