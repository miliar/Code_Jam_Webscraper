#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int T;
int k;

char s[1100];
int perm[5], n;

int getlen(){
  int count = 0;
  char last = 0;
  for(int i = 0; i < n / k; i++){
    for(int j = 0; j < k; j++){
      if (s[i*k + perm[j]] != last)
	count++;
      last = s[i*k + perm[j]];
    }
  }
  return count;
}

int main(){
  int x;
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    scanf("%d", &k);
    scanf("%s", s);
    n = strlen(s);
    for(int i = 0; i < k; i++) {
      perm[i] = i;
    }
    int ans = n;
    do {
      x = getlen();
      if (x < ans)
	ans = x;
    } while (next_permutation(perm, perm+k));
    printf("%d\n", ans);
  }
}
