#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>

#define Q 100
#define P 10000

int t;
int p,q;
int tofree[Q];
bool isfree[P];

long long Calc(int actp, long long actc)
{
    int i,j;

    isfree[actp]=true;
    // count neighbours
    int cost=0;
    // left
    for(i=actp-1; i>=0; i--)
    {
        if(!isfree[i])
        {
            ++cost;
        }
        else
        {
            break;
        }
    }
    // right
    for(i=actp+1; i<p; i++)
    {
        if(!isfree[i])
        {
            ++cost;
        }
        else
        {
            break;
        }
    }

    int tofreec=0;
    long long min=LLONG_MAX;
    for(i=0; i<q; i++)
    {
        if(!isfree[tofree[i]])
        {
            // prisoner to free
            ++tofreec;
            long long res = Calc(tofree[i], actc+cost);
            if(res<min)
            {
                min=res;
            }
        }
    }

    isfree[actp]=false;

    if(tofreec==0)
    {
        // this was the last so result
        return actc+cost;
    }
    else
    {
        // return min
        return min;
    }

}

int main()
{
    int i,j;

    scanf("%d", &t);

    for(i=0; i<t; i++)
    {
        memset(isfree,false,P);
        scanf("%d%d", &p, &q);

        for(j=0; j<q; j++)
        {
            scanf("%d", tofree+j);
            tofree[j]--;
        }

        // start with each and get min
        long long min=LLONG_MAX;
        for(j=0; j<q; j++)
        {
            long long res = Calc(tofree[j], 0);
            if(res<min)
                min=res;
        }

        printf("Case #%d: %lld\n", i+1, min);
    }

    return 0;
}
