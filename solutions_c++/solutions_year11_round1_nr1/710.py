#include <iostream>
#include <cstdio>

using namespace std;

int gcd(int a,int b){
   int c=a%b;
   if(c)
      return gcd(b,c);
   else
      return b;
}

int main()
{
   int t;
   cin>>t;
   for(int i=0;i<t;i++){
      bool ans=false;
      long long int n,p1,p2;
      int dt=100;
      cin>>n>>p1>>p2;
      if((p2==100 && p1<100)||(p1>0 && p2==0) || p1>100 || p2>100 || p1<0 || p2<0){
         ans=false;
      }else if(!p1){
         ans=true;      
      }else{
         int gc=gcd(dt,p1);
         dt/=gc;
         ///printf("gc:%d dt:%d\n",gc,dt);
         if(dt<=n)
            ans=true;
      }
      if(ans)
         cout<<"Case #"<<(i+1)<<": Possible"<<endl;
      else
         cout<<"Case #"<<(i+1)<<": Broken"<<endl;
   }
   return 0;
}
