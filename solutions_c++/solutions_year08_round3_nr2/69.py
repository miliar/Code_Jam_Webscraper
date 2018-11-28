#include<stdio.h>
#include<cstring>

bool Judge(long long x)
{
    return x%2==0||x%3==0||x%5==0||x%7==0;
}

int n;

int a[45],b[45];
long long tot;
char str[45];

void DFS(int x)
{
    if(x>=n)
    {
        int pre=1,i;
        long long num=a[0],res=0;
        for(i=1;i<=n-1;i++)
        {
            switch(b[i])
            {
                case 0:num=num*10+a[i];    
                    break;
                case 1:
                    if(pre==1)
                    {
                        res+=num;
                        num=a[i];
                        pre=1;
                    }
                    else
                    {
                        res-=num;
                        num=a[i];
                        pre=1;
                    }    
                    break;
                case 2:
                    if(pre==1)
                    {
                        res+=num;
                        num=a[i];
                        pre=2;
                    }
                    else
                    {
                        res-=num;
                        num=a[i];
                        pre=2;
                    }    
                    break; 
            }    

        }                         
        if(pre==1)
            res+=num;
        else
            res-=num;       
        if(Judge(res))
            tot++;
    } 
    else
    {
        int i;
        for(i=0;i<=2;i++)
        {
            b[x]=i;
            DFS(x+1);
        }    
    }    
}

int n1,i1,i;

int main()
{

    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%s",&str);
        for(i=0;i<strlen(str);i++)
        {
            a[i]=str[i]-'0';
        }
        n=strlen(str);
        tot=0;
        DFS(1);
        printf("Case #%d: %I64d\n",i1,tot);
    }
    return 0;
}        
