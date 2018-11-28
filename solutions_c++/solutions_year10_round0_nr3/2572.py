#include <cstdio>

long long gi[1000];
long long k;
long N, Nc=0;
long long R, Rc=0;

long long fillNext() {
  long long f=gi[Nc];
  long sN=Nc;
  while(f<=k) {
    Nc=(Nc+1)%N;
    f+=gi[Nc];
    if (Nc==sN) break;
  }
  f-=gi[Nc];
  //fprintf(stdout, "Rc-%lld: %lld\n", Rc, f);
  return f;
}

int ci(long c) {
  Rc=0;Nc=0;
  fscanf(stdin, "%lld %lld %ld", &R, &k, &N);
  for(long i=0; i<N; i++) {
    fscanf(stdin, "%lld", &(gi[i]));
  }
  
  long long y=0;
  
  while(Rc<R) {
    y+=fillNext();
    Rc++;
    if (Nc==0) break;
  }
  long long d=R/Rc;
  y*=d;
  Rc*=d;
  
  while(Rc<R) {
    y+=fillNext();
    Rc++;
  }

  fprintf(stdout, "Case #%ld: %lld\n", c, y);
}

int main(int argc, char **argv) {
  long T;
  fscanf(stdin, "%ld", &T);
  for(long i=0; i<T; i++) {
    ci(i+1);
    
  }
  return 0;
}
