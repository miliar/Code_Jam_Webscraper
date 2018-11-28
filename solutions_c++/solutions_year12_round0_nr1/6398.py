#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{freopen("A-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
 char s[1000];
  int n,x;
  scanf("%d\n",&n);
 x=n;  
while(n--)
{
gets(s);
 for(int i=0;s[i]!='\0';i++)
 {
  if(s[i]=='y')
	s[i]='a';
  else if(s[i]=='n')
	s[i]='b';
  else if(s[i]=='f')
	s[i]='c';
  else if(s[i]=='i')
	s[i]='d';
  else if(s[i]=='c')
	s[i]='e';
  else if(s[i]=='w')
	s[i]='f';
  else if(s[i]=='l')
	s[i]='g';
  else if(s[i]=='b')
	s[i]='h';
   else if(s[i]=='k')
	s[i]='i';
  else if(s[i]=='u')
	s[i]='j';
  else if(s[i]=='o')
	s[i]='k';
  else if(s[i]=='m')
	s[i]='l';
  else if(s[i]=='x')
	s[i]='m';
  else if(s[i]=='s')
	s[i]='n';
  else if(s[i]=='e')
	s[i]='o';
  else if(s[i]=='v')
	s[i]='p';
 else if(s[i]=='z')
	s[i]='q';
else if(s[i]=='p')
	s[i]='r';
else if(s[i]=='d')
	s[i]='s';
else if(s[i]=='r')
	s[i]='t';
else if(s[i]=='j')
	s[i]='u';
else if(s[i]=='g')
	s[i]='v';
else if(s[i]=='t')
	s[i]='w';
else if(s[i]=='h')
	s[i]='x';
else if(s[i]=='a')
	s[i]='y';
else if(s[i]=='q')
	s[i]='z';
}
cout<<"Case #"<<(x-n)<<": "<<s<<"\n";
}
return 1;
}
