#include <iostream.h>
#include <fstream.h>
#include <stdlib.h>
#include <string.h>

int num,n;
fstream in,out;

void clear(char *p,int size)
{for(int i=0;i<size;++i)
p[i]='\0';
}

int find(char *p)
{for(int i=0;i<40;++i)
if(p[i]==' ') return i;
return -1;
}

int getnumber(char *p,int beg,int end)
{char temp[40];
clear(temp,40);
for(int i=beg;i<end;++i)
{if(p[i]=='\0') break;
temp[i-beg]=p[i];
}
return atoi(temp);
}

bool test(int a,int b)
{int power=1<<a;
if((power-1)>b) return false;
if((power-1)==b) return true;
if((power-1)<b)
{int mod=b%power;
if(mod==(power-1)) return true;
else 
return false;
}
}



void main()
{in.open("A-large.in",ios::in);
out.open("my.out",ios::out);
char ch[50];
in.clear();
in.getline(ch,40);
num=atoi(ch);
n=1;
int a,b,k;
char b1[10];
while(n<=num){
clear(b1,10);
clear(ch,50);
itoa(n,b1,10);
in.getline(ch,40);
k=find(ch);
a=getnumber(ch,0,k);
b=getnumber(ch,k+1,40);
bool result=test(a,b);
out.write("Case #",6);
out.write(b1,strlen(b1));
out.write(": ",2);
if(result) {out.write("ON\n",3);
}
else
out.write("OFF\n",4);
++n;
}

in.close();
out.close();

}
