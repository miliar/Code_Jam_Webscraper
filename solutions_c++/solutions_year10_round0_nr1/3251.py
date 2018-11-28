#include<iostream>
#include<cstdio>
using namespace std;


int pot(int n)
{
 int ans=1,k=2;
 while(n>0)
 {
   if(n&1)          
     ans*= k;
   k=k*k;   
   n>>=1;   
 }
 return ans;
}

int t,s,k;
int main()
{
  cin>>t;
  for (int i=0;i<t;i++)
  {
   cin >>s>>k;
   if ((k+1)%pot(s)==0)
   cout <<"Case #"<<i+1<<": ON"<<endl;
   else
   cout <<"Case #"<<i+1<<": OFF"<<endl;
      
  }
  //system ("pause");
return 0;    
}
