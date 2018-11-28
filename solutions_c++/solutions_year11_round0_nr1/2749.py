#include<stdio.h>
#include<cstring>
int main()
{
    int t,i,n;
    int in[1000];
    char r[1000];
    //freopen("GAS.in","r",stdin);
    //freopen("GAL.out","w",stdout);
    scanf("%d",&t);getchar();
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d",&n);getchar();
        memset(in,0,sizeof(in));
        memset(r,0,sizeof(r));
        for(i=0;i<n;i++){scanf("%c %d",r+i,in+i);getchar();}
        //for(i=0;i<n;i++)printf("%c %d\n",r[i],in[i]);
        int time=0,noo=1,nob=1,neb,neo;
        for(i=0;i<n;i++)if(r[i]=='O')break;
        neo=i;
        for(i=0;i<n;i++)if(r[i]=='B')break;
        neb=i;
        while(in[neo]||in[neb])
        {
            if(neo<neb)
            {
                if(noo==in[neo])for(neo=neo+1;neo<n&&r[neo]!='O';neo++);
                else if(noo<in[neo])noo++;
                else if(in[neo])noo--;
                if(nob<in[neb])nob++;
                else if(nob>in[neb]&&in[neb])nob--;
            }
            else
            {
                if(nob==in[neb])for(neb=neb+1;neb<n&&r[neb]!='B';neb++);
                else if(nob<in[neb])nob++;
                else if(in[neb])nob--;
                if(noo<in[neo])noo++;
                else if(noo>in[neo]&&in[neo])noo--;
            }
            time++;
            //printf("t=%d o=%d b=%d onext=%d bnext=%d\n",time,noo,nob,neo,neb);
        }
        printf("Case #%d: %d\n",cn,time);
    }
    return 0;
}
