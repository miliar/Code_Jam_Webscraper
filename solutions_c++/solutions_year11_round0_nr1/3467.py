#include<iostream.h>
#include<fstream.h>
//#include<conio.h>
//#include<ctype.h>

int test_case, *no_but, i, j, **but, time, timeo ,timeb, cur_poso, cur_posb;
char **a;
void ino(int , int);
void inb(int, int);

void main()
{

   ifstream inf("input.in");
   ofstream opf("one.o");

   inf>>test_case;
   no_but = new int [test_case];
  // but = new * int [test_case];
//   a=new * char [test_case];
	a= new char * [test_case];
   but= new int * [test_case];



   for(i=0 ; i<test_case ; i++)
   {
   	inf>>no_but[i];
      but[i] = new int [no_but[i]];
      a[i]= new char [no_but[i]];
      for(j= 0 ; j<no_but[i] ; j++)
      {
      	inf>>a[i][j]>>but[i][j];
      }
   }

   for(i=0 ; i<test_case ; i++)
   {
   	opf<<"Case #"<<(i+1)<<": ";
      cur_poso= 1;
      cur_posb=1;
      time=0;
      timeo=0;
      timeb=0;
      for(j=0 ; j<no_but[i] ; j++)
      {
      	if(a[i][j]=='O')
         	ino(i,j );
         else
         	inb(i,j);
      }
      opf<<time<<endl;
   }

   for(i=0 ; i<test_case ; i++)
   {
   	delete[] but[i];
      delete[] a[i];
   }
   delete [] but;
   delete [] a;
   delete [] no_but;
}

void ino(int i, int j)
{
int x=1;
do
{
	if(but[i][j]<cur_poso)
   {
   	cur_poso--;
      if(timeo>0)
      	timeo--;
      else
      {
      	time++;
         timeb++;

      }
   }
   else if(but[i][j]>cur_poso)
   {
   	 cur_poso++;
      if(timeo>0)
      	timeo--;
      else
      {
      	time++;
         timeb++;

      }
   }
   else
   {
   	time++;
      timeo=0;
      timeb++;
      x=0;
   }
}while(x);
}

void inb(int i, int j)
{
int x=1;
do
{
	if(but[i][j]<cur_posb)
   {
   	cur_posb--;
      if(timeb>0)
      	timeb--;
      else
      {
      	time++;
         timeo++;

      }
   }
   else if(but[i][j]>cur_posb)
   {
   	cur_posb++;
      if(timeb>0)
      	timeb--;
      else
      {
      	time++;
         timeo++;
      
      }
   }
   else
   {
   	time++;
      timeb=0;
      timeo++;
      x=0;
   }
}while(x);
}
