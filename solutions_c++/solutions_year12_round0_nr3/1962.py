#include<stdio.h>
#include<iostream>
using namespace std;
const int MAXN=2000100;
bool used[MAXN];
int len;
int getlen(int n)
{
    int len=0;
    while(n>0)
    {
        n/=10;
        len++;
    }    
    return len;
}    
int RR(int n)
{
    int ge=n%10;
    int tmp=1;
    int tmplen=len-1;
    while(tmplen--)
           tmp*=10;
    n/=10;
    n+=tmp*ge;
    return n;
}    
int main()
{
   // freopen("C-large.in","r",stdin);
    //freopen("test.out","w",stdout);
    int T,A,B;
    int res;
    scanf("%d",&T);
    int iCase=0;
    while(T--)
    {
        iCase++;
        scanf("%d%d",&A,&B);
        memset(used,0,sizeof(used));
        int res=0;
        for(int i=A;i<=B;i++)
        {
            if(used[i]) continue;
            used[i]=1;
            len=getlen(i);
            int tmp=RR(i);
            while(tmp!=i)
            {
                if(i<tmp&&tmp>=A&&tmp<=B&&getlen(tmp)==len)
                {
                    res++;
                   // used[tmp]=1;
                    //printf("%d %d\n",i,tmp);
                }    
                tmp=RR(tmp);
            }    
        }    
        printf("Case #%d: %d\n",iCase,res);
        
    }    
    return 0;  
}    
