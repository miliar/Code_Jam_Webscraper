#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
using namespace std;

int main()
{
freopen("aho.txt","w",stdout);
string yo;
ifstream that ("A-small-attempt1.in");
int a,b,c,d,size;
a=b=c=d=size=0;


getline(that,yo);

char *string1=(char*)yo.c_str();



size=atoi(string1);


for(b=0;b<size;b++)
{
getline(that,yo);
char *string=(char*)yo.c_str();

for(c=0;c<100;c++)
{

if(string[c]=='\n')
{
break;
}
else
{

switch(string[c])
{

case 'a': string[c]='y';
break;

case 'b': string[c]='h';
break;

case 'c': string[c]='e';
break;

case 'd': string[c]='s';
break;

case 'e': string[c]='o';
break;

case 'f': string[c]='c';
break;

case 'g': string[c]='v';
break;

case 'h': string[c]='x';
break;

case 'i': string[c]='d';
break;

case 'j': string[c]='u';
break;

case 'k': string[c]='i';
break;

case 'l': string[c]='g';
break;

case 'm': string[c]='l';
break;

case 'n': string[c]='b';
break;

case 'o': string[c]='k';
break;

case 'p': string[c]='r';
break;

case 'q': string[c]='z';
break;

case 'r': string[c]='t';
break;

case 's': string[c]='n';
break;

case 't': string[c]='w';
break;

case 'u': string[c]='j';
break;

case 'v': string[c]='p';
break;

case 'w': string[c]='f';
break;

case 'x': string[c]='m';
break;

case 'y': string[c]='a';
break;

case 'z': string[c]='q';
break;

default:
break;

}


}

}
cout<<"Case #"<<(b+1)<<":"<<" "<<string<<'\n';



}





return 0;
}
