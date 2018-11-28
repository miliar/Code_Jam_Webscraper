#include <iostream>
#include <cstring>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

#define MAX 510 
#define MOD 10000
#define LEN_PATTERN 19

int i,j,k,len;
int n_tests,test;
char s[MAX],c;
char pattern[] = "welcome to code jam";
int T[MAX][LEN_PATTERN+10];

int main() {
  scanf("%d",&n_tests);
  for_to(test,1,n_tests) {
    scanf(" %c",&s[0]);
    len = 1;
    c = getchar();
    while (c != '\n') {
      s[len++] = c;
      c = getchar();
    }
    for_downto(j,LEN_PATTERN,0) {
      for_downto(i,len,0) {
        if (j == LEN_PATTERN)
          T[i][j] = 1;
        else if (i == len)
          T[i][j] = 0;
        else if (s[i] == pattern[j])
          T[i][j] = (T[i+1][j] + T[i+1][j+1]) % MOD;
        else
          T[i][j] = T[i+1][j];
      }
    }
    printf("Case #%d: %04d\n",test,T[0][0]);
  }
  return 0;
}
