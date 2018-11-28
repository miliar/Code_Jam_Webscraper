#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
  int t=0,j=1,i=0;
  char s[27]="yhesocvxduiglbkrztnwjpfmaq";
  string str;
  cin>>t;
  getline(cin,str);
  while(t--)
  {

   getline(cin,str); 
    printf("Case #%d: ",j++);
   for(i=0;i<str.length();i++)
   {
     if(str[i]==' ')
               printf(" ");
     else
               printf("%c",s[str[i]-'a']);
  }
  printf("\n");
  }
return 0;
}
