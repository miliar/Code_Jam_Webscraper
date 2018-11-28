#include<iostream>
#include<string.h>
using namespace std;
 
int main()
{
 int t,i,j;
 cin>>t;
 char a[1000];
 char b[]="yhesocvxduiglbkrztnwjpfmaq";
 
 gets(a);
 for(i=1;i<=t;i++)
 {
   gets(a);
   for(j=0;a[j]!='\0';j++)
   {
    if(a[j]!=' ')
    {
     a[j]=b[a[j]-97];
    }
   }
   cout<<"Case #"<<i<<": "<<a<<"\n";
 }
}