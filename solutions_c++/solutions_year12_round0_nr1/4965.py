#include<stdio.h>

char x[] = "yhesocvxduiglbkrztnwjpfmaq";

int main ( void ){
  int n;
  scanf("%d\n",&n);
  char s[200];
  char ss[3][200];
  char a[256] = {0};
  for (int i=0; i<n; ++i){
    gets(s);
    printf("Case #%d: ",i+1);
    for (char *q=s;*q;q++){
      if (*q!=' ')
      printf("%c",x[*q-'a']);
      else printf(" ");
    }
    printf("\n");
  }
/*  for (int i=0; i<n; ++i){
    gets(ss[i]);
  }
  for (int i=0; i<n; ++i){
    gets(s);
    for (char *q=s;*q;q++){
      a[ss[i][q-s]]=*q;
    }    
  }
  for (char b='a'; b<='z'; ++b){
    printf("%c",b);
  }
  printf("\n");
  for (char b='a'; b<='z'; ++b){
    printf("%c",a[b]);
  }
*/
  return 0;
}