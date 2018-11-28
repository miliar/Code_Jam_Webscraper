#include<iostream>
#include<stdio.h>
using namespace std;
unsigned long int pow(unsigned long int a,unsigned long int n){
   unsigned long int p=1;
   for(unsigned long int i=0;i<n;i++)
      p=p*a;
   return p;
}
int main(){
   unsigned long int t,n,k;
   string s1;
   freopen("in","r",stdin);
   freopen("out.txt","w",stdout);
   cin>>t;
   for(unsigned long int m=1;m<=t;m++){
      cin>>n>>k;
      s1="ON";
      if((k+1)%(pow(2,n)))
         s1="OFF";
      cout<<"Case #"<<m<<": "<<s1<<"\n";
   }
   return 0;
}
