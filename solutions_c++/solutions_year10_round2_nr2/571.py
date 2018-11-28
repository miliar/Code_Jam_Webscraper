#include <iostream>

using namespace std;

int c,b,n,k,t,x[100],v[100];

int main()
{
cin >>c;
for(int p=1;p<=c;p++)
{
cin >>n>>k>>b>>t;
int i;
for(i=1;i<=n;i++)
  cin>>x[i];
for(i=1;i<=n;i++)
  cin>>v[i];
int ans=0;
int total=0;
bool boolean=false;
for(i=n;i>=1;i--)
 {
   if(t*v[i]+x[i]>=b)
     total++;
   else ans +=k-total;
   if(total>=k){boolean=true;break;}
   if(i==1&&total<k){boolean=false;break;}
 }
if(boolean)
  printf("Case #%d: %d\n",p,ans);
else printf("Case #%d: IMPOSSIBLE\n",p);
}


return 0;
}
