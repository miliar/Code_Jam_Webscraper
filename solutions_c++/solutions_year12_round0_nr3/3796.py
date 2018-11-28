#include <cstdio>
#include <cmath>
#include <set>
#include <functional>

typedef long long unsigned int lli;

int digits(int x) {
  int c = 1;
  while(x>=10) {
    c++;
    x /= 10;
  }
  return c;
}

std::set<std::pair<int, int> >S;

bool inc(char *num, int d) {
  int pos = d;
  bool done = false;

  while(true) {
    if(num[pos]<9) {
      num[pos]++;
      break;
    }
    else {
      num[pos]=0;
      pos--;
      if(pos==0) return false;
    }
  }
  return true;
}

void print(char *num, int d) {
  for(int i=1;i<=d;i++) printf("%c", num[i]+'0');
  printf("\n");
}

lli recycle(char *num, int d, int n, int a, int b) {
  S.clear();
  lli count = 0;
  int i, j;
  
  //For every possible cut
  for(i=1;i<d;i++) {
    int p = 1, x = 0;
    if(num[i+1]==0) continue;

    for(j=i;j>=1;j--) {
      x += p * num[j];
      p *= 10;
    }
    for(j=d;j>i;j--) {
      x += p * num[j];
      p*= 10;
    }

    if(x>=a && x<=b && x!=n && S.find(std::pair<int, int>(x, n))==S.end()) {
      count++;
      S.insert(std::pair<int, int>(x, n));
    }
  }

  return count;
}

lli solve(int A, int B) {
  int D = digits(A), i, n;
  lli count = 0;
  char num[11];

  num[1] = 1;
  for(i=2;i<=D;i++) num[i] = 0;
  n = pow(10, D-1);

  do {
    if(n<A || n>B) continue;

    count += recycle(num, D, n, A, B);
  } while(n++, inc(num, D));

  return count/2;
}


int main() {
  int T, t, a, b;
  lli ans;
  FILE *fin = fopen("input.txt", "r"), *fout = fopen("output.txt", "w");

  fscanf(fin, "%d", &T);
  for(t=1;t<=T;t++) {
    fscanf(fin, "%d %d", &a, &b);
    printf("Solving testcase %d, A=%d, B=%d... ", t, a, b);
    ans = solve(a, b);
    fprintf(fout, "Case #%d: %lld\n", t, ans);
    printf("done. Answer: %lld\n", ans);
  }

  return 0;
}
