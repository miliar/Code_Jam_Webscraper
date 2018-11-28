#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;



int main(int argc, char *argv[])
{

    char *inFileName = "B-large.in";
    char *outFileName = "B-large.out";
    int i, j, group;
    int numGoogler, surprise, passVal, val;
    int okNum, surpriseNum, totalNum;
    FILE * pInFile, *pOutFile;
    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");

    //genDataBase();
    //displayDataBase(pOutFile);

    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
          fscanf(pInFile, "%d %d %d", &numGoogler, &surprise, &passVal);
          printf("numGoogler %d surprise %d passVal %d\n", numGoogler, surprise, passVal);
          okNum = surpriseNum = totalNum = 0;
          for(j = 0; j < numGoogler; j ++)
          {
                fscanf(pInFile, "%d", &val);
                if(passVal == 1)
                {
                    if(val >= 1)
                        okNum ++;
                }
                else if(passVal == 0)
                {
                    okNum ++;
                }
                else
                {
                    if(val >= (passVal * 3 - 2))
                        okNum ++;
                    else if(val >= (passVal * 3 - 4))
                        surpriseNum ++;
                }
          }
          
          if(surpriseNum >= surprise)
              totalNum = okNum + surprise;
          else
              totalNum = okNum + surpriseNum;
          fprintf(pOutFile, "Case #%d: %d\n", i+1, totalNum);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}



