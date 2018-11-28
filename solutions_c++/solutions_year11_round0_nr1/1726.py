#include <stdio.h>
#include <math.h>

int orange[105];
int blue[105];

typedef struct
{
    char c;
    int n;        
}order;

order a[105];

int Min(int x,int y)
{
    return x<y?x:y;    
}

int Max(int x,int y)
{
    return x>y?x:y;    
}

int Abs(int t)
{
    return t>=0?t:-t;    
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputl.out","w",stdout);
    int i,j,t,n,T,ans,ch,x,up1,up2,b,o,bnow,onow,now,cnt;
    scanf("%d",&T); 
    cnt=1;
    while(T--)
    {
        scanf("%d",&n);
        up1=up2=0;
        for (i=0;i<n;i++)          
        {
             ch=getchar();
             scanf("%c%d",&ch,&x);   
             a[i].c=ch;
             a[i].n=x; 
             if (ch=='O') orange[up1++]=x;
             if (ch=='B') blue[up2++]=x;
        }
        blue[up2++]=1000000;
        orange[up1++]=1000000;
        ans=0;
        o=0;
        b=0;
        bnow=onow=1;
        t=0;
        for (i=0;i<n;i++)
        {
       //     printf("%d..%d\n",onow,bnow);
             if (a[i].c=='O')
             {
                 t=t+Abs(orange[o]-onow)+1;
                 if (blue[b]>=bnow)
                 {
                     bnow=Min(blue[b],bnow+Abs(orange[o]-onow)+1);                  
                 }  
                 else
                 {
                     bnow=Max(blue[b],bnow-Abs(orange[o]-onow)-1);    
                 }
                 onow=orange[o]; 
                 o++;           
             }   
             else
             {
                 t=t+Abs(blue[b]-bnow)+1;
                 if (orange[o]>=onow)
                 {
                     onow=Min(orange[o],onow+Abs(blue[b]-bnow)+1);                  
                 }  
                 else
                 {
                     onow=Max(orange[o],onow-Abs(blue[b]-bnow)-1);    
                 }   
                 bnow=blue[b];
                 b++;    
             }
        }
        printf("Case #%d: %d\n",cnt++,t);
    }   
    return 0;
}
