#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

unsigned int t;
unsigned int a,b;
unsigned int digit;
unsigned int bufM[15];
unsigned int countBuf;

bool inBuff(unsigned int n)
{
    unsigned int i;
    for (i=0; i<countBuf; i++)
        if (bufM[i]==n)
            return true;
    return false;
}

int count_digits(int n)
{
    unsigned int count=0;
    while(n > 0)
    {
        n  /= 10;
        count++;
    }
    return count;
}

void newNum (char inp[],char outp[],unsigned int k)
{
    unsigned int i;

    for (i=k; i<digit; i++)
        outp[i-k]=inp[i];

    for (i=0; i<k; i++)
        outp[i+digit -k]=inp[i];

    outp[digit]=0;
}

unsigned int newN (int a,unsigned int k,bool &flage)
{
    char stA[10];
    char stB[10];
    flage=false;

    itoa(a,stA,10);
    if (stA[k]=='0')
    {
        flage=true;
        return 0;
    }
    newNum(stA,stB,k);

    return atoi(stB);
}

int main()
{
    unsigned int i,k;
    unsigned int count;
    unsigned n,m;
    bool flag;

    cin>>t;
    for (i=0; i<t; i++)
    {
        cin>>a>>b;
        count=0;
        digit=count_digits(a);
        for (n=a; n<b; n++)
        {
            countBuf=0;
            for (k=1; k<digit; k++)
            {
                m=newN(n,k,flag);
                if (flag)
                    continue;

                if ((m>=a) &&(m<=b) && (m>n))
                    if (!inBuff(m))
                    {
                        bufM[countBuf++]=m;
                        count++;
                    }
            }
        }
        cout <<"Case #"<<i+1<<": "<< count<<endl;
    }
    return 0;
}

