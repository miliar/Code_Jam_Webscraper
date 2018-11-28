#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int N;
float g,R,t,r,f;
float _g,_R,_t,_r,_f;

#define pi 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))

void main()
{
	FILE *fi;
	FILE *o;
	int i,j,k;
	long double escape,freespace;
	fi=fopen("C-small-attempt0.in","rt");
	o=fopen("C-small-attempt0.out","wt");
	fscanf(fi,"%d\n",&N);
	for (k=0;k<N;++k)
	{
		fscanf(fi,"%f %f %f %f %f\n",&_f,&_R, &_t, &_r, &_g);
		f=_f;
		R=_R;
		t=_t;
		r=_r;
		g=_g;
		r+=f;
		g-=2*f;
		t+=f;
		i=0;j=0;
		if (g>0)
		{
			freespace = 0;
			for (i=0;r+i*(g+2*r)<=R+0.0000001;++i)
			{
				for (j=0;r+j*(g+2*r)<=R+0.0000001;++j)
				{
					long double x0,x1,y0,y1;
					x0 = r+i*(g+2*r);
					y0 = r+j*(g+2*r);
					x1 = r+g+i*(g+2*r);
					y1 = r+g+j*(g+2*r);
					if (sqr(x1)+sqr(y1)<sqr(R-t))
					{
						freespace += sqr(g);
					}	
					else
						if (sqr(x0)+sqr(y0)<sqr(R-t))
						{
							float a1, a2, s1, s2, tmp, a ,b;
							if (sqr(x1)+sqr(y0)>sqr(R-t))
							{
								a1 = asin(y0/(R-t));
								tmp = sqrt(sqr(R-t)-sqr(y0));
								s1 = tmp*y0/2.0+(x1-tmp)*y0;
							}
							else
							{
								a1 = acos(x1/(R-t));
								tmp = sqrt(sqr(R-t)-sqr(x1));
								s1 = tmp*x1/2.0;
							}
							if (sqr(x0)+sqr(y1)>sqr(R-t))
							{
								a2 = asin(x0/(R-t));
								tmp = sqrt(sqr(R-t)-sqr(x0));
								s2 = tmp*x0/2.0+(y1-tmp)*x0;
							}
							else
							{
								a2 = acos(y1/(R-t));
								tmp = sqrt(sqr(R-t)-sqr(y1));
								s2 = tmp*y1/2.0;
							}
							freespace += sqr(g)-(x1*y1-s1-s2-(pi/2.0-a1-a2)*sqr(R-t)/2.0);
						}
				}
			}
			escape = 4*freespace/(pi*sqr(R));
			fprintf(o,"Case #%d: %.6f\n",k+1,1.0-escape);
		}
		else
		{
			fprintf(o,"Case #%d: %.6f\n",k+1,1.0);
		}
	}
	fclose(fi);
	fclose(o);
}