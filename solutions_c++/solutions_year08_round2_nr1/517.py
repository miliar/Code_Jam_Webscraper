#include<iostream>
using namespace std;
#include<stdlib.h>
#include<algorithm>

const int MAXN = 200;
struct point
{
   unsigned long long x,y;
   friend bool operator!=(const point &a,const point &b);
   
}a[MAXN];
long n,m;
unsigned long long A,B,C,D;


bool operator!=(const point &a,const point &b)
{
    return a.x!=b.x||a.y!=b.y;
}

bool operator<(const point &a,const point &b)
{
  if(a.x!=b.x)
  return a.x<b.x;
  return a.y<b.y;
}
     
     
long sum;
inline bool bound(const point &a,const point &b,const point &c)
{
  return a!=b&&a!=c&&b!=c&&((a.x+b.x+c.x)%3==0)&&((a.y+b.y+c.y)%3==0);
}
     
void input()
{
   long i,j,k;  
   scanf("%ld%I64u%I64u%I64u%I64u%I64u%I64u%ld",&n,&A,&B,&C,&D,&a[0].x,&a[0].y,&m);
   
   A%=m;
   B%=m;
   C%=m;
   D%=m;
   
   for(i=1;i<n;i++)
   {
     a[i].x = (((a[i-1].x%m)*A)%m+B)%m;
     a[i].y = (((a[i-1].y%m)*C)%m+D)%m;
   }
   
  /* sort(a,a+n);
   
   for(i=k=0;i<n;i++)
   {
     a[k++] = a[i];
     for(j=i+1;j<n&&a[j].x==a[i].x&&a[j].y==a[i].y;j++);
     
    i = j-1;
   }
   n = k;
    */            
   
}

/*void output()
{
     long i;
     for(i=0;i<n;i++)
     printf("%ld %ld   ",a[i].x,a[i].y);
     printf("\n");
     }                                  
*/       
int main()
{
  freopen("A.txt","w",stdout);

    
     long caseamount,casenum = 1;
     long i,j,k;
     scanf("%ld",&caseamount);
     while(caseamount--)
     {
        input();
       // output();
        
        for(i = sum = 0;i<n-2;i++)
         for(j=i+1;j<n-1;j++)
          for(k=j+1;k<n;k++)
          if(bound(a[i],a[j],a[k]))
          sum++;
       
       printf("Case #%ld: %ld\n",casenum++,sum);
       }
    
   //system("pause");
   return 0;
}     


