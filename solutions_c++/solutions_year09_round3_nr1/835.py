#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

bool exists[130];
int value[130];
int digitanz;
char digit[65];
int digitlen;

int t;

int main()
{
    int i,j;

    scanf("%d\n", &t);
    
    for(i=0; i<t; i++)
    {
        memset(exists,false,130);
        memset(value,-1,130*sizeof(int));
        gets(digit);
        digitlen=strlen(digit);
        digitanz=0;

        for(j=0; j<digitlen; j++)
        {
            if(!exists[digit[j]])
            {
                // new digit
                ++digitanz;
                exists[digit[j]]=true;
            }
        }

        if(digitanz==1)
            digitanz=2;
        
        // assign values
        value[digit[0]]=1;
        
        // assign value 0
        for(j=1; j<digitlen; j++)
        {
            if(digit[j]!=digit[0])
            {
                value[digit[j]]=0;
                break;
            }
        }

        int actvalue=2;
        // calculate values
        for(j=0; j<digitlen; j++)
        {
            if(value[digit[j]]==-1)
            {
                value[digit[j]]=actvalue;
                ++actvalue;
            }
        }

        // now calc result;
        long long result=0;
        for(j=0; j<digitlen; j++)
        {
            result += value[digit[digitlen-j-1]]*(int)pow(digitanz,j);
        }

        printf("Case #%d: %lld\n", i+1, result);
    }

    return 0;
}
