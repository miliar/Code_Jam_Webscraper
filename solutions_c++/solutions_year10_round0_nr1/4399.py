#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
clrscr();
ifstream in("cc");
ofstream out("bb.out");
if(!in)
{
cout<<"error";
}
unsigned long int d;
int z,sw,sn,l,k,flag;
in>>l;
 for(k=1;k<=l;k++)
  {
   in>>sw>>sn;
   d=pow(2,sw)-1;
    if(sn>sw)
     {
      z=(sn-d);
      d=pow(2,sw-1);
      z=z%d;
      if(z==0)
      {
       flag=1;
      }
      else
       flag=0;
     }
    else
     {
      flag=0;
       if(sn<=sw && sn!=0)
	{
	 if(d==sn)
	  {
	    flag=1;
	  }
	}
     }
      if(!out)
       {
	cout<<"error";
       }
out<<"Case #"<<z<<": "<<p<<"\n";
cout<<"\n";
}

    if(flag==1)
    {
    cout<<"ON\n";
    out<<"Case #"<<z<<": "<<"ON\n";
    }
    else
    cout<<"OFF\n";
    out<<"Case #"<<z<<": "<<"OFF\n";
   }
getch();
}
