#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define _USE_MATH_DEFINES
#include <math.h>

char buff[128];

void get_buff()
{
	buff[0]='\0';
	gets(buff);
	//printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
	return atoi(buff);
}

void get_input(double *f, double *R ,double *t ,double *r ,double *g)
{
	get_buff();
	char *loc=buff;
	*f=atof(loc);
	loc=strchr(loc,' ')+1;
	*R=atof(loc);
	loc=strchr(loc,' ')+1;
	*t=atof(loc);
	loc=strchr(loc,' ')+1;
	*r=atof(loc);
	loc=strchr(loc,' ')+1;
	*g=atof(loc);
}

double norm_sq(double x,double y)
{
	return x*x+y*y;
}

double angle(double x1,double y1,double x2,double y2,double R_sq)
{
	return acos((x1*x2+y1*y2)/R_sq);
}

double segment(double ang,double R_sq)
{
	return R_sq*(0.5*ang - sin(0.5*ang)*cos(0.5*ang));
}

bool is_crossing(double a,double b1,double b2,double R_sq,double *crosspos)
{
	*crosspos=sqrt(R_sq-a*a);
	return b1<=*crosspos && *crosspos<=b2;
}

int main(int argc, char* argv[])
{
	int n=get_num();

	for (int i=0 ; i<n ; ++i)
	{
		double f=0.0,R,t,r,g;
		get_input(&f,&R,&t,&r,&g);
		double area=M_PI*R*R;

		// assume that the fly's size is 0. fix all other variables.
		double R1=R-t-f;
		double R1_sq=R1*R1;
		double g1=g-2*f;
		double r1=2*r+2*f;
		double fly_space=0;

		if (R1>0 && g1>=0 && r1>=0)
		{
			double left,right,top,bottom,
				left_cross,right_cross,top_cross,bottom_cross,
				ang,add;
			for (int i=0 ;  norm_sq( left=i*(r1+g1)+0.5*r1 , 0.5*r1 ) <= R1_sq ; ++i )
			{
				right=left+g1;
				for (int j=0 ; norm_sq( i*(r1+g1)+0.5*r1 , bottom=j*(r1+g1)+0.5*r1 ) <= R1_sq ; ++j )
				{
					add=0;
					top=bottom+g1;
					if (is_crossing(top,left,right,R1_sq,&top_cross))
					{
						if (is_crossing(bottom,left,right,R1_sq,&bottom_cross)) // case 1 : crossing top and bottom
						{
							ang=angle(bottom_cross,bottom,top_cross,top,R1_sq);
							add=segment(ang,R1_sq) // segment
								+ (top_cross-left + bottom_cross-left)*g1/2; //trapezoid
						}
						else if (is_crossing(right,bottom,top,R1_sq,&right_cross)) // case 2 : crossing top and right
						{
							ang=angle(right,right_cross,top_cross,top,R1_sq);
							add=segment(ang,R1_sq) // segment
								+ g1 * g1 // whole rect
								- (right-top_cross)*(top-right_cross)/2; // upper right triangle
						}
						else
							perror("shouldn't happen\n");
					}
					else
					{
                        if (is_crossing(left,bottom,top,R1_sq,&left_cross))
						{
							if (is_crossing(bottom,left,right,R1_sq,&bottom_cross)) // case 3 : crossing left and bottom
							{
								ang=angle(bottom_cross,bottom,left,left_cross,R1_sq);
								add=segment(ang,R1_sq) //segment
									+ (left_cross-bottom)*(bottom_cross-left)/2; // lower right triangle
							}
							else if (is_crossing(right,bottom,top,R1_sq,&right_cross)) // case 4 : crossing left and right
							{
								ang=angle(right,right_cross,left,left_cross,R1_sq);
								add+=segment(ang,R1_sq) // segment
									+ (left_cross-bottom + right_cross-bottom)*g1/2; //trapezoid
							}
							else
								perror("shouldn't happen\n");
						}
						else // case 5 : not crossing
						{
							add=g1*g1;
						}
					}
					fly_space+=add;
				}
			}
		}

		// only calculated a quarter of the sphere
		fly_space*=4;

		printf("Case #%d: %6f\n",i+1,(float)(1-(fly_space/area)));
	}
	return 0;
}

