#include<stdlib.h>
#include<stdio.h>
int main()
{freopen("A-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int i,j,k,m,n,p=0,w;
    
    scanf("%d",&m);
    
    for(i=1;i<=m;i++)
    {
    scanf("%d%d",&j,&k);
    for(w=0;w<j;w++)
     p=p*2+1;
    if((k+1)%(p+1)==0)
    printf("Case #%d: ON\n",i);
    else
    printf("Case #%d: OFF\n",i);
    p=0;
    }
    

    
    //system("pause");
    return 0;
}
