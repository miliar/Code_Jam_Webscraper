#include<iostream>
#include<map>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
   freopen("n.txt","w",stdout);
   int t;
   cin>>t;
   for(int k=0;k<t;k++)
   {
      int n,s,p;
      cin>>n>>s>>p;
      int f1=0,f2=0;
      for(int i=0;i<n;i++)
      {
        int v;
        scanf("%d",&v);
        if(v>=max(p,3*p-2))
           f1++;
        else if(v>=max(p,3*p-4))
        {
           //cout<<v<<' '<<3*p-4<<endl;
           f2++;
           }
      }
      //cout<<f1<<' '<<f2<<endl;
      printf("Case #%d: %d\n",k+1,f1+min(f2,s));
   }
   return 0;
}
        
