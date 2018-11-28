//MaximZh
//Qualification_C.cpp

#include <stdio.h> //Standard C++ library
#define _USE_MATH_DEFINES
#include <math.h> //Standard C++ library

//Calculate square of a right-angled triangle with arc hypotenuse
double CalcSquare(double r, double x1, double y1, double x2, double y2, double a1, double a2)
{
	double S = 0.5*(r*r*(a1-a2)-x1*(y1-y2)-y2*(x2-x1));
	if( S < 0.0 )
		return 0.0;
	else
		return S;
}

int main()
{
	int N = 0; //Number of cases

	FILE *pfin = fopen("data.in", "rt");
	FILE *pfout = fopen("data.out", "wt");
	fscanf(pfin, "%d", &N); //Input number of cases
	for( int i = 0; i < N; i++ )
	{
		float ff, fR, ft, fr, fg;
		fscanf(pfin, "%f", &ff);
		fscanf(pfin, "%f", &fR);
		fscanf(pfin, "%f", &ft);
		fscanf(pfin, "%f", &fr);
		fscanf(pfin, "%f", &fg);
		double f = ff;
		double R = fR;
		double t = ft;
		double r = fr;
		double g = fg;
		double EscSquare = 0.0;
		double Sq0 = (g-2*f)*(g-2*f);
		double shift = g+2*r;
		double R1 = R-t-f;
		double y1 = r-f+g;
		double y2 = r+f;
		while( y2<R1 )
		{
			double x1 = r+f;
			double x2 = r-f+g;
			double as1 = asin(y1/R1);
			double as2 = asin(y2/R1);
			double S = 0.0;					
			while( R1*R1 >= (x2*x2 + y1*y1) )
			{
				S += Sq0;
				x1 += shift;
				x2 += shift;
			}
			
			while( R1*R1 >= (x1*x1 + y2*y2) )
			{
				bool b1 = (R1*R1 >= (x1*x1 + y1*y1));
				bool b2 = (R1*R1 >= (x2*x2 + y2*y2));
				if( b1 )
					if( b2 )
					{						
						double x1a = sqrt(R1*R1-y1*y1);
						double y2a = sqrt(R1*R1-x2*x2);
						double ac2 = acos(x2/R1);
						S += (y1-y2)*(x1a-x1)+(y2a-y2)*(x2-x1a);
						S += CalcSquare(R1, x1a, y1, x2, y2a, as1, ac2);						
					}
					else
					{
						double x1a = sqrt(R1*R1-y1*y1);
						double x2a = sqrt(R1*R1-y2*y2);
						S += (y1-y2)*(x1a-x1);
						S += CalcSquare(R1, x1a, y1, x2a, y2, as1, as2);
					}
				else
					if( b2 )
					{
						double y1a = sqrt(R1*R1-x1*x1);
						double y2a = sqrt(R1*R1-x2*x2);
						double ac1 = acos(x1/R1);
						double ac2 = acos(x2/R1);
						S += (x2-x1)*(y2a-y2);
						S += CalcSquare(R1, x1, y1a, x2, y2a, ac1, ac2);
					}
					else
					{
						double y1a = sqrt(R1*R1-x1*x1);
						double x2a = sqrt(R1*R1-y2*y2);
						double ac1 = acos(x1/R1);
						S += CalcSquare(R1, x1, y1a, x2a, y2, ac1, as2);
					}
				x1 += shift;
				x2 += shift;
			}
			y1 += shift;
			y2 += shift;
			EscSquare += S;
		}
		double P = 1-(EscSquare*4/(M_PI*R*R));
		fprintf(pfout, "Case #%d: %f\n", i+1, P);
	}
	fclose(pfout);
	fclose(pfin);
	return 0;
}