#include <conio.h>
#include <iostream.h>
#include <math.h>
#include<process.h>
#include<fstream.h>
#include<string.h>

void main()
{
 long a=0,b=0,mul,count=0;
 long ans=0;
 long k,i,tc=0;
 long tc2[5];
 char tc1[3],A[4],B[4];
 clrscr();
 ofstream fout("third.txt",ios::out);
 ifstream fin("input1.txt",ios::in);
 fin.get(tc1,3,'\n');

 for(int z=0;z<3;z++)
 {
	tc2[z]=tc1[z];
	tc2[z]=tc2[z]-48;
 }

 for(z=0;z<2;z++)
 {
	mul=pow(10,1-z);
	tc=tc+tc2[z]*mul;
 }


 for(int y=1;y<=50;y++)
 {
 a=0;
 b=0;
 ans=0;
 fin.get(A,5,' ');
 count=strlen(A);

 for(z=1;z<count;z++)
 {
	tc2[z]=A[z];
	tc2[z]=tc2[z]-48;

 }

 for(z=1;z<count;z++)
 {
	mul=pow(10,count-1-z);
	a=a+tc2[z]*mul;
 }

 fin.get(B,5,'\n');

 count=strlen(B);
 for(z=1;z<count;z++)
 {
	tc2[z]=B[z];
	tc2[z]=tc2[z]-48;
 }

 for(z=1;z<count;z++)
 {
	mul=pow(10,count-1-z);
	b=b+tc2[z]*mul;
 }

 if(b < 10 || a==b)
 {
  ans=0;
 }
 else
 {
 k=a;
 for(i=1;;i++)
 {
  k=k/10;
  if(k==0)
   break;
 }

 k=a;
 long l,m,n,p;
 p=pow(10,i-1);

 for(k=a;k<b;k++)
 {
  m=k;
  for(l=1;l<i;l++)
  {
   n=m%10;
   n=n*p;
   m=m/10;
   n=n+m;
   m=n;
   if(n<=b && n>k)
    ans++;
  }
 }
 }

 fout<<"\n\nCase #"<<y<<":" <<ans;

 getch();
}
getch();
}