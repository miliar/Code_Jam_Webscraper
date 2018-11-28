#include<iostream>
#include<cstdio>
 
using namespace std;
 
int main(void)
{
 int t, cas=1, i;
 char s[101];
 char c[26]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
 scanf("%d\n", &t);
 while(t--)
 {
           fflush(stdin);
           gets(s);
           for(i=0;s[i]!='\0';i++)
           {
                                  if(s[i]>='a'&&s[i]<='z')
                                                          {
                                                            s[i]=c[s[i]-'a'];
                                                            }
                                  }
           printf("Case #%d: %s\n", cas++, s);
           }
 return 0;
}
