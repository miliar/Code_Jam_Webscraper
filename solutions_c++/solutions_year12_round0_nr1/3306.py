#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

char tong(char c)
{
 switch(c)
 {
  case 'a': return 'y';break;
  case 'b': return 'h';break;
  case 'c': return 'e';break;
  case 'd': return 's';break;
  case 'e': return 'o';break;
  case 'f': return 'c';break;
  case 'g': return 'v';break;
  case 'h': return 'x';break;
  case 'i': return 'd';break;
  case 'j': return 'u';break;
  case 'k': return 'i';break;
  case 'l': return 'g';break;
  case 'm': return 'l';break;
  case 'n': return 'b';break;
  case 'o': return 'k';break;
  case 'p': return 'r';break;
  case 'q': return 'z';break;
  case 'r': return 't';break;
  case 's': return 'n';break;
  case 't': return 'w';break;
  case 'u': return 'j';break;
  case 'v': return 'p';break;
  case 'w': return 'f';break;
  case 'x': return 'm';break;
  case 'y': return 'a';break;
  case 'z': return 'q';break;
  default: return ' ';
 }
}

int main()
{
 int test;
 char enter;
 scanf("%d",&test);
 
 scanf("%c",&enter);
 for(int cases=1;cases<=T;cases++)
 {
  char st[101];
  gets(st);
  int l=strlen(st);
  cout<<"Case #"<<cases<<": ";
  for(int i=0;i<l;i++)
  {
   cout<<tong(st[i]);
  }
  cout<<endl;
 }
 return 0;
}
