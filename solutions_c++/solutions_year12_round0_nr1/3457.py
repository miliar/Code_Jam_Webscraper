#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
  freopen("A-small-attempt2.in","r",stdin);
  freopen("a.txt","w",stdout);
  int cases,i,T;
  char table[27]="yhesocvxduiglbkrztnwjpfmaq",str[102];
  cin>>T;
  getchar();
  for(cases=1;cases<=T;cases++)
  {
    gets(str);
    for(i=0;str[i];i++)
    {
      if(str[i]!=32)
        str[i]=table[str[i]-97];
    }
    printf("Case #%d: %s\n",cases,str);
  }
  return 0;
}
