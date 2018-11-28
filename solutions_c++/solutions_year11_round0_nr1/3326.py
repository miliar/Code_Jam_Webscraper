#include<stdio.h>
#include<stdlib.h>
struct node
{
    int order;
    int button;   
}O[110],B[110];
int abs(int x)
{
    if(x<0)
        return x*-1;
    return x;   
}
int main()
{
    int tcase,i,j,k,l,n,b;
    int sizeO,sizeB,time;
    int curO,curB,diff,temp;
    char c;
    freopen("A-large.in","rt",stdin);
    freopen("bot.out","wt",stdout);
    scanf("%d",&tcase);
    for(int l=1;l<=tcase;l++)
    {
        scanf("%d",&n);
        for(k=1,sizeO=0,sizeB=0;k<=n;k++)
        {
            scanf(" %c %d",&c,&b);
            if(c=='O')
            {
                sizeO++;
                O[sizeO].order=k;
                O[sizeO].button=b;   
            }
            else if(c=='B')
            {
                sizeB++;
                B[sizeB].order=k;
                B[sizeB].button=b;   
            }
        }
        i=1;
        j=1;
        curO=1;
        curB=1;
        time=0;
        while(i<=sizeO && j<=sizeB)
        {
            if(O[i].order < B[j].order)
            {
                diff=abs(O[i].button-curO)+1;
                time+=diff;
                curO=O[i].button;
                i++;
                temp=abs(B[j].button-curB)+1;
                if(temp>diff)
                {
                    if(curB<B[j].button)
                        curB+=diff;
                    else
                        curB-=diff;
                }
                else
                    curB=B[j].button;
            }
            else
            {
                diff=abs(B[j].button-curB)+1;
                time+=diff;
                curB=B[j].button;
                j++;
                temp=abs(O[i].button-curO)+1;
                if(temp>diff)
                {
                    if(curO<O[i].button)
                        curO+=diff;
                    else
                        curO-=diff;
                }
                else
                    curO=O[i].button;
            }
        }
        while(i<=sizeO)
        {
            time+=abs(O[i].button-curO)+1;
            curO=O[i++].button;   
        }
        while(j<=sizeB)
        {
            time+=abs(B[j].button-curB)+1;
            curB=B[j++].button;   
        }
        printf("Case #%d: %d\n",l,time);
    }
    //system("pause");
    return 0;   
}
