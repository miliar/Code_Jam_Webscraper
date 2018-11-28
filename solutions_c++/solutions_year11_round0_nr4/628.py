#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

unsigned short a[1000];
unsigned short b[1000];

void bubble_sort(unsigned short *a, unsigned short N)
{
     unsigned short i, j, temp;
     for (i = 0; i < N - 1; i++)
     {
         for (j = i; j < N; j++)
         {
             if (a[i] > a[j])
             {
                  temp = a[i];
                  a[i] = a[j];
                  a[j] = temp;
             }
         }
     }
} 

int main(int argc, char **argv)
{
    unsigned short usTestCases = 0;
    double hits;
    unsigned short i, j, k;
    FILE *ptInFile;
    FILE *ptOutFile;
    signed int N;
     
    printf ("%d\n", argc);
    
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
              fscanf(ptInFile, "%d", &N);
              for (i = 0; i < N; i++)
              {
                  fscanf(ptInFile, "%d", &a[i]);
              }
              
              memcpy(b, a, N * sizeof(unsigned short));
              bubble_sort(b, N);
              
              hits = 0.0;
              for (i = 0; i < N; i++)
              {
                  /* As no element in the array is same */
                  if (a[i] != b[i])
                  {
#if 0 
                     for (k = 0; k < N; k++)
                     {
                        
                         if (b[i] == a[k])
                         {
                             a[k] = a[i];
                             break;
                         }
                     }
                     
                     a[i] = b[i];      
#endif         
                     hits ++;
                  }
              }
              
              fprintf(ptOutFile, "Case #%d: %f\n", j+1, hits);
          }
    }
    else
    {
        printf("Error reading the input file\n");
    }
    
    return 0;
}
