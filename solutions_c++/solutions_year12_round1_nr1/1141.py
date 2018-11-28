#include"stdio.h"
int T,i,j,n,m;
double pos[100005],qm[100005],min,tmp;
int main()
{
    //freopen("2.in","r",stdin);
    //freopen("2.txt","w",stdout);
    scanf("%d",&T);
    qm[0]=1;
    for(j=1;j<=T;j++)
    {
        scanf("%d%d",&m,&n);
        for(i=1;i<=m;i++)
        {
            scanf("%lf",&pos[i]);
            qm[i]=qm[i-1]*pos[i];
        }
        min=qm[m]*(n-m+1)+(1.0-qm[m])*(2*n-m+2);
        for(i=1;i<=m;i++)
        {
            tmp=qm[m-i]*(n-m+1+2*i)+(1.0-qm[m-i])*(2.0*(n+1+i)-m);
            if(tmp<min) min=tmp;
        }
        if(n+2<min) min=n+2;
        printf("Case #%d: %lf\n",j,min);
    }
    scanf(" ");
}
