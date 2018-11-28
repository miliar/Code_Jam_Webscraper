#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
char st[1000];
int main(void)
{
 int t,flag=1;
 scanf("%d\n",&t);
 t=1;
 char sss[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 while (cin>>st) {
  if (flag) printf("Case #%d: ",t),flag=0;
  int len=strlen(st);
  for (int i=0;i<len;i++) printf("%c",sss[st[i]-'a']);
  char ch; ch=getchar();
  if (ch==' ') printf(" "); else puts(""), t++, flag=1;
 }
 return 0;
}
