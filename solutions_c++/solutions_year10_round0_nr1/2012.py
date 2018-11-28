#include<stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n2[33],i,ii,cases,n,k;
    n2[0]=1;
    for(i=1;i<=30;i++)n2[i]=n2[i-1]*2,fprintf(stderr,"n2[%d]=%d\n",i,n2[i]);
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d",&n,&k);
        fprintf(stderr,"Case #%d: %s\n",ii,((k+1)%n2[n])==0?"ON":"OFF");
        printf("Case #%d: %s\n",ii,((k+1)%n2[n])==0?"ON":"OFF");
        //printf("Case #%d: %s\n",ii,(k/n2[n-1])%2==1?"ON":"OFF");
        //fprintf(stderr,"Case #%d: %s\n",ii,(k+1)%n2[n-1]==0?"ON":"OFF");
        //printf("Case #%d: %s\n",ii,(k+1)%n2[n-1]==0?"ON":"OFF");
    }
    fprintf(stderr,"END\n");
    while(1);
    return 0;
}
