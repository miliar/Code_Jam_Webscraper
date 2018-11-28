#include <cstdlib>
#include <iostream>
#include <stdio.h>

using namespace std;

char map[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k',
    'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g',
    't', 'h', 'a', 'q'};

char map2[26];

int main(int argc, char *argv[])
{
    FILE * pInFile, *pOutFile;
    char *inFileName = "A-small-attempt0.in";
    char *outFileName = "A-small-attempt0.out";
    int i, j, group;
    char inTmp[2000], outTmp[2000];
    char charTmp;
    
    
    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");
    
    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");

    fscanf(pInFile, "%d", &group);
    charTmp = fgetc(pInFile);
    printf("group %d\n", group);

    for(i = 0; i < 26; i ++)
    {
        map2[map[i] - 'a'] = 'a' + i;
    }

    for(i = 0; i < 26; i ++)
    {
        printf("%c->%c\n", 'a'+i , map2[i]);
    }

    for(i =0; i< group; i++)
    {
          memset(outTmp, 0, sizeof(outTmp));
          charTmp = fgetc(pInFile);
          while(charTmp != '\n')
          {
              if(charTmp != ' ')
              {
                sprintf(inTmp, "%c", map2[charTmp - 'a']);
                if(charTmp != '\r')
                    strcat(outTmp, inTmp);
              }
              else
              {
                strcpy(inTmp, " ");
                strcat(outTmp, inTmp);
              }
                
              charTmp = fgetc(pInFile);
          }
          fprintf(pOutFile, "Case #%d: %s\n", i+1, outTmp);

    }
  
    
    fclose(pInFile);
    fclose(pOutFile);
    system("PAUSE");
    return EXIT_SUCCESS;
}
