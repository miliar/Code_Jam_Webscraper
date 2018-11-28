#include <stdio.h>
#include <string.h>

using namespace std;

int i,j,a,b;
char cad[102],val[30];

int main() {

strcpy(val,"yhesocvxduiglbkrztnwjpfmaq");

scanf("%d ",&j);

 for(i=0; i<j; i++) {

   gets(cad);
   b = strlen(cad);

   printf("Case #%d: ",i+1);

  for(a=0; a<b; a++) {

    if(cad[a]-'a' >= 0 && cad[a]-'a'<= 26) {

      printf("%c",val[cad[a]-'a']);

    }
    else {

     printf("%c",cad[a]);

    }

  }

   printf("\n");
 }


return 0;
}
