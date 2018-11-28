#include<cstdio>
#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string s;
char ch[110];
int t,a;
int main()
{fstream x,y;
x.open("ud.txt");
   x>>t;
    //scanf("%d",&t);
   y.open("ans.txt");
    a=t;
x.getline(ch,110);
while(t--)
{

//a-t case
x.getline(ch,110);

//x.getline(ch,80);
//cin.getline(ch,80);
int i=0;
while(ch[i]!='\0')
{
switch(ch[i])
{case 'a':
ch[i]='y';
break;
case 'b':
ch[i]='h';
break;
case 'c':
ch[i]='e';
break;
case 'd':
ch[i]='s';
break;
case 'e':
ch[i]='o';
break;
case 'f':
ch[i]='c';
break;
case 'g':
ch[i]='v';
break;
case 'h':
ch[i]='x';
break;
case 'i':
ch[i]='d';
break;
case 'j':
ch[i]='u';
break;
case 'k':
ch[i]='i';
break;
case 'l':
ch[i]='g';
break;
case 'm':
ch[i]='l';
break;
case 'n':
ch[i]='b';
break;
case 'o':
ch[i]='k';
break;
case 'p':
ch[i]='r';
break;
case 'q':
ch[i]='z';//not sure
break;
case 'r':
ch[i]='t';
break;
case 's':
ch[i]='n';
break;
case 't':
ch[i]='w';
break;
case 'u':
ch[i]='j';
break;
case 'v':
ch[i]='p';
break;
case 'w':
ch[i]='f';
break;
case 'x':
ch[i]='m';
break;
case 'y':
ch[i]='a';
break;
case 'z':
ch[i]='q';
break;
default :
break;
}
i++;
}

y<<"Case #"<<a-t<<": "<<ch<<"\n";
//printf("Case #%d: %s\n",a-t,ch);

}
return 0;
}
