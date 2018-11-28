#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
bool isarea(int x1,int y11,int x2,int y2,int x3,int y3,double A);
double distance(int x1,int y11,int x2,int y2);

FILE *testfile;
char filename[100];

int main(int argc,char*argv[])
{
int A,N,M;
int x1,x2,x3,y11,y2,y3;
int numtestcases;
bool found;
 
  strcpy(filename,argv[1]);
  testfile=fopen(filename,"r");
  fscanf(testfile,"%d",&numtestcases);
  //cout << isarea(0,0,0,1,1,1,32) << endl;
  for(int i=1;i<=numtestcases;i++)
    {
      fscanf(testfile,"%d",&N);
      fscanf(testfile,"%d",&M);
      fscanf(testfile,"%d",&A);
      //printf("%d %d %d\n",A,N,M);
      x1=0;
      found=0;
      while(x1<=0 && !found)
	{
	  y11=0;
	  //cout << x1 << endl;
	  while(y11<=0 && !found)
	    {
	      x2=0;
	      //cout << y11 << endl;
	      while(x2<=N && !found)
		{
		  y2=0;
		  while(y2<=M && !found)
		    {
		      x3=0;
		      while(x3<=N && !found)
			{
			  y3=0;
			  //cout << x3 << endl;
			  while(y3<=M && !found)
			    {
			      if(isarea(x1,y11,x2,y2,x3,y3,0.5*(double)A)==1)
				{
				  //ut << isarea(0,0,0,1,1,0,32)            << endl;
				  //ut << A << endl;

				  printf("Case #%d: %d %d %d %d %d %d \n",i,x1,y11,x2,y2,x3,y3);
				  found=1;
				}
			      y3++;
			    }
			  x3++;
			  
			}
		      y2++;
		    }
		  x2++;
		}
	      y11++;
	    }
	  x1++;
	}
      if(!found)
	printf("Case #%d: IMPOSSIBLE\n",i);
    }


  fclose(testfile);

  
}



bool isarea(int x1,int y11,int x2,int y2,int x3,int y3,double A)
{
  double a=distance(x1,y11,x2,y2);
  double b=distance(x1,y11,x3,y3);
  double c=distance(x2,y2,x3,y3);
  double s=0.5*(double)(a+b+c);
  double area=sqrt(s*(s-a)*(s-b)*(s-c));
  //printf("%lf\n",area);
  if((area-A)*(area-A)<1e-15)
    return 1;
  else
    return 0;
}


double distance(int x1,int y11,int x2,int y2)
{
  return sqrt((double)((x1-x2)*(x1-x2))+(double)((y11-y2)*(y11-y2)));
}
