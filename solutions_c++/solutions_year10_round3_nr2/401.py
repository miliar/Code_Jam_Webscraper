#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <math.h>

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

/* Fair Warning 
#define MAX_NUMBER "999999999999999999999999999999999999999999999999999"

typedef struct bigNum
{
    char number[51];
    int len;
}sBigNumberData;

void inverseStr(char* str, int len)
{
    int i,j;
    char temp;
    
    for(i = len -1, j = 0; i != j; i--, j++)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int bigNumCmp(char* Bn1, char* Bn2)
{
    int i;
    for(i = 50; i >= 0; i++)
    {
        if(Bn1[i] > Bn2[i])
        {
            return 1;
        }    
        if(Bn1[i] < Bn2[i])
        {
            return 2;
        }
    }
    return 0;
}

int isZero(char* Bn)
{
    int i;
    for(i = 0; i < 51; i++)
    {
        if(Bn[i] > '0')
        {
            return 0;
        }
    }
    return 1;
}

void wSubtract(char* a, char* b, char* c)
{
    int i;
    int lenA;
    int lenB;

    if(2 == bigNumCmp(a,b))
    {
        strcpy(c,a);
    }
    else
    {
        for(i = 0; i < 51; i++)
        {
        
        }
    }
    return;
}
void wAsubtract(char* a, char* b, char* c)
{
    if(1 == bigNumCmp(a,b))
    {
    
    }
    else
    {
    
    }
}

void modR(char* a, char* r)
{
    
}

void wgcd(char* Bn1, char* Bn2)
{
    char r[51], temp[51];
    
    for(strcpy(r, Bn2); !isZero(r);)
    {
        strcpy(temp,r);

    }
}

int main(void)
{
    int i,j,k,m,n;
    int testNumber;
    int bigEventNumber;
    sBigNumberData bigEventTable[1000];
    sBigNumberData commonFactor;
    sBigNumberData temp;
    sBigNumberData answer;
    sBigNumberData smallest;

    strcpy(smallest.number, MAX_NUMBER);
    smallest.len = 51;

    FILE * fIn = fopen("D:\\B-small-attempt0.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < testNumber; i++)
    {
        fscanf(fIn,"%d",&bigEventNumber);
        
        for(j = 0; j < bigEventNumber; j++)
        {
            fscanf(fIn,"%s",&(bigEventTable[j].number));
            bigEventTable[j].len = strlen(bigEventTable[j].number);
            
            if(bigNumCmp(smallest,bigEventTable[j]))
            {
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

        if(0 == wmod(smallest,commonFactor))
        {
            answer.len = 1;
            answer.number[0] = '0';
        }
        else
        {
            answer = wsubtract(commonFactor, wmod(smallest,commonFactor));
        }
        fprintf(fOut,"Case #%d: %s\n",i+1,answer.number);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
} 

*/
/*
int getDistance(char* oldPath, char* newPath)
{
    int i, j;
    
    char slash = '/';
    char* oldPtr = ++oldPath;
    char* newPtr = ++newPath;
    int distance = 0;
    
    for(;(*oldPtr != 0) && (*oldPtr == *newPtr) && (*newPtr != 0); 
        oldPtr++, newPtr++);

    if(*newPtr != 0)
    {
        distance = 1;
    }
    if((*oldPtr == 0) && (slash == *newPtr))
    {
        newPtr++;
    }

    for(;*newPtr != 0; newPtr++)
    {       
        if(slash == *newPtr)
        {
            distance++;
        }
    }

    return distance;
}
int main(void)
{
    int i,j,k,m,n,p1,p2;
    int oldNum;
    int newNum;
    int testNumber;
    int minDistance;
    int tempDistance;
    int answer;
    char temp[2];
    char oldPath[201][201];
    char newPath[201][201];

    temp[0] = 0;
    temp[1] = 0;
    FILE * fIn = fopen("D:\\A-small-attempt0.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < testNumber; i++)
    {
        answer = 0;
        for(p1 = 0; p1 < 200; p1++)
        {
            for(p2 = 0; p2 < 200; p2++)
            {
                oldPath[p1][p2] = 0;
                newPath[p1][p2] = 0;
            }
        }
        fscanf(fIn,"%d %d",&oldNum,&newNum);
        for(j = 0; j < oldNum; j++)
        {
            fscanf(fIn,"%s",oldPath[j]);
        }
        
        for(j = 0; j < newNum; j++)
        {
            fscanf(fIn,"%s",newPath[j]);
        }

        for(j = 0; j < newNum; j++)
        {
            minDistance = getDistance(temp, newPath[j]);
            for(k = 0; k < oldNum; k++)
            {
                tempDistance = getDistance(oldPath[k],newPath[j]);
                if(tempDistance < minDistance)
                {
                    minDistance = tempDistance;    
                }
            }

            for(k = 0; k < j; k++)
            {
                tempDistance = getDistance(newPath[k],newPath[j]);
                if(tempDistance < minDistance)
                {
                    minDistance = tempDistance;    
                }   
            }

            answer += minDistance;
        }

        fprintf(fOut,"Case #%d: %d\n",i+1,answer);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
} 
*/
/*

int getOrder(int a, int index)
{
    int count = 0;
    
    for(int i = 0; i < index; i++)
    {
        if((a & (1 << i)))
        {
            count++;
        }
    }

    return count;
}
int main(void)
{
    int i,j,k,m;
    int testNumber;
    int N;
    int answer;
    int Num = 1;
    int answerArray[26];
    int order;
    
    FILE * fIn = fopen("D:\\test.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);
    
    for(i = 0; i < 26; i++)
    {
        answerArray[i] = -1;
    }
    for(i = 0; i < testNumber; i++)
    {
        fscanf(fIn,"%d",&N);
        Num = 1 << N;
        answer = 0;
        
        if(-1 != answerArray[N])
        {
            answer = answerArray[N];
        }

        else
        {
            for(j = 1; j < Num; j++)
            {
                for(order = getOrder(j,N); order != 1;)
                {
                    if(!(j&(1<<(order-1))))
                    {
                        break;
                    }
                    order = getOrder(j,order-1);
                }

                if(1 == order)
                {
                    answer++;
                }
            }
            answerArray[N] = answer;
        }


        fprintf(fOut,"Case #%d: %d\n",i+1,answer);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
} 

*/

/*
int main(void)
{
    int i,j,k,m;
    int testNumber;
    int wireCount;
    int answer;
    int aW[20000];
    int bW[20000];
    
    FILE * fIn = fopen("D:\\A-large.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);

    for(i = 0; i < testNumber; i++)
    {      
        fscanf(fIn,"%d",&wireCount);
        answer = 0;
        
        for( j = 0; j < wireCount; j++)
        {
            fscanf(fIn,"%d %d",&aW[j],&bW[j]);
        }

        for( j = 0; j < wireCount; j++)
        {
            for(k = 0; k < j; k++)
            {
                if(((aW[j] > aW[k]) && (bW[j] < bW[k])) || 
                    ((aW[j] < aW[k]) && (bW[j] > bW[k])))
                {
                    answer++;
                }
            }
        }

        fprintf(fOut,"Case #%d: %d\n",i+1,answer);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
} 
*/

int logN(int base, int shit)
{
    int count = 0;
    int remainder = 0;
    
    if((shit % base != 0) && (shit != 1))
    {
        remainder++;   
    }

    for(;shit >= base;)
    {
        if(shit % base != 0)
        {
            remainder++;   
        }
        shit /= base;
        count++;
    }

        if((shit % base != 0) && (shit != 1))
        {
            remainder++;   
        }

    if(remainder) count++;

    return count;
}

int main(void)
{
    int i,j,k,m;
    int testNumber;
    int answer;
    int base;
    int smallNum;
    int bigNum;
    int quotient;
   
    
    FILE * fIn = fopen("D:\\B-large.in","r");
    FILE * fOut = fopen("D:\\test.out","w"); 
    
    fscanf(fIn,"%d",&testNumber);

    for(i = 0; i < testNumber; i++)
    {      
        fscanf(fIn,"%d %d %d",&smallNum, &bigNum, &base);
        quotient = bigNum/smallNum;
        if( (bigNum % smallNum) )
        {
            quotient += 1;   
        }

        quotient = logN(base,quotient);
        answer = logN(2,quotient);

        fprintf(fOut,"Case #%d: %d\n",i+1,answer);  
    }

    fclose(fIn);
    fclose(fOut);
    return 1;
}