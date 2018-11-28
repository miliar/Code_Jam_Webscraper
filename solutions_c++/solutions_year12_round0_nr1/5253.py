#include<iostream>
#include<stdlib.h>
#include<cstdio>

using namespace std;

class Googlerese
{
public:
char G[150];
void input();
void output();
void english(char &);
};

void Googlerese::input()
{
gets(G);
}

void Googlerese::output()
{
int i=0;
while(G[i]!='\0')
english(G[i++]);
puts(G);
}

void Googlerese::english(char &ch)
{
switch(ch)
{
case 'a':ch='y';break;
case 'b':ch='h';break;
case 'c':ch='e';break;
case 'd':ch='s';break;
case 'e':ch='o';break;
case 'f':ch='c';break;
case 'g':ch='v';break;
case 'h':ch='x';break;
case 'i':ch='d';break;
case 'j':ch='u';break;
case 'k':ch='i';break;
case 'l':ch='g';break;
case 'm':ch='l';break;
case 'n':ch='b';break;
case 'o':ch='k';break;
case 'p':ch='r';break;
case 'q':ch='z';break;
case 'r':ch='t';break;
case 's':ch='n';break;
case 't':ch='w';break;
case 'u':ch='j';break;
case 'v':ch='p';break;
case 'w':ch='f';break;
case 'x':ch='m';break;
case 'y':ch='a';break;
case 'z':ch='q';break;
case ' ':ch=' ';break;
}
}


int main()
{
Googlerese g[50];
int n;
cin>>n;
char ch=getchar();
if(ch=='\n')
{
for(int i=0;i<n;i++)
g[i].input();
for(int i=0;i<n;i++)
{
cout<<"Case #"<<(i+1)<<": ";
g[i].output();
}
}
return 0;
}
