#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#define ZEEPLUS (91)

int main(int argc, char **argv)
{
    unsigned short usTestCases = 0;
    unsigned char string[10], Invoke[102], Result[307];
    unsigned char combine[26][26] = {0};
    unsigned char antogonist[27][27] = {0};
    unsigned int C, D, N;
    signed short val1, val2, i, j, k, m;
    
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
        
    if (0 != fscanf(ptInFile, "%d", &usTestCases))
    {
          for (j = 0; j < usTestCases; j++)
          {
              memset(combine, 0, sizeof(combine));                                                       
              memset(antogonist, 0, sizeof(antogonist));
                            
              fscanf(ptInFile, "%d", &C);
              
              for (k = 0; k < C; k++)
              {
                  fscanf(ptInFile, "%s", &string);
                  val1 = string[0] - 'A';
                  val2 = string[1] - 'A';
                  combine[val1][val2] = string[2];
                  combine[val2][val1] = string[2];          
              }
                           
              fscanf(ptInFile, "%d", &D);
              
              for (k = 0; k < D; k++)
              {
                  fscanf(ptInFile, "%s", &string);
                  val1 = string[0] - 'A';
                  val2 = string[1] - 'A';                  
                  antogonist[val1][val2] = '1';
                  antogonist[val2][val1] = '1';
              }
              
              fscanf(ptInFile, "%d %s", &N, &Invoke);
                            
              for (i = 1; i < N; i++)
              {   
                  val1 = Invoke[i] - 'A';
                  
                  for (m = i - 1; m >=0; m--)
                  {
                      if(Invoke[m] != ZEEPLUS)
                      {
                          val2 = Invoke[m] - 'A';          
                          break;
                      }
                  }
                  if (m < 0)
                  {
                        continue;
                  }
                  
                  if (0 != combine[val1][val2])
                  {
                        Invoke[i] = combine[val1][val2];
                        Invoke[m] = ZEEPLUS;
                  }
                  else if (0 != combine[val2][val1])
                  {
                        Invoke[i] = combine[val2][val1];
                        Invoke[m] = ZEEPLUS;
                  }
                  else
                  {
                      for (k = i - 1; k >= 0; k--)
                      {
                          val2 = Invoke[k] - 'A';
                          if (antogonist[val1][val2] != 0
                               || antogonist[val2][val1] != 0)
                          {
                               for (m = 0; m <= i; m++)
                               {
                                   Invoke[m] = ZEEPLUS;
                               }
                               
                               break;
                          }
                      }
                  }
              }
              
              k = 0;
              Result[k++] = '[';
              for (i = 0; i < N; i++)
              {
                  if (Invoke[i] != ZEEPLUS)
                  {
                     if (k == 1)
                     {
                         Result[k++] = Invoke[i];
                     }
                     else
                     {
                         Result[k++] = ',';
                         Result[k++] = ' ';                           
                         Result[k++] = Invoke[i];
                     }
                  }
              }
              
              Result[k++] = ']';
              Result[k] = '\0';
              
              fprintf(ptOutFile, "Case #%d: %s\n", j + 1, Result); 
          }
    }
    else
    {
        printf("Error reading the input file\n");
    }
    
    return 0;
}
