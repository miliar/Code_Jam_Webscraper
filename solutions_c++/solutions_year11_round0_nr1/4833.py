#include<stdio.h>
#include<string.h>

long abs(long a)
{
    if(a>=0) return a;
    else     return (a*(-1));    
}
  
int main()
{
    long a,c,i,n,t,o,b,ot,bt,time,cell,cas=1;
    char ch,ch1;
    
    freopen("c:\\inp\\a.in","r",stdin);
    freopen("c:\\out\\a.out","w",stdout);
    scanf("%ld",&t);
    while(t--)
    {
        scanf("%ld",&n);        
        time=0;
        o=1;
        ot=0;
        b=1;
        bt=0;
        
        getchar();
        for(i=0; i<n; i++)
        {
            scanf("%c%ld",&ch,&cell);
            //printf("%c",ch);
            getchar();
            if(ch=='O')
            {
                if((time-ot)<abs(cell-o))
                {
                   time=ot+abs(o-cell);
                }
                time++;
                o=cell;
                ot=time;
            }
            else if(ch=='B')
            {
                if((time-bt)<abs(b-cell))
                {
                   time=bt+abs(b-cell);
                }
                time++;
                b=cell;
                bt=time;
            }
//            printf("%ld %c",time,ch);
        }
        
        printf("Case #%ld: %ld\n",cas++,time);
    }
    
    
    return 0;    
}
