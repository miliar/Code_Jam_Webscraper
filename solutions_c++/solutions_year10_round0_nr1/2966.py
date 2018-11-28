# include<fstream.h>
# include <conio.h>
# include <string.h>
# include <stdio.h>
long a[1000];
void main()
{
  clrscr();
  ifstream infile("in2.in",ios::in);
  ofstream outfile("zl31.out",ios::out);
 unsigned long t,k,n,w;
  infile >> t;
  long c,c1;

 for( long  q=1;q<=1;q++)//1==n
  {
   infile >>k;
   infile >>n;
   a[1]=0;
   c1=1;
   int pos;
   for(unsigned long i=2;i<=k;i++)
   {
       a[i]=-1;
   }
   for( i=1;i<=n;i++)
   {
     cout <<"value of a"<<i<<endl;
     //c1=1;
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

	long c=0;
       //	cout <<"value of c"<<c<<endl;
	for(j=1;j<=k;j++)
	 {
	  if(a[j] ==1)
	  { ++c;
	   }
	  }
	  if(c ==c1&&c1<k&&a[c+1] ==-1)
	  {  a[c+1]=0;
	     c1++;
	  }
	long   c3=0;
	   for( j=1;j<=k;j++)
    {
     if( a[j]==1 )
       c3++;
     }
     if(c3==k)
     {
     pos=i+1;
   //  cout <<"value of k"<<i<<endl;
     break;
     }


   }
  // outfile<<"Case #"<<q<<": ON"<<"\n";
  long t=  n%pos;
   cout<<"\nValue of t"<<t;
   if(t==pos-1)
    outfile<<"Case #"<<q<<": ON"<<"\n";
    else
  outfile<<"Case #"<<q<<": OFF"<<"\n";


  }
  getch();
  }
