#include<iostream>
#include<string.h>
using namespace std;
 
 
 
 
 
 
 
int main()
{
int t;
cin>>t;
char str[800];
 
char s[]="yhesocvxduiglbkrztnwjpfmaq";
int i,j;
gets(str);
for(j=1;j<=t;j++)
{
gets(str);
for(i=0;str[i]!='\0';i++)
{
if(str[i]!=' ')
{
str[i]=s[str[i]-97];
}
}
cout<<"Case #"<<j<<": "<<str<<"\n";
}
}
 