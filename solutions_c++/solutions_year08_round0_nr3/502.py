#include <fstream.h>
#include <iomanip.h>
#include <math.h>

double square(double x, double y, double R, double f, double g)
{
	double x1,x2,x3,y1,y2,y3,x4,y4,s,ugol1,ugol3;
	if (g<=2*f) return 0;

	else if ( (x+g)*(x+g)+(y+g)*(y+g)<=(R-f)*(R-f))
	{
	     return (g-2*f)*(g-2*f);
	}
	else
	{
		if ( (x+f)*(x+f)+(y+f)*(y+f)>=(R-f)*(R-f) ) return 0;

		x=x+f;
		y=y+f;
		x1=x;
		y1=y+g-2*f;
		if (x1*x1+y1*y1 >= (R-f)*(R-f))
		{
			y1=pow(fabs((R-f)-x1),0.5)*
			pow(R-f+x1,0.5);
			x2=x+g-2*f;
			y2=y;
			if (x2*x2+y2*y2 > (R-f)*(R-f))
			x2=pow(fabs((R-f)-y2),0.5)*pow(R-f+y2,0.5);
			else y2=pow(fabs((R-f)-x2),0.5)*pow(R-f+x2,0.5);
						ugol1=asin(y1/(R-f));
			ugol3=asin(y2/(R-f));
			s=(R-f)*(R-f)*(ugol1-sin(ugol1*2)/2
			-ugol3+sin(ugol3*2)/2)/2-y*(x2-x1);
			return s;
		}
		else
		{
			x2=x+g-2*f;
			y2=y;
			if (x2*x2+y2*y2 > (R-f)*(R-f))
			x2=pow(fabs((R-f)-y2),0.5)*pow(R-f+y2,0.5);
			y3=y1;
			x4=x2;
			x3=pow(fabs((R-f)-y3),0.5)*pow(R-f+y3,0.5);
			y4=pow(fabs((R-f)-x4),0.5)*pow(R-f+x4,0.5);
			s=(y1-y)*(x3-x);
			s+=(x2-x3)*(y1-y+y4-y)/2;
			ugol1=asin(y3/(R-f));
			ugol3=asin(y4/(R-f));
			s+=(R-f)*(R-f)*(ugol1-ugol3-sin(ugol1-ugol3))/2;
			return s;
		}
	}


}
int main()
{
	fstream fin("in.txt",ios::in);
	fstream fout("out.txt",ios::out);
	int N;
	int k=0;
	int i,ing,j;
	double f,R,t,r,g;
	double s;
	double result;
	fin>>N;
	for(i=0;i<N;i++)
	{
		s=0;
		fin>>f>>R>>t>>r>>g;
		for(j=0;j<(R-t-r)/(g+2*r);j++)
		for(k=0;k<(R-t-r)/(g+2*r);k++)
		s+= square(j*(g+2*r)+r,k*(g+2*r)+r,R-t,f,g);
		result=((4/M_PI)*(s/R))/R;
		fout<<"Case #"<<i+1<<": "<<setprecision(6)<<(1-result)<<endl;
	}

	fin.close();
	fout.close();
	return 0;
}