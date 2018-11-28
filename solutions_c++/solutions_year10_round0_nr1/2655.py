#include <cstdio>

long mp(long a) {
  long r=1;
  for(long i=0;i<a;i++)
    r*=2;
  return r;
}

int fc(long N, long K) {
  long p=mp(N);
  return ((K+1)%p)==0;
}

int main(int argc, char **argv) {
  long T;
  fscanf(stdin, "%ld", &T);
  for(long i=0; i<T; i++) {
    long N,K;
    fscanf(stdin, "%ld %ld", &N, &K);
    int r=fc(N,K);
    fprintf(stdout, "Case #%ld: %s\n", i+1, (r?"ON":"OFF"));
  }
  return 0;
}
