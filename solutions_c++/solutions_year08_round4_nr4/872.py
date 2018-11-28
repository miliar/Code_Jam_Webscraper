#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  //freopen("input.txt", "w", stdin);
  int C;
  scanf("%d", &C);
  for (int c=1; c<=C; ++c){
    printf("Case #%d: ", c);

    int k;
    char s[1024];
    scanf("%d %s", &k, s);
    //fprintf(stderr, "%s\n", s);

    int perm[k], n = strlen(s);
    for (int i=0; i<k; ++i){
      perm[i] = i;
    }

    int answer = (1<<30);
    do{
      //fprintf(stderr, "Perm: "); for (int i=0; i<k; ++i) fprintf(stderr, "%d-", perm[i]); fprintf(stderr, "\n");
      char t[1024];
      for (int i=0; i<n; i += k){
        for (int j=0; j<k; ++j){
          t[i+j] = s[i + perm[j]];
        }
      }
      int score = 0, i = 0, j = 0;
      while(j < n){
        while (j < n && t[i] == t[j]){
          ++j;
        }
        i = j;
        score++;
      }
      answer = score < answer ? score : answer;
      //fprintf(stderr, "%s\n", t);

    }while(next_permutation(perm, perm+k));
    printf("%d\n", answer);
  }
  return 0;
}
