#include<stdio.h>
#include<cstring>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int i,j,D,L,N,an,ii,y;
    bool ok[22][333],in,yes;
    char word[5002][22],ss[222222];
    
    scanf("%d%d%d",&L,&D,&N);
    
    for(i=1;i<=D;i++)
        scanf("%s",word[i]);
        
    for(i=1;i<=N;i++)
    {
        scanf("%s",ss);
        in=0;
        y=0;
        memset(ok,0,sizeof(ok));
        for(j=0;ss[j];j++)
        {
            if(ss[j]=='(')
                in=1;
            else if(ss[j]==')')
                in=0,y++;
            else
            {
                ok[y][ss[j]]=1;
                //fprintf(stderr,"ok[%d][%c]=1\n",y,ss[j]);
                if(!in)y++;
            }
        }
        
        an=0;
        for(j=1;j<=D;j++)
        {
            yes=1;
            for(ii=0;ii<L;ii++)
            {
                //fprintf(stderr,"j=%d ok %d %c\n",j,ii,word[j][ii]);
                if(!ok[ii][word[j][ii]])
                    yes=0;
            }
            if(yes)an++;
            //fprintf(stderr,"word %s  yes=%d\n",word[j],yes);
        }
        printf("Case #%d: %d\n",i,an);
    }
    fputs("END",stderr);
    while(1);
    return 0;
}
