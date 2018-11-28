#include<stdio.h>
#include<string.h>
using namespace std;
char a[5000][15];
    int check[5000];
    char c[500];
    void chek(char q,int c,int t)
    {
         int i;
         if(c==0)
         {
         for(i=0;i<t;i++)
         {
            if(a[i][c]==q)
            check[i]=1;             
         }
         }
         else
         {
         for(i=0;i<t;i++)
         {
                         if(check[i]>0)
                         {
                                        if(a[i][c]==q)
                                        check[i]++;
                         }              
         }
         }
    }
    void job(int l,int t)
    {
         int i;
         for(i=0;i<t;i++)
         {
                         if(check[i]!=l)
                         check[i]=0;
         }
    }
    int total(int l,int t)
    {
        int i,res=0;
        for(i=0;i<t;i++)
        {
         if(check[i]==l)
         res++;
        }
        return res;
    }
    void initialize()
    {
         int i;
         for(i=0;i<5000;i++)
         check[i]=0;
         
    }
int main()
{
    
    int cnt=0;
    int stat;
    int l,d,n;
    int i,j;
    scanf("%d %d %d",&l,&d,&n);
    for(i=0;i<d;i++)
    {
     scanf("%s",&a[i]);
    }
    for(i=0;i<n;i++)
    {
                    initialize();
    stat=0;
    scanf("%s",&c);
    int cnt=0;
    for(j=0;j<strlen(c);j++)
    {
     if(c[j]!='(' && stat==0)
     {
        chek(c[j],cnt,d);
        cnt++;
        job(cnt,d);
     }
     else if(c[j]=='(')
     {
                  stat=1;
     }
     else if(c[j]==')')
     {
          stat=0;
          cnt++;
          job(cnt,d);
     }
     else
     {
         chek(c[j],cnt,d);
     }
    }
    printf("Case #%d: %d \n",i+1,total(cnt,d));
    }
    int c;
    scanf("%d",&c);
    return 0;
}
    
    
    
