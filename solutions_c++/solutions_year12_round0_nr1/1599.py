#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
int main()
{
    char ch;
    int n, i;
    FILE *fp1, *fp2;
    fp1 = fopen("A-small-attempt3.in", "r");
    fp2 = fopen("Output2.txt", "w");
    fscanf(fp1, "%d", &n);
    fscanf(fp1, "%c", &ch);
    for(i = 0; i < n; i++)
    {
          fscanf(fp1, "%c", &ch);
          fprintf(fp2, "Case #%d: ", i + 1);
          while(ch != '\n')
          {
                   if(ch == 'a')
                       fprintf(fp2, "y");
                   else if(ch == 'b')
                       fprintf(fp2, "h");
                   else if(ch == 'c')
                       fprintf(fp2, "e");       
                   else if(ch == 'd')
                       fprintf(fp2, "s");
                   else if(ch == 'e')
                       fprintf(fp2, "o");
                   else if(ch == 'f')
                       fprintf(fp2, "c");
                   else if(ch == 'g')
                       fprintf(fp2, "v");
                   else if(ch == 'h')
                       fprintf(fp2, "x");
                   else if(ch == 'i')
                       fprintf(fp2, "d");
                   else if(ch == 'j')
                       fprintf(fp2, "u");
                   else if(ch == 'k')
                       fprintf(fp2, "i");
                   else if(ch == 'l')
                       fprintf(fp2, "g");
                   else if(ch == 'm')
                       fprintf(fp2, "l");
                   else if(ch == 'n')
                       fprintf(fp2, "b");
                   else if(ch == 'o')
                       fprintf(fp2, "k");
                   else if(ch == 'b')
                       fprintf(fp2, "h");
                   else if(ch == 'p')
                       fprintf(fp2, "r");
                   else if(ch == 'q')
                       fprintf(fp2, "z");    
                   else if(ch == 'r')
                       fprintf(fp2, "t");
                   else if(ch == 's')
                       fprintf(fp2, "n");
                   else if(ch == 't')
                       fprintf(fp2, "w");
                   else if(ch == 'u')
                       fprintf(fp2, "j");
                   else if(ch == 'v')
                       fprintf(fp2, "p");
                   else if(ch == 'w')
                       fprintf(fp2, "f");
                   else if(ch == 'x')
                       fprintf(fp2, "m");
                   else if(ch == 'y')
                       fprintf(fp2, "a");
                   else if(ch == 'z')
                       fprintf(fp2, "q");
                   else
                       fprintf(fp2, " ");
                   fscanf(fp1, "%c", &ch);    
          }
          fprintf(fp2, "\n");
    }
    return 0;
}        
                                                                                                           
