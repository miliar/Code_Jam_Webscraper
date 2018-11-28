#include<iostream.h>
#include<string.h>
#include<fstream.h>
fstream f("date.in", ios::in);
fstream g("date.out", ios::out);
int main()
{int n,i,j;
char a[100];
f>>n;
f.getline(a,100);

for(i=1;i<=n;i++)
{f.get(a,100);
//g<<strlen(a)<<"\n";


for(j=0;j<=strlen(a)-1;j++)
   switch(a[j])
     { case 'y': a[j]='a'; 	break;
       case 'n': a[j]='b';      break;
       case 'f': a[j]='c';      break;
       case 'i': a[j]='d';      break;
       case 'c': a[j]='e';      break;
       case 'w': a[j]='f';      break;
       case 'l': a[j]='g';      break;
       case 'b': a[j]='h';      break;
       case 'k': a[j]='i';      break;
       case 'u': a[j]='j';      break;
       case 'o': a[j]='k';      break;
       case 'm': a[j]='l';      break;
       case 'x': a[j]='m';      break;
       case 's': a[j]='n';      break;
       case 'e': a[j]='o';      break;
       case 'v': a[j]='p';      break;
       case 'z': a[j]='q';      break;
       case 'p': a[j]='r';      break;
       case 'd': a[j]='s';      break;
       case 'r': a[j]='t';      break;
       case 'j': a[j]='u';      break;
       case 'g': a[j]='v';      break;
       case 't': a[j]='w';      break;
       case 'h': a[j]='x';      break;
       case 'a': a[j]='y';      break;
       case 'q': a[j]='z';      break;
       default: break;  }

g<<a<<"\n";     
f.getline(a,100);

}
 f.close();
 g.close();
  return 0;
  }