#include <stdio.h>
#include <math.h>

double f,R,t,r,g;
bool isinside(double radius,double x,double y);
double arcarea(double radius,double x1,double y1,double x2,double y2);

double Ax,Ay,Bx,By,Dx,Dy,Cx,Cy;
double Axp,Ayp,Bxp,Byp,Cxp,Cyp,Dxp,Dyp;
double area;
double PI=3.14159265358979323;
int numtestcases;
FILE *testfile;
int main(int argc,char *argv[])
{


  f=1;
  R=100 ;
  t=1 ;
  r=1 ;
  g=10;
  testfile=fopen(argv[1],"r");
  fscanf(testfile,"%d",&numtestcases);
  //f=0.25;R= 1.0;t= 0.1;r= 0.01;g= 0.9;
  
  for(int testcase=1;testcase<=numtestcases;testcase++)
    {
      fscanf(testfile,"%lf",&f);
      fscanf(testfile,"%lf",&R);
      fscanf(testfile,"%lf",&t);
      fscanf(testfile,"%lf",&r);
      fscanf(testfile,"%lf",&g);

  area=0;
  if(g-2*f>0)
    {
  for(double m=0;m<=1000;m++)
    for(double n=0;n<=1000;n++)
      {
	if(isinside(R-t-f,r+m*(2*r+g)+f,r+n*(2*r+g)+f))
	  {
	    Ax=r+m*(2*r+g)+f;
	    Ay=r+n*(2*r+g)+f;
	    Bx=Ax+g-2*f;
	    By=Ay;
	    Dx=Ax;
	    Dy=Ay+g-2*f;
	    Cx=Ax+g-2*f;
	    Cy=Ay+g-2*f;
	    
	    Axp=Ax;
	    Ayp=sqrt((R-t-f)*(R-t-f)-Ax*Ax);
	    Cxp=Cx;
	    Cyp=sqrt((R-t-f)*(R-t-f)-Cx*Cx);
	    
	    Byp=By;
	    Bxp=sqrt((R-t-f)*(R-t-f)-By*By);
	    Dyp=Dy;
	    Dxp=sqrt((R-t-f)*(R-t-f)-Dy*Dy);
	    
	      //printf("%lf %lf %lf %lf %lf %lf %lf %lf\n",Ax,Ay,Bx,By,Cx,Cy,Dx,Dy);
	    if(isinside(R-t-f,Bx,By) && !isinside(R-t-f,Cx,Cy) && !isinside(R-t-f,Dx,Dy))
	      {
		area+=0.5*(g-2*f)*(Ayp-Ay+Cyp-By)+arcarea(R-t-f,Cxp,Cyp,Axp,Ayp);
		//printf("0-->%lf %lf %lf\n",0.5*(g-2*f)*(Ayp-Ay+Cyp-By)+arcarea(R-t-f,Cxp,Cyp,Axp,Ayp),m,n);
		
		//printf("->%lf\n",arcarea(R-t-f,Cxp,Cyp,Axp,Ayp));
		//printf("0--->%lf %lf %lf %lf %lf %lf %lf %lf\n",Ax,Ay,Bx,By,Cx,Cy,Dx,Dy);

	      }
	    if(!isinside(R-t-f,Bx,By) && !isinside(R-t-f,Cx,Cy) && isinside(R-t-f,Dx,Dy))
	      {
		area+=0.5*(g-2*f)*(Bxp-Ax+Dxp-Dx)+arcarea(R-t-f,Bxp,Byp,Dxp,Dyp);
		//printf("1-->%lf %lf %lf %lf \n",0.5*(g-2*f)*(Bxp-Ax+Dxp-Dx),arcarea(R-t-f,Bxp,Byp,Dxp,Dyp),m,n);
		//printf("->%lf\n",arcarea(R-t-f,Bxp,Byp,Dxp,Dyp));
	      }
	    if(!isinside(R-t-f,Bx,By) && !isinside(R-t-f,Cx,Cy) && !isinside(R-t-f,Dx,Dy))
	      {
		area+=0.5*(Ayp-Ay)*(Bxp-Ax)+arcarea(R-t-f,Bxp,Byp,Axp,Ayp);
		//printf("2--->%lf %lf %lf %lf %lf %lf %lf %lf\n",Ax,Ay,Bx,By,Cx,Cy,Dx,Dy);

		//printf("2-->%lf %lf %lf %lf %lf %lf %lf\n",Ayp,Ay,Bxp,Ax,arcarea(R-t-f,Bxp,Byp,Axp,Ayp),m,n);
		//printf("%lf %lf %lf %lf\n",Bxp,Byp,Axp,Ayp);
		//printf("%lf %lf\n",Ayp-Ay,Bxp-Ax);
		//printf("->%lf\n",arcarea(R-t-f,Bxp,Byp,Axp,Ayp));
	      }
	    if(isinside(R-t-f,Bx,By) && !isinside(R-t-f,Cx,Cy) && isinside(R-t-f,Dx,Dy))
	      {
		area+=(g-2*f)*(Dxp-Dx)+0.5*(Cx-Dxp)*(g-2*f+Cyp-By)+arcarea(R-t-f,Cxp,Cyp,Dxp,Dyp);
		//printf("3--> %lf %lf\n",Dxp-Dx,Cyp-By);
		//printf("3->%lf\n",(g-2*f)*(Dxp-Dx)+0.5*(Cx-Dxp)*(g-2*f+Cyp-By)+arcarea(R-t-f,Cxp,Cyp,Dxp,Dyp));
		//printf("3 %lf\n",arcarea(R-t-f,Cxp,Cyp,Dxp,Dyp));
		//printf("3--->%lf %lf %lf %lf %lf %lf %lf %lf\n",Ax,Ay,Bx,By,Cx,Cy,Dx,Dy);

	      }
	    
	      
	    if(isinside(R-t-f,Bx,By) && isinside(R-t-f,Cx,Cy) && isinside(R-t-f,Dx,Dy))
	      {
		//printf("Comes here\n");
		//printf("%lf\n",(g-2*f)*(g-2*f));
		area+=(g-2*f)*(g-2*f);
	      }
	   

	       
	     
	    
	  }
      }
    }
  printf("Case #%d: %lf\n",testcase,1-4*area/(PI*R*R));
    }
  

}



bool isinside(double radius,double x,double y)
{
  if(x*x+y*y>radius*radius)
    return 0;
  else
    return 1;
}


double arcarea(double radius,double x1,double y1,double x2,double y2)
{
  double tan1=y1/x1;
  double tan2=y2/x2;
  double difftan=(y2*x1-y1*x2)/(x1*x2+y1*y2);
  double theta=atan(difftan);
  //printf("%lf %lf %lf %lf %lf\n",x1,y1,x2,y2,theta);
  return 0.5*radius*radius*(theta-sin(theta));
}
