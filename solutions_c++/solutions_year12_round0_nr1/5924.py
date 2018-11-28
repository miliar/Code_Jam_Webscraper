#include<iostream.h>
#include<string.h>
#include<stdio.h>
#include<conio.h>
#include<fstream.h>
void main()
{char A[200];
char ch[5];
int N=0;
int i,j,m,p,q,r,t;
ifstream fin;
ofstream fout;
fin.open("A-small-attempt0.in");
fout.open("out.txt");
fin.getline(ch,5);
int s=strlen(ch);
for(i=0;i<s;i++)
N=N*10+(ch[i]-48);
cout<<N<<endl;
for(i=0;i<N;i++)
{fin.getline(A,200);
m=strlen(A);
j=0;
while(j<m)
{if(A[j]=='a')
A[j]='y';
else if(A[j]=='b')
A[j]='h';
else if(A[j]=='c')
A[j]='e';
else if(A[j]=='d')
A[j]='s';
else if(A[j]=='e')
A[j]='o';
else if(A[j]=='f')
A[j]='c';
else if(A[j]=='g')
A[j]='v';
else if(A[j]=='h')
A[j]='x';
else if(A[j]=='i')
A[j]='d';
else if(A[j]=='j')
A[j]='u';
else if(A[j]=='k')
A[j]='i';
else if(A[j]=='l')
A[j]='g';
else if(A[j]=='m')
A[j]='l';
else if(A[j]=='n')
A[j]='b';
else if(A[j]=='o')
A[j]='k';
else if(A[j]=='p')
A[j]='r';
else if(A[j]=='q')
A[j]='z';
else if(A[j]=='r')
A[j]='t';
else if(A[j]=='s')
A[j]='n';
else if(A[j]=='t')
A[j]='w';
else if(A[j]=='u')
A[j]='j';
else if(A[j]=='v')
A[j]='p';
else if(A[j]=='w')
A[j]='f';
else if(A[j]=='x')
A[j]='m';
else if(A[j]=='y')
A[j]='a';
else if(A[j]=='z')
A[j]='q';
j++;}
fout<<"Case #"<<i+1<<": ";
for(j=0;j<m;j++)
fout<<A[j];
fout<<endl;}
fin.close();
fout.close();
}