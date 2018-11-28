#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

char tab[100];


int main() {
  int Z;
  scanf("%d", &Z);
  for (int z=1; z<=Z; z++) {
    scanf("%s", tab+1);
    tab[0]='0';
    int N=0;
    while (tab[N]) N++;
    next_permutation(tab, tab+N);
    printf("Case #%d: ", z);
    if (tab[0]!='0') printf("%c", tab[0]);
    printf("%s\n", tab+1);
  }
  return 0;
}