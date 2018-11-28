#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

long long permutations(int a[], int b[], int n){
  int i;
  long long x = 0;
  for (i = 0; i < n; i++){
    x += a[i]*b[n-i-1];
  }
  return x;
}

int main(){
  int t, k, n, i;
  int na[900], nb[900];
  long long x;
  
  scanf("%d", &t);
  for (k = 1; k <= t; k++){
    scanf("%d", &n);
    for (i = 0; i < n; i++){
      scanf("%d", &na[i]);
    }
    for (i = 0; i < n; i++){
      scanf("%d", &nb[i]);
    }

    sort(na, na+n);
    sort(nb, nb+n);
    x = permutations(na, nb, n);
    printf("Case #%d: %d\n", k, x);
  }

  return 0;
}
