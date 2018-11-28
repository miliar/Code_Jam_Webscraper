#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<string.h>
#include<stdlib.h>


struct d
{
int c,r,t;
}x[10];

void sort(char s[10][100],int sc,char q[100][100],int qc)
{
int i,j,t;
char c[100];

for(i=0;i<sc;i++)
{
strcpy(c,s[i]);
x[i].c=qc;
x[i].r=qc;

for(j=0;j<qc;j++)
{
if(strcmp(c,q[j])==0)
x[i].c--;
if(x[i].c==qc-1)
x[i].r=j;
}
}

for(i=0;i<sc;i++)
{
cout<<x[i].c<<" "<<x[i].r<<"\n";
x[i].t=x[i].r+x[i].c;
}

for(i=0;i<sc;i++)
{
for(j=0;j<sc-1;j++)
{
if(x[j].t<x[j+1].t)
{
t=x[j].t;
x[j].t=x[j+1].t;
x[j+1].t=t;
strcpy(c,s[j]);
strcpy(s[j],s[j+1]);
strcpy(s[j+1],c);
}

}
}

for(i=0;i<sc;i++)
cout<<s[i]<<"\n";
getch();

}

int find(char s[10][100],int sc,char q[100][100],int qc)
{
int i,t,j=0,k,c=0;

char g[10][100];
char z[100];

for(i=0;i<qc;i++)
{
for(k=0;k<j;k++)
if(strcmp(q[i],g[k])==0)
break;

if(k==j)
strcpy(g[j++],q[i]);
}

strcpy(z,g[j-1]);

if(j!=sc)
{
for(k=0;k<sc;k++)
{
for(i=0;i<j;i++)
if(strcmp(s[k],g[i])==0)
break;
if(i==j)
strcpy(z,s[k]);
}
}

for(t=0;t<qc;t++)
{
//cout<<z<<"\n";
//getch();
if(strcmp(z,q[t])==0)
{
c++;
j=0;
for(i=t;i<qc;i++)
{
for(k=0;k<j;k++)
if(strcmp(q[i],g[k])==0)
break;

if(k==j)
strcpy(g[j++],q[i]);
}

strcpy(z,g[j-1]);

if(j!=sc)
{
for(k=0;k<sc;k++)
{
for(i=0;i<j;i++)
if(strcmp(s[k],g[i])==0)
break;
if(i==j)
strcpy(z,s[k]);
}
}



}
}

return c;
}


void main()
{

char c[50];
//char t[500][100];
int i=0;
fstream f,ot;
f.open("1.txt",ios::in);
ot.open("out.txt",ios::out);


int sc,qc,j;
char s[10][100];
char q[100][100];

clrscr();

f.getline(c,50,'\n');
//strcpy(t[i++],c);
int k=atoi(c);

for(i=0;i<k;i++)
{

f.getline(c,50,'\n');
sc=atoi(c);
for(j=0;j<sc;j++)
{
f.getline(c,50,'\n');
strcpy(s[j],c);
}

f.getline(c,50,'\n');
qc=atoi(c);
//cout<<qc;
for(j=0;j<qc;j++)
{
f.getline(c,50,'\n');
strcpy(q[j],c);
//cout<<q[j]<<"\n";
//getch();
}

//sort(s,sc,q,qc);
cout<<"Case #"<<i+1<<": "<<find(s,sc,q,qc)<<"\n";
//ot<<"Case #"<<i+1<<": "<<find(s,sc,q,qc)<<"\n";

}

ot.close();
f.close();
getch();
}