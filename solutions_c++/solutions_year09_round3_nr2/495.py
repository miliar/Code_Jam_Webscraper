#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

template < class T>
T** array(int m, int n)
{
	T **p;
	p = (T**)malloc(m*sizeof(T*));
	p[0] = (T*)malloc(m*n*sizeof(T));
	if ( p[0] == NULL )
	{
		cout<<"error."<<endl;
	}
	memset(p[0],0,m*n*sizeof(T));
	for (int i=1; i<m; ++i)
		p[i]=p[i-1]+n;
	return p;
}

template < class T>
void freearray(T** p)
{
	free(*p); free(p);
}

#define MAX 1000

int main()
{
	int nCase;
	ifstream ifs( "B-large.in" );
	ofstream ofs( "B-large-out.txt" );

	char buffer[MAX];

	ifs>>nCase;

	for (int iCase = 0; iCase < nCase; iCase++ )
	{
		double dmin, tmin;
		int N = 0;
		ifs >> N;
		double x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;
		for ( int iN = 0; iN < N; iN++ )
		{
			int iTmp;
			ifs >> iTmp;	x += iTmp;
			ifs >> iTmp;	y += iTmp;
			ifs >> iTmp;	z += iTmp;
			ifs >> iTmp;	vx += iTmp;
			ifs >> iTmp;	vy += iTmp;
			ifs >> iTmp;	vz += iTmp;
		}
		x /= (double)N;	y /= (double)N;	z /= (double)N;
		vx /= (double)N;	vy /= (double)N;	vz /= (double)N;

		double a = vx*vx + vy*vy + vz*vz;
		double b = 2*( x*vx + y*vy + z*vz );
		double c = x*x + y*y + z*z;


 		if ( c == 0 )
		{
			tmin = 0.0;
			dmin = 0.0;
		}
		else if ( a == 0.0 )
		{
			if ( b >= 0.0 )
			{
				tmin = 0.0;
				dmin = dmin = sqrt(c);
			}
			else
			{
				printf("a=0,b!=0,no way!\n");
				tmin = -1.0*c/b;
				dmin = 0.0;
			}
		}
		else if ( b == 0 )
		{
			tmin = 0.0;
			dmin = sqrt(c);
		}
		else
		{
			double negBdiv2A = -0.5*b/a;
			if ( negBdiv2A >= 0 )
			{
				double b2sub4ac = b*b -4.0*a*c;
				if ( b2sub4ac < 0.0 )
				{
					tmin = negBdiv2A;
					dmin = (4.0*a*c-b*b)/4.0/a;
					dmin = sqrt(dmin);
				}
				else
				{
					tmin = negBdiv2A - sqrt(b2sub4ac)/2.0/a;
					dmin = 0.0;
				}
			}
			else
			{
				tmin = 0.0;
				dmin = sqrt(c);
			}
		}
		
		char output[MAX];
		sprintf(output,"%.8f %.8f",dmin, tmin);
		ofs<<"Case #"<<iCase+1<<": "<<output<<endl;
	}
	
	ifs.close();
	ofs.close();

	return 0;
}    