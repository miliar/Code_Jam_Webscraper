#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    int T,N,K,i,fs,bin[50],top,res;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d %d",&N,&K);
        printf("Case #%d: ",i);
        if(N==1)
        {
            if(K%2==0) printf("OFF\n");
            else printf("ON\n");
            continue;
        }
        top = 0;
        res = 0;
        while(K>0)
        {
            bin[top]=K%2;
            res += bin[top];
            K/=2;
            top++;
            if(top==N) break;
        }
        if(res == N && res != 0)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
