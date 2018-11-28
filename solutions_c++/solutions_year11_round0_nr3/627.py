#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

unsigned long a[1000];

int main(int argc, char **argv)
{
    unsigned short usTestCases;
    unsigned long Sum, Small, Value;
    unsigned short i, j;
    FILE *ptInFile;
    FILE *ptOutFile;
    signed int N;
   
    if (argc != 3)
    {
        printf("Please specify the input file name and output files names as arguments\n");
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
        
    if (0 != fscanf(ptInFile, "%d", &usTestCases))
    {
          for (j = 0; j < usTestCases; j++)
          {
              Sum = 0;
              Small = 0xFFFFFFFF;
         
              fscanf(ptInFile, "%d", &N);
              
              for (i = 0; i < N; i++)
              {
                  fscanf(ptInFile, "%ld", &a[i]);

                  if (Small > a[i])
                  {
                      Small = a[i];
                  }
                  if (i == 0)
                  {
                      Value = a[i];
                  }
                  else
                  {
                      Value ^= a[i];
                  }
                  
                  Sum += a[i];              
              }
              
              if (Value != 0)
              {
                 fprintf(ptOutFile, "Case #%d: %s\n", j+1, "NO");
              }
              else
              {
                  fprintf(ptOutFile, "Case #%d: %ld\n", j+1, (Sum - Small));
              } 
          }        
    }
    else
    {
        printf("Couldn't read the file properly");
        return -1;
    }
    
    return 0;
}
