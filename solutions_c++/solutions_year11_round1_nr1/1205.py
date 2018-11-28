#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#define ZEEPLUS (91)

unsigned long
hcf ( unsigned long a, unsigned long int b )
{
  unsigned long c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}


int main(int argc, char **argv)
{
    unsigned short usTestCases = 0;
    unsigned long N;
    unsigned long Pd, Pg;
    signed short i, j, k, m;
    unsigned long long hcfd, hcfg;
     
    FILE *ptInFile;
    FILE *ptOutFile;
       
    if (argc != 3)
    {
        printf("Please specify input file and output files names as arguments respectively\n");
        return -1;
    }
        
    ptInFile = fopen(argv[1], "r");
    
    if (ptInFile == NULL)
    {
        printf("Not able to open the file %s\n", argv[1]);
        return -1;
    }
    ptOutFile = fopen(argv[2], "w");
    
    if (ptOutFile == NULL)
    {
        printf("Not able to open the file %s\n", argv[2]);
        return -1;
    }
      
    printf("%d\n", sizeof(long long));        
    if (0 != fscanf(ptInFile, "%d", &usTestCases))
    {
       for (i = 1; i <= usTestCases; i++)
       {   
          
        fscanf(ptInFile, "%d %d %d", &N, &Pd, &Pg);
        printf("%d, %d, %d\n", N, Pd, Pg);
       

#if 0        
        hcfg = hcf(Pg, 100);
#endif
        
        if ((Pg == 100 && Pd < Pg) || (Pg == 0 && Pd > Pg))
        {
            fprintf(ptOutFile, "Case #%d: %s\n", i, "Broken");
            continue;               
        }        
       
        if (N > 100)
        {
              fprintf(ptOutFile, "Case #%d: %s\n", i, "Possible");
              continue;
        } 
        
        hcfd = hcf(Pd, 100);
        if (100/hcfd > N)
        {
            fprintf(ptOutFile, "Case #%d: %s\n", i, "Broken");
            continue; 
        }
        
        fprintf(ptOutFile, "Case #%d: %s\n", i, "Possible"); 
        
#if 0        
        if ((Pd/hcfd <= Pg/hcfg) && (100/hcfd <= 100/hcfg))
        {
             fprintf(ptOutFile, "Case #%d: %s\n", i, "Possible");        
        }
        else
        {
             fprintf(ptOutFile, "Case #%d: %s\n", i, "Broken");  
        }
#endif        
       }
    }
    
    getch();
}
