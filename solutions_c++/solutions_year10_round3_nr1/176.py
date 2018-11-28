#include <iostream>
#include <algorithm>
using namespace std;




struct line
{
int a,b;    
};

bool com(const line &l1,const line &l2)
{
return l1.a<l2.a;    
}
int t,n;

line l[2000];

int main()
{
cin >>t;
for(int p=1;p<=t;p++)
  {
      
   cin >>n;
   for(int i=1;i<=n;i++)
     cin>>l[i].a>>l[i].b;
   sort(&l[1],&l[n+1],com);
   int ans=0;
   for(int i=1;i<=n;i++)
     {
      for(int j=1;j<=i-1;j++)
        if(l[i].b<l[j].b)ans++;    
     }
   printf("Case #%d: %d\n",p,ans);
  }
return 0;    
}
