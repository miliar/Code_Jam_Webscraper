#include<iostream.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	long int i, j, tc, *pd, *pg, *n,z;
   int pos1=0;
   long double x ;

	ifstream inf("input.in");
   ofstream opf("one.o");

   inf>>tc;
   pd = new long int[tc];
   pg = new long int[tc];
   n = new long int[tc];

   for(i=0 ; i<tc ; i++)
   {
   	cout<<"Case #"<<(i+1)<<": ";
   	inf>>n[i]>>pd[i]>>pg[i];
      cout<<n[i]<<endl<<pd[i]<<endl<<pg[i];
      for(j=n[i] ; j>0 ; j--)
      {
//     	x=(j*((float(pd[i]))/100))-(long int(j*((float(pd[i]))/100)));
			x=((long double)(pd[i])/100)*j;
         x= x-(long int)(x);
         z=1000000000 * x;
      	if(z==0)
         	pos1=1;
      }
      opf<<"Case #"<<(i+1)<<": ";
      if(pos1)
      {
      	if((pg[i]==0&&pd[i]==0)||((pg[i]<100&&pg[i]>0)||(pg[i]==100&&pd[i]==100)))

           	opf<<"Possible";

         else
           	opf<<"Broken";

      }
      else
        	opf<<"Broken";

   	opf<<endl;
      pos1=0;
   }

   delete [] pd;
   delete [] pg;
   delete [] n;
   getch();
}
