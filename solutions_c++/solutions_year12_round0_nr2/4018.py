#include<stdio.h>
#include<algorithm>
int main()
{
    int T,t,N,S,P,p[100],ans,i;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&N,&S,&P);
        for(i=0;i<N;i++)
            scanf("%d",p+i);
        for(ans=0,i=N-1;i>=0;i--)
        {
            if(p[i]>=P*3-2)
                ans++;
            else if(p[i]>=P*3-4&&(P==0||p[i]>0)&&S>0)
                ans++,S--;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
