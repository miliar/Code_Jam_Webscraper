#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<fstream.h>
int compare(char a[3],char b[15])
{
int i,j=0,flag=0;
for(i=0;i<strlen(a);i++)
{  flag=0;
 while(j<strlen(b))
  {
     if(b[j]==a[i])
      {
       flag=1;
       j++;
      }
     else if(b[j]=='(')
      {
       j=j+1;
	while(b[j]!=')')
	 {
	  if(b[j]==a[i])
	   {
	    flag=1;
	    j++;
	   }
	  else
	   {j++;}

	 } j++;
      }
	if(flag==0)
	 {
	  return 0;
	 }

   break;
  }
}
  return 1;
}

void main()
{
char p[2000][15],q[2000][15],r[1000][15];
char z[15];
int i,k,l,d,n;
clrscr();
ifstream in("cc");//changed the name of the input file to cc
ofstream out("bb.out");
if(!in)
{
cout<<"error";
}
in>>l>>d>>n;
for(i=0;i<d;i++)
{
if(i%3==0)
{
 in>>p[i/3];
}
if(i%3==1)
{
in>>q[(i/3)];
}
if(i%3==2)
{
in>>r[(i/3)];
}
}
for(i=0;i<n;i++)
{
int j=0,found=0;
in>>z;
for(int k=0;k<d;k++)
{
found=0;
if(k%3==0)
{
p[k][strlen(p[k])]='\0';
found=compare(p[k],z);
}
if(k%3==1)
{
q[(k/3)][strlen(q[(k/3)])]='\0';
found=compare(q[(k/3)],z);
}
if(k%3==2)
{
r[(k/3)][strlen(r[(k/3)])]='\0';
found=compare(r[(k/3)],z);
}
if(found==1){
j++;}
 }
out<<"Case #"<<i+1<<": "<<j<<"\n";
}
}