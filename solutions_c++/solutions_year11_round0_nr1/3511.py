#include<fstream>
#include<iostream>
//#include<cmath>
int abs(int n)
{
if(n<0)
return -n;
else return n;
}
using namespace std;
int o,b;
int main()
{
int t1=0,t2;
o=1,b=1;
char r,s;
int m;
int t=0;
ofstream f5;
f5.open("/home/tarun/Desktop/tarun.out");
ifstream f;
f.open("/home/tarun/Desktop/tarun.in");
int n;
f>>n;
int n1;
int f1;
for(int i=0;i<n;i++)
{
t=0,o=1,b=1,t1=0;
f>>n1;
//f>>s;
int f2=0,f1=0;
for(int k=0;k<n1;k++)
{
f>>r;
//f>>s;
f>>m;
//f>>s;
if(f2==0)
{
f2=1;
if(r=='O')
f1=0;
else
f1=1;
}

if(r=='O')
{

if(f1==0)
{

t1+=abs(m-o);
t1++;
t+=abs(m-o)+1;

//b+=t1;
o=m;
//t1=0;
}
else 
{
if(t1>=abs(m-o))
{
t1=0;
o=m;
t1++;
t+=t1;
f1=0;
}
else
{
 t2=abs(m-o);
t2-=t1;
t+=t2;
o=m;
t1=t2;
t++;
t1++;
f1=0;
}

}
}
else if(r=='B')
{
if(f1==1)
{
t1+=abs(m-b);
t+=abs(m-b);
b=m;

t++,t1++;
}
else
{
if(t1>=abs(m-b))
{
b=m;
t1=1;
t++;
f1=1;
}
else
{
t2=abs(m-b);
t2-=t1;
t+=t2;
b=m;
t++;
t1=t2+1;
f1=1;
}
}
}
}

f5<<"Case #"<<i+1<<": "<<t<<endl;
}
}
