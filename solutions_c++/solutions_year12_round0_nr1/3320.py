#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int strPos(char *str, char ch);
static char mappingL[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
static char mappingU[] = {'Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q'};
char *InpFilename = "C:\\VINOD\\A-small-attempt1.in"; 
char *OutFilename = "C:\\VINOD\\A-small-output_1.txt"; 
#define LINE_MAX 100

int main()
{
    
 /** number of test cases, T. T test cases follow, one per line. **/
 int T = 0, i =1 , j = 0, flg = 0;
 char G[LINE_MAX];
 /** read from input file **/
 //first char T
 //remaining chars will be G[i] and write the output in one file
 FILE *fpr, *fpw; 
 fpr=fopen(InpFilename,"r");
 fpw=fopen(OutFilename,"w"); 
 T = atoi(fgets(G,LINE_MAX,fpr));
 
 while((fgets(G,LINE_MAX+1,fpr) != NULL) && i<=T)
 {
   
   for(j=0; j<strlen(G); j++)
   {
     if(G[j] != ' ') 
     {
         if(isupper(G[j])) G[j] = mappingU[G[j] - 'A'];       
         else G[j] = mappingL[G[j] - 'a'];  
     }
   }      
         
  if(strlen(G) > 0 ) 
  { fprintf(fpw,"Case #%d: %s\n", i, G);
    i++;
  }
    
 }
 

 fclose(fpr); 
 fclose(fpw); 

 return 1;
    
}

