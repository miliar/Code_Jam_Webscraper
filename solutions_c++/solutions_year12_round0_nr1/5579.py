#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
  int T;
  char L[101] = {'\0'};
  scanf("%d", &T);
  gets(L);
  for(int Ti=1; Ti<=T; ++Ti) {
    gets(L);
    //fprintf(stderr, "%s, %d, %c", L, strlen(L), L[strlen(L)]);
    //fprintf(stderr, "%s, %d", L, strlen(L));
    int i=0;
    char l=L[i];
    printf("Case #%d: ", Ti);
    while(l != '\0') {
           if(l=='y') L[i]='a';
      else if(l=='n') L[i]='b';
      else if(l=='f') L[i]='c';
      else if(l=='i') L[i]='d';
      else if(l=='c') L[i]='e';
      else if(l=='w') L[i]='f';
      else if(l=='l') L[i]='g';
      else if(l=='b') L[i]='h';
      else if(l=='k') L[i]='i';
      else if(l=='u') L[i]='j';
      else if(l=='o') L[i]='k';
      else if(l=='m') L[i]='l';
      else if(l=='x') L[i]='m';
      else if(l=='s') L[i]='n';
      else if(l=='e') L[i]='o';
      else if(l=='v') L[i]='p';
      else if(l=='z') L[i]='q';
      else if(l=='p') L[i]='r';
      else if(l=='d') L[i]='s';
      else if(l=='r') L[i]='t';
      else if(l=='j') L[i]='u';
      else if(l=='g') L[i]='v';
      else if(l=='t') L[i]='w';
      else if(l=='h') L[i]='x';
      else if(l=='a') L[i]='y';
      else if(l=='q') L[i]='z';
      printf("%c", L[i]);
      l=L[++i];
    }
    printf("\n");
  }
  return 0;
}
