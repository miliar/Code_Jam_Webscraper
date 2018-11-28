#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char map[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    int T;
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++)
    {
          char line[120];
          gets(line);
          printf("Case #%d: ",t);
          for (int i=0;i<strlen(line);i++)
          {
              if (line[i]==' ') printf(" ");
              else printf("%c",map[line[i]-'a']);
          }
          printf("\n");
    }
    return 0;
}
