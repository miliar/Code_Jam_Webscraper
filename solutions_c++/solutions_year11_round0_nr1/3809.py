#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("al.out","w",stdout);
    int t,i,j,po,pb,n,sec,time,proo,prob,P[1000],kase=0;
    char R[1000];
    scanf(" %d",&t);
    while (t--)
    {
        scanf(" %d",&n);
        for (i=0;i<n;i++)
        {
            scanf(" %c",&R[i]);
            scanf(" %d",&P[i]);
        }
        sec=0;
        po=1;
        pb=1;
        proo=0;
        prob=0;
        for (i=0;i<n;i++)
        {
            time=0;
            if (R[i]=='O')
            {
                time=abs(P[i]-po)+1;
                if (time>proo)
                {
                    sec+=time-proo;
                    prob+=(time-proo);
                    proo=0;
                }
                else
                {
                    sec+=1;
                    prob+=1;
                    proo=0;
                }
                po=P[i];
            }
            else if (R[i]=='B')
            {
                time=abs(P[i]-pb)+1;
                if (time>prob)
                {
                    sec+=time-prob;
                    proo+=(time-prob);
                    prob=0;
                }
                else
                {
                    sec+=1;
                    proo+=1;
                    prob=0;
                }
                pb=P[i];
            }
        }
        printf("Case #%d: %d\n",++kase,sec);

    }
    return 0;
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
