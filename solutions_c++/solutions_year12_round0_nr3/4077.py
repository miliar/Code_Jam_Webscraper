
#include<stdio.h>
#include<string>

int check(long a,long b)
{
    char ch[30];
    int len,i,ans=0;
    long tmp;
    ltoa(a,ch,10);
    len=strlen(ch);
    
    for(i=0;i<len;i++)ch[len+i]=ch[i];   
    ch[i+len]='\0';
    //printf("%s ",ch);
    
    for(i=len-1;i>=1;i--)
    {
        *(ch+len+i)='\0';
        tmp=atol(ch+i);
        if(tmp>a&&tmp<=b)ans++;  
        
    }
    return ans;
    
}
int main()
{
    int i,j,n,ans;
    long a,b;
    scanf("%d",&n);
    
    for(i=1;i<=n;i++)
    {
        scanf("%ld%ld",&a,&b);
        ans=0;
        printf("Case #%d: ",i);
        
        for(j=a;j<=b;j++)ans=ans+check(j,b);
        
        printf("%d\n",ans);
    }   
    
    
}
