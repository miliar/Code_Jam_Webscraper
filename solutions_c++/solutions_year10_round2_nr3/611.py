#include<stdio.h>
#include<cstring>

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int cases,ii,n,i,an,rank[505],rs;
    int y[505],aa[505];
    scanf("%d",&cases);
    for(n=1;n<=25;n++)
    {
        //scanf("%d",&n);
        memset(y,0,sizeof(y));
        an=0;
        
        do
        {
            rs=0;
            for(i=1;i<=n;i++)
            {
                if(y[i])rank[i]=++rs;
            }
            bool yes=0;
            if(y[n])
            {
                yes=1;
                int t=n;
                while(t!=1)
                {
                    //fprintf(stderr,"t=%d rank =%d yes=%d\n",t,rank[t],yes);
                    if(rank[t]==1)break;
                    if(!y[rank[t]] || t==rank[t])
                    {
                        yes=0;
                        break;
                    }
                    t=rank[t];
                    
                }
            
                if(yes)
                {
                    an++;
                    an%=100003;
                }  
            }
            //for(i=1;i<=n;i++)fprintf(stderr,"%d ",y[i]);fprintf(stderr,"\n");
            //fprintf(stderr,"yes=%d\n",yes);
            y[1]++;
            for(i=1;i<=n;i++)y[i+1]+=y[i]/2,y[i]%=2;
        }while(!y[n+1]);
        aa[n]=an;
        fprintf(stderr,"aa[%d]=%d\n",n,aa[n]);
    }
    
    
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&n);
        printf("Case #%d: %d\n",ii,aa[n]);
    }
    fprintf(stderr,"END\n");
    while(1);
    
    return 0;
}
