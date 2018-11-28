#include<iostream>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    int T,N,K,i,VAL;
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        scanf("%d%d",&N,&K);
        VAL = K+1 - (1<<N);
        if (VAL >=0 && VAL%(1<<N)==0)
           printf("Case #%d: ON\n",i);
        else
            printf("Case #%d: OFF\n",i);
    }
}
