#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;


int getDigit(int val)
{
    int digit = 0;
    
    while(val > 0)
    {
        val /= 10;
        digit = digit + 1;
    }
    return digit;
}

int numMask[2000000/32 + 1];

int isBitSet(int bit)
{
    if((1 << (bit%32)) & numMask[bit/32] )
        return 1;
    else 
        return 0;
}

int bitSet(int bit)
{
    numMask[bit/32] |= (1 << (bit%32)); 
}

int pow10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};

int getPairNum(int val, int start, int end)
{
    int digit;
    int shift;
    int range;
    int shiftValue;
    
    digit = getDigit(val);
    range = 1;
    bitSet(val);
    for(shift = 1; shift < digit; shift ++)
    {
        shiftValue = (val / pow10[shift]) + ((val % pow10[shift]) * pow10[digit-shift])  ;
        
        if(shiftValue >= start && shiftValue <= end)
            if(!isBitSet(shiftValue))
            {
                bitSet(shiftValue);
                range ++;
                //printf("");
            }
    }
    
    return range * (range-1) / 2;
}

int getPairNum(int start, int end)
{
    int i;
    int pair;
        
    memset(numMask, 0, sizeof(numMask));
    pair = 0;
    for(i = start; i <= end; i ++)
    {
        if(!isBitSet(i))
        {
            pair += getPairNum(i, start, end);
            
        }
    }
    
    return pair;
}

int main(int argc, char *argv[])
{

    char *inFileName = "C-large.in";
    char *outFileName = "C-large.out";
    int i, group;
    int start, end, pairNum;
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
          fscanf(pInFile, "%d %d", &start, &end);
          printf("start %d end %d\n", start, end);
          pairNum = getPairNum(start, end);
          fprintf(pOutFile, "Case #%d: %d\n", i+1, pairNum);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}

int num[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

#if 0
void genDataBase2()
{
     int i, j, iMax, jMax;
     int d[2];
     int used[10];
     int val, shiftVal;
     
     i = j = iMax = jMax = 0;
     for(d[1] = 0; d[1] < 10; d[1] ++)
     {
            used[d[1]] = 1;
            for(d[0] = 0; d[0] < 10; d[0] ++)
            {
                if(used[d[0]] == 1)
                    continue;
                used[d1] = 1;
                val = num[d[]] * 10 + num[d1];
                for()
                
                used[d1] = 0;
            }
            used[d10] = 0;
     }
}
#endif




