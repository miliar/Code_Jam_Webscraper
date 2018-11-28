#include <cstdio>

#include <cstring>

int op(int p)
{
    int kk=p,s1=1;
    while(kk>0)
    {
        s1*=10;       
        kk/=10;   
    }
    return s1;
}
int b1[11]={0},r,o;
int main()
{
     freopen("1.in","r",stdin);
     freopen("1.out","w",stdout);
     int T,a,b,s,pp,ppp=0,ans1=0;
     scanf("%d",&T);
     while(T--)
     {
         ppp++;      
         int ans=0;      
         ans1=0;
         scanf("%d%d",&a,&b);
         for(int i=a;i<=b;i++)
         {
             int k,tmp=i,t=i,d=1;
             k=op(i);
             k/=10;
             s=0;
             r=0;
             while(tmp>0)
             {
                t/=10;         
                s=s+d*(tmp%10);
                d=d*10;
                tmp/=10;
                pp=s*k+t;
                k/=10;
                o=0;
                if(i<pp && pp<=b)
                { 
                for(int iq=0;iq<r;iq++)
                {
                     if(b1[iq]==pp){o=1;  break; }        
                }
                if(o==0){ b1[r++]=pp; 
                        ans++;} 
                }
                //printf("%d %d ",pp,s);
             }        
         }   
         printf("Case #%d: %d\n",ppp,ans);
     }    
     //for(;;);
     return 0;
}
