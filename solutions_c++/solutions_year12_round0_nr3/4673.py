#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
int len;
//int test_cases;
int index;
int i=1;
char g[102];
const char replace[] = "yhesocvxduiglbkrztnwjpfmaq";
char *s;
FILE *iFile = fopen("A-small-attempt2.in", "r");
FILE *oFile = fopen("output.txt", "w");
if (iFile == NULL)
    {
                 perror("Failed to open file \"input.txt\"");
                 return EXIT_FAILURE;
    }

if (oFile == NULL)
{
perror("Failed to open file \"output.txt\"");
return EXIT_FAILURE;
}

fgets(g,102,iFile);
while(fgets(g,sizeof(g),iFile) != NULL)
{
    len = strlen(g)-1;
     if(g[len] == '\n')
     g[len] = 0;

s = g;


 while(*s)
      {
       index = *s - 'a';
          if(*s != ' ')
        *s = replace[index];
         s++;
       }
fprintf(oFile,"Case #%d: %s\n",i,g);
i++;
}
fclose(iFile);
fclose(oFile);
return 0;
}
