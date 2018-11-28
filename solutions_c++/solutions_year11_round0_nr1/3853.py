#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string>
using namespace std;
struct Buton
{
	char robot;
	int buton;
};

FILE *g = fopen("output.out","w");
void timp(Buton *s,int n)
{
   int timpi[100];
   int ts=0;
   int cs=0;
   int blue=1,orange = 1;
   for (int i = 0; i<n ; i++)
   {
	   if (s[i].robot=='O')
	   {
		   timpi[i] = abs(s[i].buton - orange) +1;
		   orange = s[i].buton;
	   }
	   else
	   {
		   timpi[i] = abs(s[i].buton - blue) +1;
		   blue = s[i].buton;
	   }

   }
   //init
   ts = timpi[0];
   cs = timpi[0];
   for (int i = 1; i<n; i++) 
   {
	   if (s[i].robot == s[i-1].robot)
	      {
			  ts = ts + timpi[i];
			  cs = cs + timpi[i];
	      }
	   else if(timpi[i]<=cs)
	   {
		   ts = ts+1;
		   cs = 1;
	   }
	   else if (timpi[i] > cs)
	   {
		   ts = ts + timpi[i] - cs;
		   cs = timpi[i]-cs;
	   }
	  
   }
fprintf(g," %d\n",ts);


}
 void main()
{
	int n;
	Buton b[100];
	FILE *f=fopen("A-large.in","r");
	fscanf(f,"%d",&n);
	for (int i = 0; i<n; i++)
	{
	  int nr;
	  char a;
	  int aa;
	  fscanf(f,"%d",&nr);
	   for ( int j = 0; j<nr;j++)
		{
			fscanf(f,"%c",&a);
			fscanf(f,"%d",&aa);
			fscanf(f,"%c",&b[j].robot);
			fscanf(f,"%d",&b[j].buton);
	   }
	   fprintf(g,"Case #%d:",i+1);
	 timp(b,nr);
	}
	

}