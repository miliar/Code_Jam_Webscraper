#include <iostream>

using namespace std;

#define for_to(i,j,k) for (i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

#define huge long long

huge next(huge n,huge b) {
  huge ret =0;
  while (n) {
    ret += (n%b) * (n%b);
    n/=b;
  }
  return ret;
}

huge happy(huge n,huge b) {
  int it;
  for_to(it,1,1000) {
    n = next(n,b);
    if (n==1) return 1;
  }
  return 0;
}

int n_tests,test;
int i,j,k,ok,n;
int c;
int base[10],n_bases;

int main() {
  scanf("%d\n",&n_tests);
  for_to(test,1,n_tests) {
    c = getchar();
    n_bases = 0;
    while (c!='\n') {
      ungetc(c,stdin);
      scanf("%d",&base[n_bases++]);
      c=getchar();
    }
    n = 2;
    while (1) {
      ok=1;
      for_to(i,0,n_bases-1) {
        if (!happy(n,base[i])) {
          ok = 0;
          break;
        }
      }
      if (ok) {
        printf("Case #%d: %d\n",test,n);
        break;
      }
      ++n;
      //cout << "n=" << n << endl;
    }
  }
  return 0;
}
