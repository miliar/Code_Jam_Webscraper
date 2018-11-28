#include<iostream>
#include<cstdio>
#include<cstdlib>
#define MAX 200
using namespace std;

char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
    int i,j,t;
    char st[MAX+1];
    gets(st);
    t=atoi(st);
    j=1;
    while (t--){
          gets(st);
          printf("Case #%d: ",j);
          for (i=0;i<strlen(st);++i){
              if(st[i]>='a' && st[i]<='z')printf("%c",a[(int)(st[i]-'a')]);
              else printf("%c",st[i]);
              }
          printf("\n");
          ++j;
          }
    
    return 0;
    }
