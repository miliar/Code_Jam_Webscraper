#include<iostream>
#include<string>
#include<cstdio>
using namespace std;


int main()
{
   int Z;
   scanf("%d",&Z);
   for(int z=1;z<=Z;z++)
   {
      int n,q,p,a,mi,mi2,res=0;
      scanf("%d %d %d",&n,&q,&p);
      mi=max(p,p*3-2);
      mi2=max(p,p*3-4);
      for(int i=0;i<n;i++)
      {
         scanf("%d",&a);
         if(a>=mi)res++;
         if(mi>a && a>=mi2 && q){q--;res++;}
      }
      cout<<"Case #"<<z<<": "<<res<<endl;
   }
   return 0;
}
