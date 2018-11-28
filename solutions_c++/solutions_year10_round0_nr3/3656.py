#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
clrscr();
ifstream in("cc");
ofstream out("dd.out");
if(!in)
{
cout<<"error";
}
unsigned long int ro,cap,cost,tc,p[1000];
int z,sw,sn,l,k,fg,nug,n,tp;
in>>l;
 for(k=1;k<=l;k++)
  {tp=0;
   in>>ro>>cap>>nug;
    for(int a=0;a<nug;a++)
     {
      in>>p[a];
      tp=tp+p[a];
     }
     n=0;fg=0,cost=0,tc=0;
    if(tp>cap)
    {
      while(n<ro)
       { cost=0;
	 while(cost<=cap)
	  {
	    if(fg>=nug)
	     {
	       fg=0;
	     }
	    cost=cost+p[fg];
	    if(cost>cap)
	     {
	      cost=cost-p[fg];
	      tc=tc+cost;
	      n++;
	      break;
	     }
	    fg++;
	  }
       }
    }
    else
   { tc=tp*ro;}
     cout<<tc<<"\n";
   out<<"Case #"<<k<<": "<<tc<<"\n";

   }
getch();
}
