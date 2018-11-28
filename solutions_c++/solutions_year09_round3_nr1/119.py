#include<stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cases,ii,cs,a[333],i;
    char ss[102];
    long long int an;
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%s",ss);
        for(i='0';i<='9';i++)a[i]=-1;
        for(i='a';i<='z';i++)a[i]=-1;
        cs=0;
        for(i=0;ss[i];i++)
        {
            if(a[ss[i]]==-1)
            {
                cs++;
                if(cs==1)a[ss[i]]=1;
                else if(cs==2)a[ss[i]]=0;
                else a[ss[i]]=cs-1;
            }
        }
        an=0;
        if(cs<2)cs=2;
        for(i=0;ss[i];i++)an=an*cs+a[ss[i]];
        //fprintf(stderr,"Case #%d: %I64d\n",ii,an);
        printf("Case #%d: %I64d\n",ii,an);
    }
    fputs("END\n",stderr);
    while(1);
    return 0;
}
