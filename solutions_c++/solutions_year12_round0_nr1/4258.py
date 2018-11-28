#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
int j,tc;
cin>>tc;
for(j=1;j<=tc;j++)
{
 if(j==1)
 {
 string dummy;
 getline(cin,dummy);
 }
 string tick="yhesocvxduiglbkrztnwjpfmaq";
 string input="",answer="";
 int i=0;
 getline(cin,input);
 int length=input.length();
 for(i=0;i<length;i++)
  {
  if(input[i]==' ')
   {
    answer+=" ";
    continue;
   }
  answer+=tick[(int)input[i]-97];
  }
  cout<<"Case #"<<j<<": "<<answer<<"\n";
}
return 0;
}
