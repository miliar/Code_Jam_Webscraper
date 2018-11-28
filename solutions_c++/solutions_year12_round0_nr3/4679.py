 #include<stdio.h>
#include<conio.h>
#include<cmath>

int count;

inline int telldigits(int x)
{
   if(x<10) return 0;
   else if(x<100) return 2;
   else if(x<1000)return 3;
   else if(x<10000) return 4;
   else if(x<100000) return 5;
   else if(x<1000000) return 6;
   else if(x<2000000) return 7;
} 

inline void rcs(int n,int m,int len,int len1)
{
    int temp=n,temp1;
    if(len==len1)
    {
        while(n>0)
    {
                 n=n/10;
                 temp1=((pow(10.00,len-1)*(temp%10))+floor(temp/10));
                 if(temp1==m) 
                 {
                              
                              count++;
                              break;
                 }
                 temp=temp1;
                 
    }
    }
}

int main()
{
int t,a,b,i,j,test,temp_,temp_2;

freopen("C-small-attempt1.in","r",stdin);
freopen("code2.txt","w",stdout);
int p=1;
scanf("%d",&t);
while(t--)
{
         count=0;
         scanf("%d %d",&a,&b);
         for(i=a;i<=b-1;i++)
         {
                            for(j=i+1;j<=b;j++)
                            {
                                               rcs(i,j,telldigits(i),telldigits(j));
                            }
         }
         printf("Case #%d: %d\n",p,count);   
         p++;                                
}
return 0;
}
