#include <fstream.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <iostream.h>

int num,n;
fstream in,out;


void clear(char *p,int size)
{for(int i=0;i<size;++i)
p[i]='\0';
}

__int64 mina(__int64 a,__int64 b)
{return a<=b?a:b;
}


__int64 gys(__int64 m,__int64 n)
{__int64 temp,r;
if (m<n)
 {
  temp=m,m=n,n=temp;
 }
  while(n)
 {
  r=m%n,m=n,n=r;
 }
return m;
}



__int64 caculate(__int64 a[],int count,__int64 sub[])
{__int64 temp;
__int64 min;
if(count==2)
{temp=sub[0];
min=mina(a[0],a[1]);
printf("%I64u %I64u\n",temp,min);

if(min%temp==0) return 0;
else
return (temp-min%temp);
}
if(count==3)
{min=mina(a[0],a[1]);
min=mina(min,a[2]);
temp=gys(sub[0],sub[1]);
temp=gys(temp,sub[2]);
printf("%I64u %I64u\n",temp,min);
if(min%temp==0)  return 0;
else
return (temp-min%temp);
}

return 0;
}

__int64 abs64(__int64 a)
{if(a<0) return -a;
else
return a;
}

void main()
{in.open("B-small.in",ios::in);
//in.open("test.in",ios::in);
out.open("my.out",ios::out);
char ch[200];
in.clear();
in.getline(ch,200);
num=atoi(ch);
n=1;
while(n<=num)
{__int64 a[3],sub[3];
int count;
clear(ch,200);
in.getline(ch,200);
count=atoi(strtok(ch," "));
for(int i=0;i<count;++i)
{a[i]=_atoi64(strtok(NULL," "));
}

if(count==2) sub[0]=abs64(a[1]-a[0]);
else
{sub[0]=abs64(a[1]-a[0]);
sub[1]=abs64(a[2]-a[1]);
sub[2]=abs64(a[2]-a[0]);
}

__int64 result=caculate(a,count,sub);
char b1[20];
clear(b1,20);
itoa(n,b1,10);
out.write("Case #",6);
out.write(b1,strlen(b1));
clear(b1,20);
_i64toa(result,b1,10);
out.write(": ",2);
out.write(b1,strlen(b1));
out.write("\n",1);

//__int64 result=caculate(a,count,sub);

//printf("%I64d ",result);
//printf("\n");



++n;


}




in.close();
out.close();
}