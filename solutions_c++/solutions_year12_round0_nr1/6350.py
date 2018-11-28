#include <stdio.h>
#include <stdlib.h>
char isalpha(char chr) {
 return((chr>=65&&chr<=90)||(chr>=97&&chr<=122));
}
char tolower(char chr) {
 if(chr>=65&&chr<=90)
  return(chr+32);
 else
  return(chr);
}
int main(int argc, char *argv[])
{
int n,i,j;
char str[30][200];
scanf("%d ",&n);
for(i=0;i<n;i++)
 gets(str[i]);

for(i=0;i<n;i++) {
 printf("Case #%d: ",(i+1));
 j=0;
 while(str[i][j]) {
  if(isalpha(str[i][j]))
   switch(tolower(str[i][j])) {
    case 'a': printf("y"); break;
    case 'b': printf("h"); break;
    case 'c': printf("e"); break;
    case 'd': printf("s"); break;
    case 'e': printf("o"); break;
    case 'f': printf("c"); break;
    case 'g': printf("v"); break;
    case 'h': printf("x"); break;
    case 'i': printf("d"); break;
    case 'j': printf("u"); break;
    case 'k': printf("i"); break;
    case 'l': printf("g"); break;
    case 'm': printf("l"); break;
    case 'n': printf("b"); break;
    case 'o': printf("k"); break;
    case 'p': printf("r"); break;
    case 'q': printf("z"); break;
    case 'r': printf("t"); break;
    case 's': printf("n"); break;
    case 't': printf("w"); break;
    case 'u': printf("j"); break;
    case 'v': printf("p"); break;
    case 'w': printf("f"); break;
    case 'x': printf("m"); break;
    case 'y': printf("a"); break;
    case 'z': printf("q"); break;
   }
  else
   printf("%c",str[i][j]);
  j++;
 }
 printf("\n");
}	
return(0);
}
