#include <cstdio>

using namespace std;

char *frase = "welcome to code jam"; //19 caracteres

void welcome(char *s, int ind, int m, int *cnt) {
  if( m==19 )
    *cnt = (*cnt + 1)%10000;
  else {
    int i=ind;

    while( s[i] && s[i] != '\n' ) {
      if( s[i] == frase[m] )
	welcome(s, i+1, m+1, cnt);
      
      i++;
    }
  }
}

int main() {
  int N;
  char word[512];

  scanf("%d", &N);
  getchar();

  for(int ncases=1; ncases<=N; ncases++) {
    fgets(word, 501, stdin);

    int count=0;
    welcome(word, 0, 0, &count);

    printf("Case #%d: %04d\n", ncases, count);
  }
}
