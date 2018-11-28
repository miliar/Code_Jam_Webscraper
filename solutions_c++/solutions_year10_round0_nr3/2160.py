#include <fstream.h>
#include <iostream.h>
#include <stdlib.h>
#include <string>
#include <stdio.h>
#include <list>

fstream in,out;
using namespace std;
int num,x;



void clear(char *p,int size)
{for(int i=0;i<size;++i)
p[i]='\0';
}

int caculate(list<int> link,int r,int k,int n)
{int sum=0,last=k,go=n,g;
g=link.front();
for(int i=0;i<r;++i)
{while((g<=last)&&(go!=0))
{link.pop_front();
sum+=g;
last-=g;
link.push_back(g);
--go;
g=link.front();
}
last=k;
go=n;
}
return sum;
}






void main()
{in.open("C-small.in",ios::in);
out.open("my.out",ios::out);
char ch[50];
in.clear();
in.getline(ch,40);
num=atoi(ch);
x=1;
list<int> link;
char b1[100];
while(x<=num)
{int r,k,n;
clear(ch,50);
in.getline(ch,40);
r=atoi(strtok(ch," "));
k=atoi(strtok(NULL," "));
n=atoi(strtok(NULL," "));
clear(ch,50);
in.getline(ch,40);
int g=atoi(strtok(ch," "));
link.push_back(g);
for(int i=0;i<n-1;++i)
{g=atoi(strtok(NULL," "));
link.push_back(g);
}

int sum=caculate(link,r,k,n);

link.clear();

clear(b1,100);
itoa(x,b1,10);
out.write("Case #",6);
out.write(b1,strlen(b1));
out.write(": ",2);

clear(b1,100);
itoa(sum,b1,10);
out.write(b1,strlen(b1));
out.write("\n",1);


++x;
}
in.close();
out.close();
}