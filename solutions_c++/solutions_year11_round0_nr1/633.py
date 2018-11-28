#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

unsigned short a[100];


int main(int argc, char **argv)
{
    unsigned short usTestCases = 0;
    unsigned char temp;
    FILE *ptInFile;
    FILE *ptOutFile;
    signed int i,j,k, N;
    signed short OrangePos = 1, BluePos = 1;
    signed short NextBluePos, NextOrangePos, timeSpent, TotalTimeSpent = 0;
     
    printf ("%d\n", argc);
    
    if (argc != 3)
    {
        printf("Please specify the input file name and output files names as arguments\n");
    }
    
    ptInFile = fopen(argv[1], "r");
    
    if (ptInFile == NULL)
    {
        printf("Not able to open the file %s\n", argv[1]);
    }
    
    ptOutFile = fopen(argv[2], "w+");
    
    if (ptOutFile == NULL)
    {
        printf("Not able to open the file %s\n", argv[2]);
    }
        
    if (0 != fscanf(ptInFile, "%d", &usTestCases))
    {
          for (i = 0; i < usTestCases; i++)
          {
              fscanf(ptInFile, "%d\n", &N);

              for (j = 0; j < N; j++)
              {
                  fscanf(ptInFile, "%c", &temp);
                  fscanf(ptInFile, "%d ", &a[j]);
                  
                  a[j] = temp << 8 | a[j];
              }
              
              OrangePos = 1;
              BluePos = 1;
              TotalTimeSpent = 0;
               
              for (j = 0; j < N; j++)
              {
                  if ((a[j] >> 8) == 'O')
                  {
                       timeSpent = (a[j] & 0x00FF) - (OrangePos);
                       if (timeSpent < 0)
                       {
                           timeSpent = -timeSpent;
                       }
                       
                       timeSpent++;
                       OrangePos = (a[j] & 0x00FF);
                       /* Get the next Blue element left */
                       for (k = j + 1; k < N; k++)
                       {
                           if ((a[k] >> 8) == 'B')
                           {
                              NextBluePos = (a[k] & 0x00FF);
                              if (NextBluePos - BluePos == 0)
                              {
                                   /* Don't do anything */
                              }
                              else if (NextBluePos - BluePos > 0)
                              {
                                   if (timeSpent >= NextBluePos - BluePos)
                                   {
                                        BluePos = NextBluePos;
                                   }
                                   else
                                   {
                                       BluePos += timeSpent;
                                   }
                              }
                              else
                              {
                                   if (timeSpent >= (BluePos - NextBluePos))
                                   {
                                        BluePos = NextBluePos;
                                   }
                                   else
                                   {
                                       BluePos -= timeSpent;
                                   }                                  
                              }
                              break;
                           }
                       }                       
                  }
                  
                  
                  else if ((a[j] >> 8) == 'B')
                  {
                       timeSpent = (a[j] & 0x00FF) - (BluePos);
                       if (timeSpent < 0)
                       {
                           timeSpent = -timeSpent;
                       }
                       
                       timeSpent++;
                       BluePos = (a[j] & 0x00FF);
                       /* Get the next Blue element left */
                       for (k = j + 1; k < N; k++)
                       {
                           if ((a[k] >> 8) == 'O')
                           {
                              NextOrangePos = (a[k] & 0x00FF);
                              if (NextOrangePos - OrangePos == 0)
                              {
                                   /* Don't do anything */
                              }
                              else if (NextOrangePos - OrangePos > 0)
                              {
                                   if (timeSpent >= NextOrangePos - OrangePos)
                                   {
                                        OrangePos = NextOrangePos;
                                   }
                                   else
                                   {
                                       OrangePos += timeSpent;
                                   }
                              }
                              else
                              {
                                   if (timeSpent >= (OrangePos - NextOrangePos))
                                   {
                                        OrangePos = NextOrangePos;
                                   }
                                   else
                                   {
                                       OrangePos -= timeSpent;
                                   }                                  
                              }
                              break;
                           }
                       }                       
                  }
                  
                  TotalTimeSpent += timeSpent;
              }
              
              fprintf(ptOutFile, "Case #%d: %d\n", (i + 1), TotalTimeSpent);
          }
          

    }
    else
    {
        printf("Couldn't read properly from input file\n");
    }
    
    fclose(ptInFile);
    fclose(ptOutFile);
}
