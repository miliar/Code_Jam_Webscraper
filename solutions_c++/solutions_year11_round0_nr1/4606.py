#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>

int max(int a,int b)
{
 if(a>=b)
  {
   return a;
  }
 else
  return b;
}

void main()
{
clrscr();
ifstream in("C:\\tc\\cc");
ofstream out("C:\\tc\\bb.out");
if(!in)
{
cout<<"error";
}
 int b=1,o=1;
 char k;
 int i,j,l,l1,z,timeo,timeb;

 in>>l;
 for(z=1;z<=l;z++)
  {
   in>>l1;

   timeo=0;
   timeb=0;
   b=1;o=1;
    for(i=0;i<l1;i++)
     {
      in>>k>>j;
      if(k=='O')
       {

	timeo=timeo+abs(j-o)+1;
	o=j;
	 if(timeo<=timeb)
	  {
	   timeo=timeb+1;
	  }

       }
      else
       {
	timeb=timeb+abs(j-b)+1;
	b=j;
	  if(timeb<=timeo)
	  {
	   timeb=timeo+1;
	  }
       }
	 }
		if(!out)
		 {
		  cout<<"error";}
		  out<<"Case #"<<z<<": "<<max(timeo,timeb)<<"\n";
		  cout<<max(timeo,timeb)<<"\n";
     }


getch();
}