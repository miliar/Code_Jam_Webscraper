#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

int main()
{
char ch;
int T;
int i=0;
string a;
cin>>T;
ch=getchar();
for(int tt=0;tt<T;tt++)
{


i=0;
getline(cin,a,'\n');


int templen=a.size();

for(i=0;i<templen;i++)
{
switch(a[i])
{
case 'a':
a[i]='y';
break;
case 'n':
a[i]='b';
	break;
case 'f':
	a[i]='c';
	break;
case 'i':
	a[i]='d';
break;
case 'c':
	a[i]='e';
break;
case 'w':
	a[i]='f';
break;
case 'l':
	a[i]='g';
break;
case 'b':
	a[i]='h';
	break;
case 'k':
	a[i]='i';
break;
case 'u':
	a[i]='j';
break;
case 'o':
	a[i]='k';
break;
case 'm':
	a[i]='l';
	break;
case 'x':
	a[i]='m';
break;
case 's':
	a[i]='n';
break;
case 'e':
	a[i]='o';
break;
case 'v':
	a[i]='p';
break;	
case 'z':
	a[i]='q';
break;
case 'p':
	a[i]='r';

	break;
case 'd':
	a[i]='s';

break;
case 'r':
	a[i]='t';
break;
case 'j':
a[i]='u';
break;
case 'g':
a[i]='v';
break;
case 't':
a[i]='w';
break;
case 'h':
	a[i]='x';
break;
case 'y':
a[i]='a';
break;
case 'q':
a[i]='z';
break;
}
}

cout<<"Case #";
cout<<tt+1;
cout<<": ";
cout<<a;
cout<<endl;
}
return 0;
}