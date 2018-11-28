# include<fstream.h>
# include <conio.h>
# include <string.h>
# include <stdio.h>
long a[1000];
void main()
{
  clrscr();
  ifstream infile("in2.in",ios::in);
  ofstream outfile("zl2.out",ios::out);
  long t,k,n,w;
  infile >> t;
  long c,c1=1;

 for( unsigned long q=1;q<=t;q++)//1==n
  {
   infile >>n;
   infile >>k;
   a[1]=0;
   for( long i=2;i<=k;i++)
   {
       a[i]=-1;
   }
   for( i=1;i<=n;i++)
   {
     for( long j=1;j<=k;j++)
       { if(a[j] == 1)
	  a[j]=0;
	 else
	   if(a[j] == 0)
	    {
	      a[j]=1;
	      break;
	    }
	}
	int c=0;
	for(j=1;j<=n;j++)
	 {
	  if(a[j] ==1)
	   c++;
	  }
	  if(c ==c1&&c1<k)
	  {  a[c+1]=0;
	     c1++;
	  }
    // c=0;

   }
       c=0;
      for(long j=1;j<=k;j++)
    {
     if( a[j]==1 )
       c++;
     }
   if(c==k)
     outfile<<"Case #"<<q<<": ON"<<"\n";
   else
    outfile<<"Case #"<<q<<": OFF"<<"\n";

  }
  getch();
  }
