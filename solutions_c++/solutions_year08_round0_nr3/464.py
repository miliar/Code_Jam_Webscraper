#include <cstdio>
#include <cmath>

#define PI 3.14159265

double slice(double x, double y, double x1, double y1, double x2, double y2, double R)
{
  double ret;
  double alfa;
  double hsq;
  hsq=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
  alfa=acos(1.0-hsq/(2.0*R*R));
  ret=R*R*alfa/2.0;
  ret-=(y2-y)*x/2.0 + (x1-x)*y/2.0;
  return ret;
}

int main()
{
  int N;
  scanf("%d\n",&N);
  double prob;
  double f, R, t, r, g;

  for (int n=0; n<N; n++)
    {
      printf("Case #%d: ",n+1);

      scanf("%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g);
      t+=f;
      r+=f;
      g-=2*f;

      double nohitarea=0.0;

      for (double x=r; x<R-t; x+=(g+2*r))
	{
	  for (double y=r; x*x+y*y<(R-t)*(R-t); y+=(g+2*r))
	    {
	      if ((x+g)*(x+g)+(y+g)*(y+g) <= (R-t)*(R-t))
		{
		  nohitarea+=g*g;
		  //		  printf("a");
		}
	      else if ((x+g)*(x+g)+y*y<=(R-t)*(R-t) && (y+g)*(y+g)+x*x<=(R-t)*(R-t))
		{
		  double x1, x2, y1, y2;
		  x1=x+g;
		  y1=sqrt((R-t)*(R-t)-x1*x1);
		  y2=y+g;
		  x2=sqrt((R-t)*(R-t)-y2*y2);
		  nohitarea+=slice(x2, y1, x1, y1, x2, y2, R-t);
		  nohitarea+=(x2-x)*g;
		  nohitarea+=(x1-x2)*(y1-y);
		  //		  printf("b");
		}
	      else if ((x+g)*(x+g)+y*y<=(R-t)*(R-t) && !((y+g)*(y+g)+x*x<=(R-t)*(R-t)))
		{
		  double x1, x2, y1, y2;
		  x1=x+g;
		  y1=sqrt((R-t)*(R-t)-x1*x1);
		  x2=x;
		  y2=sqrt((R-t)*(R-t)-x2*x2);
		  nohitarea+=slice(x2, y1, x1, y1, x2, y2, R-t);
		  nohitarea+=g*(y1-y);
		  //		  printf("c");
		}
	      else if (!((x+g)*(x+g)+y*y<=(R-t)*(R-t)) && (y+g)*(y+g)+x*x<=(R-t)*(R-t))
		{
		  double x1, x2, y1, y2;
		  y1=y;
		  x1=sqrt((R-t)*(R-t)-y1*y1);
		  y2=y+g;
		  x2=sqrt((R-t)*(R-t)-y2*y2);
		  nohitarea+=slice(x2, y1, x1, y1, x2, y2, R-t);
		  nohitarea+=(x2-x)*g;
		  //		  printf("d");
		}
	      else
		{
		  double x1, x2, y1, y2;
		  x2=x;
		  y1=y;
		  x1=sqrt((R-t)*(R-t)-y1*y1);
		  y2=sqrt((R-t)*(R-t)-x2*x2);
		  nohitarea+=slice(x, y, x1, y1, x2, y2, R-t);
		  //		  printf("e");
		}
	    }
	}
      //      printf("\n");


      prob=1.0-(4.0*nohitarea/(R*R*PI));


      printf("%lf\n", prob);
    }

  return 0;
}
