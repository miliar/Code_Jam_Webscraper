// monte carlo precision
#define PRECISION (2000000)

// rec depth
#define MAX_DEPTH (7)

#include <cstdio>
#include <cmath>

using namespace std;

double fly, outer, frame, cord, square;
double inner; // inner radius
double inner2; // inner*inner
double diff; // square+cord
int gran; // granularity for monte carlo
double invGran2; // 1/((gran+1)*(gran+1))

void input(void)
{
	scanf("%lf %lf %lf %lf %lf", &fly, &outer, &frame, &cord, &square);
	
	// transform the fly to a dot
	square -= 2*fly;
	cord = (cord+fly)*2;
	
	frame += fly;
	inner = outer-frame;
	inner2 = inner*inner;
	diff = square+cord;
	
	gran = (int)ceil(sqrt(PRECISION/inner*diff));
	if(gran==1)
	{
		gran=20;
	}
	invGran2 = 1/((double)(gran+1)*(double)(gran+1));
}

double monteCarlo(const double &row, const double &col, double square)
{
	static double delta; // distance between points
	static int count; // count of inner points
	static int i, j;
	static double x, y;
	
	delta = square/(double)gran;
	count = 0;
	
	for(i=0; i<=gran; ++i)
	{
		for(j=0; j<=gran; ++j)
		{
			x=row+i*delta;
			y=col+j*delta;
			if(x*x+y*y<inner2)
			{
				++count;
			}
		}
	}
	
	return (double)count*square*invGran2*square;
}

double rec(double x1, double y1, double x2, double y2, char depth)
{
	if(x2*x2+y2*y2 < inner2)
	{
		return (x2-x1)*(y2-y1);
	}
	if(inner2 < x1*x1+y1*y1)
	{
		return 0;
	}
	
	if(depth >= MAX_DEPTH)
	{
		return monteCarlo(x1, y1, x2-x1);
	}
	
	double mx, my;
	mx=(x1+x2)*0.5;
	my=(y1+y2)*0.5;
	return rec(x1, y1, mx, my, depth+1)
			+rec(x1, my, mx, y2, depth+1)
			+rec(mx, y1, x2, my, depth+1)
			+rec(mx, my, x2, y2, depth+1);
}

double chance(void)
{
	double row, col;
	double squaresSurface=0;
	double cirSurface;
	
	if(square<=1e-15)
	{
		return 1;
	}
	
	for(row=cord*0.5; row<inner; row+=diff)
	{
		for(col=cord*0.5; col<inner; col+=diff)
		{
			squaresSurface += rec(row, col, row+square, col+square, 0);
		}
	}
	cirSurface = M_PI*outer*outer;
	
	return (cirSurface-squaresSurface*4)/cirSurface;
}

int main(void)
{
	int i, N;
	
	scanf("%d", &N);
	for(i=1; i<=N; ++i)
	{
		input();
		printf("Case #%d: %.6lf\n", i, chance());
	}
	
	return 0;
}
