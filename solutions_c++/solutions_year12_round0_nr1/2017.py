#include <cstdio>
#include <iostream>

using namespace std;
         // abcdefghijklmnopqrstuvwxyz
char map[]="yhesocvxduiglbkrztnwjpfmaq";
char s[10000];

int main (){
  int t,i,u=0;
  gets(s);
  sscanf(s,"%d",&t);
  for (u=0;u<t;u++){
    gets(s);
    cout<<"Case #"<<(u+1)<<": ";
    for (i=0; s[i]; i++)
      if (s[i]>='a' && s[i]<='z') printf("%c",map[s[i]-'a']);
      else printf("%c",s[i]);
    cout<<endl;
  }
  return 0;
}
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
 */
