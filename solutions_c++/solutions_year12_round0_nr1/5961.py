#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main(int argc,char *argv[])
{
  freopen("A-small-attempt0.in","r",stdin);
  int ans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  string refer="yhesocvxduiglbkrztnwjpfmaq",str;
  int T,i,j;
  scanf("%d\n",&T);
  for(j=1;j<=T;j++)
  {
    getline(cin,str);
    for(i=0;i<str.length();i++)
    {
      if(str[i]!=' ')
        str[i]=refer[str[i]-97];
    }
    printf("Case #%d: %s\n",j,str.c_str());
  }
  return 0;
}
