 #include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
#define EOL '\n'
int main()
{
       FILE *fr = fopen("A-small-attempt0.in", "r");
       if(fr == NULL)
               exit(1);

       FILE *fw = fopen("A-small-attempt0.out", "w");
       if(fw==NULL)
               exit(1);
       
       char ch99,ch;
       char googleLetters[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
       char decodedValues[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
       int T;
       fscanf(fr,"%d",&T);
       char nl;
       fscanf(fr, "%c", &nl);
       int j=0;
       for(int i=0; i<T; i++)
       {
               fprintf(fw,"Case #%d: ",i+1);
               while((ch = fgetc(fr)) != EOL )
                {
                       if(ch==EOF) break;
                       
                       //code to check ch in googleLetters                        
                       for(j = 0; j<26; j++)
                       {
                               if(googleLetters[j] == ch)
                               break;
                       }
                       if(j!=26)
                               ch99 = decodedValues[j];
                       else ch99 = ch;
                       fprintf(fw, "%c", ch99);
               }
			   if(i != T-1)
               fprintf(fw,"%c",'\n');
       }
       fclose(fr);
       fclose(fw);

       return 0;
}