#include <cstdio>
#include <cmath>

using namespace std;
const double PI = 3.14159265;

double areatri(double Ax,double Ay,double Bx,double By,double Cx,double Cy)
{
	return abs(Ax*By + Bx*Cy + Cx*Ay - Ax*Cy - Cx*By - Bx*Ay)/2;
}

double sqr(double x)
{
	return x*x;
}

double area(double f, double R, double t, double r, double g)
{
	if (g<=2*f) return 0;
	double total_result = 0;
	for (int i=1;i<(R-t+g+r)/(2*r+g);i++)
	{
		double partial_result = 0;
		int m;
		if (sqr(R-t-f)>sqr(i*(2*r+g)-r-f)) m = floor((sqrt(sqr(R-t-f) - sqr(i*(2*r+g)-r-f))+r+f)/(2*r+g));
		else m = 0;

		partial_result += (m*sqr(g-2*f));
		
		double j_lim;
		if (sqr(R-t-f)<sqr((i-1)*(2*r+g)+f+r)) j_lim = -1;
		else j_lim=(sqrt(sqr(R-t-f)-sqr((i-1)*(2*r+g)+f+r))+r-f+g)/(2*r+g);
		for (int j=m+1;j<j_lim;j++)
		{
			double NVx = r+(i-1)*(2*r+g)+f;
			double NVy = j*(2*r+g)-f-r;
			double SEy = r+(j-1)*(2*r+g)+f;
			double SEx = i*(2*r+g)-f-r;
			double SVy = SEy;
			double SVx = NVx;

			double Nx,Ny,Sx,Sy;

			if (sqrt(sqr(NVx) + sqr(NVy)) < R-t-f)
			{
				Ny = NVy;
				Nx = sqrt(sqr(R-t-f)-sqr(Ny));
			}
			else
			{
				Nx = SVx;
			    Ny = sqrt(sqr(R-t-f)-sqr(Nx));	
			}

			if (sqrt(sqr(SEx) + sqr(SEy)) < R-t-f)
			{
				Sx = SEx;
				Sy = sqrt(sqr(R-t-f)-sqr(Sx));
			}
			else
			{
				Sy = SVy;
			    Sx = sqrt(sqr(R-t-f)-sqr(Sy));	
			}
			
			partial_result += areatri(Nx,Ny,SVx,SVy,Sx,Sy);
			partial_result += areatri(Nx,Ny,SVx,SVy,NVx,NVy);
			partial_result += areatri(SEx,SEy,SVx,SVy,Sx,Sy);

			double angle = acos((Nx*Sx + Ny*Sy)/(sqrt(sqr(Nx)+sqr(Ny))*sqrt(sqr(Sx)+sqr(Sy))));
			partial_result+= (angle/2 - sin(angle)/2) * sqr(R-t-f);
		}

		total_result += partial_result;
	}

	return 4*total_result;
}

int main()
{
	int N;
	scanf("%d",&N);
	
	float f,R,t,r,g;

	for (int i=0;i<N;i++)
	{
		scanf("%f %f %f %f %f",&f, &R, &t, &r, &g);
		printf("Case #%d: %.6f\n", i+1, 1-area(f,R,t,r,g)/PI/sqr(R));
	}

	return 0;
}