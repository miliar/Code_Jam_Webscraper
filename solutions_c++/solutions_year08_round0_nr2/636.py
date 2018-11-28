#include <iostream>
#include <stdio.h> 
//#include <string>
//#include <map>
#include <stdlib.h>

using namespace std;

#define DAY_MINUTE (24*60+1)

int main()
{
    int N,NA,NB,T;
    int a[DAY_MINUTE];
    int b[DAY_MINUTE];
    int h,m;
    int A,B;
    int sa,sb;//start train
    scanf("%d",&N);
    for(int i=1;i<=N;i++)
    {
        memset(a,0,sizeof(int)*DAY_MINUTE);
        memset(b,0,sizeof(int)*DAY_MINUTE);
        scanf("%d",&T);
        scanf("%d %d",&NA,&NB);
        for(int j=0;j<NA;j++)
        {
            scanf("%d:%d",&h,&m);
            a[h*60+m]--;
            scanf("%d:%d",&h,&m);
            if(h*60+m+T<(DAY_MINUTE-1))
            {
                b[h*60+m+T]++;
            }
        }
        for(int j=0;j<NB;j++)
        {
            scanf("%d:%d",&h,&m);
            b[h*60+m]--;
            scanf("%d:%d",&h,&m);
            if(h*60+m+T<(DAY_MINUTE-1))
            {
                a[h*60+m+T]++;
            }
        }
        A=0;B=0;
        sa=0;sb=0;
        for(int j=0;j<DAY_MINUTE;j++)
        {
            if(a[j]<0)
            {
                if(a[j]+A>=0)
                {
                    A=a[j]+A;
                }
                else
                {
                    sa+=(-a[j]-A);
                    A=0;
                }
            }
            else
            {
                A += a[j];
            }

            if(b[j]<0)
            {
                if(b[j]+B>=0)
                {
                    B=b[j]+B;
                }
                else
                {
                    sb+=(-b[j]-B);
                    B=0;
                }
            }
            else
            {
                B += b[j];
            }
        }
        printf("Case #%d: %d %d\n",i,sa,sb);
    }

}