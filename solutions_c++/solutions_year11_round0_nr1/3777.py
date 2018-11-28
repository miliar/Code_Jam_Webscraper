#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define MAXN 105
using namespace std;
char ope[MAXN];
int step[MAXN];
int t, n;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &t);
    for(int k=1; k<=t; k++)
    {
        scanf("%d", &n);
        int flago=1, flagb=1, sum=0;
        int sumo=0, sumb=0;
        for(int i=0; i<n; i++)
        {
            scanf("%s %d", &ope[i], &step[i]);
        }
        for(int i=1; i<n; i++)
        {
            if(ope[i]==ope[i-1])
            {
                if(ope[i]=='O')
                {
                    sum+=abs(step[i-1]-flago)+1;
                    sumo=sum;
                    flago=step[i-1];
                }
                else
                {
                    sum+=abs(step[i-1]-flagb)+1;
                    sumb=sum;
                    flagb=step[i-1];
                }
            }
            else
            {
                if(ope[i]=='O')
                {
                    int o=abs(step[i]-flago);
                    int b=abs(step[i-1]-flagb);
                    sum+=b+1;
                    sumb=sum;
                    flagb=step[i-1];
                    if(o<=(sum-sumo)) flago=step[i];
                    else
                    {
                        if(step[i]<flago) flago-=sum-sumo;
                        else flago+=sum-sumo;
                    }
                    sumo=sum;
                }
                else
                {
                    int o=abs(step[i-1]-flago);
                    int b=abs(step[i]-flagb);
                    sum+=o+1;
                    sumo=sum;
                    flago=step[i-1];
                    if(b<=(sum-sumb)) flagb=step[i];
                    else
                    {
                        if(step[i]<flagb) flagb-=sum-sumb;
                        else flagb+=sum-sumb;
                    }
                    sumb=sum;
                }
            }
        }
        if(ope[n-1]=='O')
            sum+=abs(step[n-1]-flago)+1;
        else
            sum+=abs(step[n-1]-flagb)+1;
        printf("Case #%d: %d\n", k, sum);
    }
    return 0;
}
