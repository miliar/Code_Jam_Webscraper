#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

int Z, N;


int tab[100];
char S[100];

int main() {
  scanf("%d", &Z);
  for (int z=1; z<=Z; z++) {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        int V=0;
        scanf("%s", S);
         for (int j=0; j<N; j++) if (S[j]=='1') V=j;
        tab[i]=V;
    }

    int W=0;
    for (int i=0; i<N; i++) {
        int j=i;
        while (tab[j]>=i+1) j++;
        while (j>i) {
            swap (tab[j-1], tab[j]);
            j--;
            W++;
        }
    }

    printf("Case #%d: %d\n", z, W);
  }
  return 0;
}
