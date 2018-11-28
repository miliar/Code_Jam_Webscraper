#include<cstdio>
#include<string>
#include<vector>
#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

void tofind(char x);


int main()
{
ofstream f2;
f2.open("Codejam_Out_A.txt");
string str;
int n=0,g=1;

scanf("%d\n",&n);

for(int i=0;i<n;i++)
{
        string p;
       getline(cin,p);
for(int j=0;j<p.length();j++)
{

if(p[j]==' ')
continue;

if(p[j]=='y')
p[j]='a';

else if(p[j]=='a')
p[j]='y';

else if(p[j]=='b')
p[j]='h';
else if(p[j]=='c')
p[j]='e';
else if(p[j]=='d')
p[j]='s';
else if(p[j]=='e')
p[j]='o';
else if(p[j]=='f')
p[j]='c';
else if(p[j]=='g')
p[j]='v';
else if(p[j]=='h')
p[j]='x';
else if(p[j]=='i')
p[j]='d';
else if(p[j]=='j')
p[j]='u';
else if(p[j]=='k')
p[j]='i';
else if(p[j]=='l')
p[j]='g';
else if(p[j]=='m')
p[j]='l';
else if(p[j]=='n')
p[j]='b';
else if(p[j]=='o')
p[j]='k';
else if(p[j]=='p')
p[j]='r';
else if(p[j]=='q')
p[j]='z';
else if(p[j]=='r')
p[j]='t';
else if(p[j]=='s')
p[j]='n';
else if(p[j]=='t')
p[j]='w';
else if(p[j]=='u')
p[j]='j';
else if(p[j]=='v')
p[j]='p';
else if(p[j]=='w')
p[j]='f';
else if(p[j]=='x')
p[j]='m';
else if(p[j]=='z')
p[j]='q';
}


f2<<"Case #"<<i+1<<": ";
f2<<p;
if(i!=(n-1))
f2<<endl;


}
f2.close();
return 0;
}
