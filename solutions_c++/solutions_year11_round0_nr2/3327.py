#include<iostream>
#include<string.h>
#include<fstream>
#include<stdio.h>
using namespace std;
struct gam
{
int c3,c2,n;
char *a,*b;
char *c;
}*cases;
bool hel(char e,char f,int k)
{
int l=0;
for(int i=0;i<cases[k].c2;i++)
{
if(cases[k].b[l]==e||cases[k].b[l]==f)
{
if(cases[k].b[l]==e)
{
if(cases[k].b[l+1]==f)
return(true);
}
else if(cases[k].b[l]==f)
{
if(cases[k].b[l+1]==e)
return(true);
}
}
l+=2;
}
}
char combin(char e,char f,int k)
{
int l=0;
for(int i=0;i<cases[k].c3;i++)
{
if(cases[k].a[l]==e||cases[k].a[l]==f)
{
if(cases[k].a[l]==e)
{
if(cases[k].a[l+1]==f)
return(cases[k].a[l+2]);
}
else if(cases[k].a[l]==f)
{
if(cases[k].a[l+1]==e)
return(cases[k].a[l+2]);
}
}
l+=3;
}
return '#';
}
bool oppos(char *d,int k,int l)
{
for(int i=0;i<l+1;i++)
{
if(hel(d[l],d[i],k))
return true;
}
return false;
}


int num;
int main()
{
char dum[4],dum1[3];
ifstream f;
ofstream f2;
f2.open("/home/tarun/Desktop/tarun.out");
f.open("/home/tarun/Desktop/tarun.in");
f>>num;
cases=new gam[num];
for(int i=0;i<num;i++)
{
f>>cases[i].c3;
cases[i].a=new char[cases[i].c3*3];
for(int k=0;k<cases[i].c3;k++)
{
f>>dum;
strcat(cases[i].a,dum);
}
f>>cases[i].c2;
cases[i].b=new char[cases[i].c2*2];
for(int l=0;l<cases[i].c2;l++)
{
f>>dum1;
strcat(cases[i].b,dum1);
}
f>>cases[i].n;
cases[i].c=new char[cases[i].n+1];
f>>cases[i].c;
}
//cout<<cases[3].b;
char *d;
int l;
char e;
for(int i=0;i<num;i++)
{
l=0;
d=new char[cases[i].n];
for(int m=0;m<cases[i].n;m++)
{
d[l]=cases[i].c[m];
l++;
if(l>1)
{

if(cases[i].c3>0){if(combin(d[l-1],d[l-2],i)!='#')
{
e=combin(d[l-1],d[l-2],i);
l--;
d[l-1]=e;
d[l]='0';
l++;
}}
if(cases[i].c2>0){ if(oppos(d,i,l-1))
{
for(int h=0;h<l;h++)
d[l]='0';
l=0;
}}
}
}
cout<<d<<" "<<l<<endl;
f2<<"Case #"<<i+1<<": "<<'[';
for(int q=0;q<l;q++)
{if(d[q]!='0')
{
f2<<d[q]; 
if((d[q+1]=='0' && q+2==l)||q+1==l);
else 
{f2<<", ";}
}
}


f2<<']'<<endl;
}
}
