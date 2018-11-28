//
//  main.cpp
//  RecycledNumbers3
//
//  Created by Choi Peter on 12. 4. 15..
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int nEnd;


int Sequence(int num)
{
    int Seq;
    Seq = (int)(log10((float)num) + 1);
    return Seq;
}

void MoveLeft(char* sIn, int nSize)
{
    char temp;
    int  i;
    
    temp = sIn[0];
    
    for(i=0 ; i<nSize-1 ; i++)
    {
        sIn[i] = sIn[i+1];
    }
    sIn[nSize-1] = temp;
}

int RecycleNum(const int nStart)
{
    int   i,j;
    int   nRet;
    int   nStartSize;
    int   nRecycleSize;
    char* sStart;
    char* sRecycledNumber;
    int*  nRecycledNumbers;
    
    bool bSame;
    int temp;
    
    nStartSize = Sequence(nStart);
    sStart = (char*)malloc(sizeof(char)*(nStartSize+1));
    sRecycledNumber  = (char*)malloc(sizeof(char)*(nStartSize+1));
    nRecycledNumbers = (int*)malloc(sizeof(char)*(nStartSize));
    
    sprintf(sStart, "%d",nStart);
    
    nRet=0;
    
    strcpy(sRecycledNumber, sStart);
    
    
    for (i=0,nRecycleSize=0; i<nStartSize-1; i++)
    {
        MoveLeft(sRecycledNumber, nStartSize);
        temp = (int)atoi(sRecycledNumber);
        
        
        if(temp > nStart && temp <= nEnd)
        {
            bSame=false;
            
            for (j=0; j<nRecycleSize; j++) 
            {
                if(temp == nRecycledNumbers[j])
                {
                    bSame = true;
                    break;
                }
            }
            
            if(bSame == false)
            {
                nRecycledNumbers[nRecycleSize] = temp;
                nRecycleSize++;
            }
        }
    }
    
    return nRecycleSize;
}

int main(int argc, const char * argv[])
{
    int T;
    int A,B;
    
    int i,j,k;
    bool bDigitUsed[7];
    int nAD, nBD;
    char *sRecycledNum;
    int nStart;
    
    int nOutput;
    
    FILE *inputF,*outputF;
    
    inputF  = fopen("./C-large.in.txt", "r");
    outputF = fopen("./C_result_large00.txt","w");
    if(outputF==NULL || inputF==NULL)
    {
        printf("error!\n");
        return -1;
    }
    
    
    
    //scanf("%d\n",&T);
    fscanf(inputF, "%d\n",&T);
    for(i=0; i<T ;i++)
    {
        //scanf("%d %d",&A,&B);
        fscanf(inputF, "%d %d",&A,&B);
        
        nAD = Sequence(A);
        nBD = Sequence(B);
        
        for(j=0 ; j<7 ; j++)
        {
            bDigitUsed[j]=false;
        }

        nOutput=0;
        for (j=nAD; j<=nBD; j++)
        {
            sRecycledNum = (char*)malloc(sizeof(char)*(j+1));
            if (j > nAD)
            {
                nStart = (int)pow(10, j-1);
            }
            else if(j == nAD)
            {
                nStart = A;
            }
            
            if (j < nBD)
            {
                nEnd = (int)pow(10, j) - 1;
            }
            else if(j == nBD)
            {
                nEnd = B;
            }
            
            for (k=nStart; k<nEnd; k++)
            {
                nOutput += RecycleNum(k);
                
            }
            free(sRecycledNum);
        }
        
        printf("Case #%d: %d\n",i+1, nOutput);
        fprintf(outputF,"Case #%d: %d\n",i+1, nOutput);
    }
    
    getchar();
    fclose(inputF);
    fclose(outputF);
    
    

    return 0;
}

