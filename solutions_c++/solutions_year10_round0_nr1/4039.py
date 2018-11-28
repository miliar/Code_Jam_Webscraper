#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
   unsigned long int t,n,k,s;
   string str;
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   cin>>t;
   for(unsigned long int m=1;m<=t;m++){
      cin>>n>>k;
      str="ON";
      s=pow(2,n);
      if((k+1)%s)
         str="OFF";
      cout<<"Case #"<<m<<": "<<str<<"\n";
   }
   return 0;
}
