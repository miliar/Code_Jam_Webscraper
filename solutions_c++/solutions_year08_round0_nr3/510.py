#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

const float M=100000;
float f,R,t,r,g;

float mk(double x, double y)
{
	int n1=0,s1,s2,s3,s4;
	double kx, ky,x1 , y1, x2, y2, res, s, s0, st, alpha, a, b, c,p,r1,g1;


	x=x+f;y=y+f;
	r1=R-t-f;
	g1=g-2*f;

	if(x*x+y*y<r1*r1) s1=1; else s1=0;
	if(x*x+(y+g1)*(y+g1)<r1*r1) s2=1; else s2=0;
	if((x+g1)*(x+g1)+(y+g1)*(y+g1)<r1*r1) s3=1; else s3=0;
	if((x+g1)*(x+g1)+y*y<r1*r1) s4=1; else s4=0;
	
	if(!s1) {s=0;printf("!s1; ");}//1 ok
	else if (s3) {s=g1*g1;printf("s3; ");}//2 ok
	else if(s2 && s4)//3
	{

	y1=y+g1; x1=sqrt(r1*r1-y1*y1);
	x2=x+g1; y2=sqrt(r1*r1-x2*x2);
	
	a=sqrt(x1*x1+y1*y1);
	b=sqrt(x2*x2+y2*y2);
	c=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	p=(a+b+c)/2;
	st=sqrt(p*(p-a)*(p-b)*(p-c));
	alpha=asin(2*st/r1/r1);
	s0=r1*r1*alpha/2-st;
	s=g1*g1-0.5*(x+g1-x1)*(y+g1-y2)+s0;
	printf("s2&&s4; ");
	}

	else if (!s2 && !s4)//4 ok
	{
	x1=x; y1=sqrt(r1*r1-x1*x1);
	y2=y; x2=sqrt(r1*r1-y2*y2);
	
	a=sqrt(x1*x1+y1*y1);
	b=sqrt(x2*x2+y2*y2);
	c=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	p=(a+b+c)/2;
	st=sqrt(p*(p-a)*(p-b)*(p-c));
	alpha=asin(2*st/r1/r1);
	s0=r1*r1*alpha/2-st;
	s=0.5*(y1-y)*(x2-x)+s0;
	printf("!s2&&!s4; ");
	}

	else if (s2 && !s4)//5
	{
	y1=y+g1; x1=sqrt(r1*r1-y1*y1);
	y2=y; x2=sqrt(r1*r1-y2*y2);
	
	a=sqrt(x1*x1+y1*y1);
	b=sqrt(x2*x2+y2*y2);
	c=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	p=(a+b+c)/2;
	st=sqrt(p*(p-a)*(p-b)*(p-c));
	alpha=asin(2*st/r1/r1);
	s0=r1*r1*alpha/2-st;
	s=(x1-x)*g1+0.5*(x2-x1)*g1+s0;
	printf("s2&&!s4; ");
	}

	else if (!s2 && s4)//6
	{
	x1=x; y1=sqrt(r1*r1-x1*x1);
	x2=x+g1; y2=sqrt(r1*r1-x2*x2);
	
	a=sqrt(x1*x1+y1*y1);
	b=sqrt(x2*x2+y2*y2);
	c=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	p=(a+b+c)/2;
	st=sqrt(p*(p-a)*(p-b)*(p-c));
	alpha=asin(2*st/r1/r1);
	s0=r1*r1*alpha/2-st;
	s=(y2-y)*g1+0.5*(y1-y2)*g1+s0;
	printf("!s2&&s4; ");
	}

	printf("s=%f\n",s);
	return s;
}

int main(int argc, char* argv)
{
	FILE *fin, *fout;
	double x, y, ans, kx, ky,c1,s;
	int n, i, j, k, n1, n2;

	srand(time(NULL));
	fin=fopen("C-large.in", "r");
	fout=fopen("C.txt", "w");
	fscanf(fin, "%d", &n);
	for(i=0;i<n;i++)
	{
		fscanf(fin, "%f%f%f%f%f", &f, &R, &t, &r, &g);
		
		if(g-2*f<0) ans=1;
		else
		{
		s=0;
		for(x=r;x<R-t;x+=2*r+g)
			for(y=r;y<R-t;y+=2*r+g)
				if(x*x+y*y<(R-t-f)*(R-t-f))
				{
					if ((x+g)*(x+g)+(y+g)*(y+g)<(R-t-f)*(R-t-f)) s+=(g-2*f)*(g-2*f);
					else s+=mk(x, y);
				}
		ans=1-4*s/R/R/3.1415926;
		}
		fprintf(fout, "Case #%d: %f\n", i+1, ans);
		printf("Case #%d Complete!\n", i+1);
	}
	fclose(fin);
	fclose(fout);
	scanf("%f", r);
	return 0;
}