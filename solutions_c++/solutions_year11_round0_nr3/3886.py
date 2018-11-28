#include<stdio.h>
#include<vector>
#include<bitset>
#include<iostream>
#include<conio.h>
using namespace std;

#define max(a,b) (a>=b?a:b)
int t=1,tests,n,i,patrick,sean,xors,xorp,ans=-1,j;
vector<int> a;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("candy_splitting.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {
         a.clear();
         scanf("%d",&n);
         for(i=0;i<n;i++)
         {
             int temp;
             scanf("%d",&temp);
             a.push_back(temp);
         }            
         ans=-1;
         for(i=1;i<(1<<n)-1;i++)
         {
             patrick=0;
             sean=0;
             xors=0;
             xorp=0;             
             bitset<15> bits(i);            
             for(j=0;j<n;j++)
             {                  
                  if(bits[j])
                  {sean+=a[j];xors^=a[j];}
                  else
                  {xorp^=a[j];} 
             }             
             if(xors==xorp)
             {       
                ans=max(ans,sean);
             }
         }
         if(ans==-1)
         {printf("Case #%d: NO\n",t);}
         else
         {printf("Case #%d: %d\n",t,ans);}
         t++;         
    }
    getch();
}
