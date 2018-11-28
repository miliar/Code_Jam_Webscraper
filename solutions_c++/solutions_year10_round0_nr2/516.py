#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#ifdef _MSC_VER
typedef unsigned __int64 uint64;
#else
typedef unsigned long long uint64;
#endif


/* 2010 google code jam-- Theme Park 
int main(void)
{
    int i,j,k,m,n;
    int testNumber;
    int roundNumber;
    int groupNumber;
    int n32GroupCountTable[1001];
    uint64 u64SumTable[1001];
    int nextIndex[1001];
    int traverseCount[1001];
    uint64 traverseSum[1001];
    int sizeK;
    int currentRound;
    int cycleNumber;
    int cycleStartIndex;
    uint64 cycleSum;
    uint64 u64CurrentSum;
    uint64 answer;
    int previousCount;
    int count2Index[1001];
    uint64 KeyTable[1001];
    
    FILE * fIn = fopen("D:\\C-large.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < testNumber; i++)
    {
        for(j = 0; j < 1001; j++)
        {
            n32GroupCountTable[j] = 0;
            u64SumTable[j] = 0;
            nextIndex[j] = 0;
            traverseCount[j] = 0;
            traverseSum[j] = 0;
            count2Index[j] = 0;
            KeyTable[j] = 0;
        }
        roundNumber = 0;
        groupNumber = 0;
        sizeK = 0;
        currentRound = 0;
        u64CurrentSum = 0;
        cycleNumber = 0;
        cycleStartIndex = -1;
        cycleSum = 0;
        answer = 0;
        
        fscanf(fIn,"%d %d %d",&roundNumber, &sizeK, &groupNumber);
        for(j = 0; j < groupNumber; j++)
        {
            fscanf(fIn,"%d",&n32GroupCountTable[j]);
        }

        for(j = 0; j < groupNumber; j++)
        {
            int tempSum = n32GroupCountTable[j];
            
            for(m = (j+1)%groupNumber; m != j; m = (m+1)%groupNumber)
            {
                tempSum += n32GroupCountTable[m];
                
                if(tempSum > sizeK)
                {
                    break;
                }
            }
            
            if(tempSum > sizeK)
            {
                tempSum -= n32GroupCountTable[m];
            }
            
            u64SumTable[j] = tempSum;
            nextIndex[j] = m;
        }

        int index = 0;
        int tempTraverseCount = 1;
        uint64 tempTraverseSum = 0;

        for(;;tempTraverseCount++)
        {
            if(traverseCount[index])
            {
                cycleStartIndex = index;
                cycleNumber = tempTraverseCount - traverseCount[index];
                cycleSum = tempTraverseSum - traverseSum[index];
                previousCount = traverseCount[index] - 1;
                break;
            }
            
            count2Index[tempTraverseCount] = index;
            traverseCount[index] = tempTraverseCount;
            traverseSum[index] = tempTraverseSum;
            tempTraverseSum += u64SumTable[index];
            KeyTable[tempTraverseCount] = tempTraverseSum;
            index = nextIndex[index];
        }

        if(roundNumber < previousCount)
        {
            int tempIndex = count2Index[roundNumber];
            answer = traverseSum[tempIndex] + u64SumTable[tempIndex];
        }
        else
        {
            int q,r;
            roundNumber -= previousCount;
            q = roundNumber/cycleNumber;
            r = roundNumber%cycleNumber;
            answer = (q * cycleSum);
            
            r = r + previousCount;
            answer = answer + KeyTable[r];
        }

        fprintf(fOut,"Case #%d: %lld\n",i+1,answer);
    
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
}

*/

/*Snapper Chain
 int main(void)
{
    int i,j,k,m,n;
    int testNumber;
    int Nth;
    int Kcount;
    int completeN;
    
    FILE * fIn = fopen("D:\\A-large.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < testNumber; i++)
    {
        
        fscanf(fIn,"%d %d",&Nth,&Kcount);
        completeN = (1 << Nth);
        Kcount %= completeN;
        
        if((completeN -1) == Kcount)
        {
            fprintf(fOut,"Case #%d: ON\n",i+1);
        }

        else
        {
            fprintf(fOut,"Case #%d: OFF\n",i+1);
        }
    
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
}  */

/* Fair Warning */

int wgcd(int a, int b)
{
    int r, temp;
    for( r = b; r != 0;)
    {
        temp = r;
        r = a%r;
        a = temp;
    }
    return a;
}

int wsubtract(int a, int b)
{
    if(a>=b)
    {
        return a-b;
    }
    else
    {
        return b-a;
    }
}

int main(void)
{
    int i,j,k,m,n;
    int testNumber;
    int bigEventNumber;
    int bigEventTable[1000];
    int commonFactor;
    int temp;
    int answer;
    int smallest= 1<<30;

    FILE * fIn = fopen("D:\\B-small-attempt0.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < testNumber; i++)
    {
        smallest= 1<<30;
        fscanf(fIn,"%d",&bigEventNumber);
        
        for(j = 0; j < bigEventNumber; j++)
        {
            fscanf(fIn,"%d",&bigEventTable[j]);
            if(smallest > bigEventTable[j])
            {
                smallest = bigEventTable[j];
            }
        }
        commonFactor = wsubtract(bigEventTable[0],bigEventTable[1]);
        
        for(j = 0; j < bigEventNumber; j++)
        {
            for(k = j+1; k < bigEventNumber; k++)
            {
                temp = wsubtract(bigEventTable[j],bigEventTable[k]);
                commonFactor = wgcd(commonFactor, temp);
            }
        }

        if(0 == smallest%commonFactor)
        {
            answer = 0;
        }
        else
        {
            answer = commonFactor - (smallest%commonFactor);
        }
        fprintf(fOut,"Case #%d: %d\n",i+1,answer);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
} 

