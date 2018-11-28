#include <iostream>
#include <fstream>
#include <math.h>

#define INPUT_F "B-large.in"
#define OUTPUT_F "B-large.out"
using namespace std;

int main ()
{
	fstream fin, fout;
	fin.open ( INPUT_F, fstream::in);
	fout.open ( OUTPUT_F, fstream::out);
	int T = 0;
	fin >> T;
	fout.precision(8);
	fout.setf(ios::fixed,ios::floatfield); 

	long double A, B, C;
	for ( int i = 0; i < T; i++)
	{
		int N;
		fin >> N;
		long long svx = 0;
		long long svy = 0;
		long long svz = 0;
		long long sx = 0;
		long long sy = 0;
		long long sz = 0;
		for (int j = 0; j < N; j++)
		{
			long long tmp;
			fin >> tmp;
			sx += tmp;
			fin >> tmp;
			sy += tmp;			
			fin >> tmp;
			sz += tmp;			
			fin >> tmp;
			svx += tmp;			
			fin >> tmp;
			svy += tmp;
			fin >> tmp;
			svz += tmp;
		}
		fout << "Case #" << i+1 << ": ";
		A = ((double)(svx *svx) + (double)(svy *svy) + (double)(svz *svz));
		B = 2. * ((double) (svx * sx) + (double) (svy * sy) + (double) (svz * sz));
		C = ((double)(sx *sx) + (double)(sy *sy) + (double)(sz *sz));
		if ( (svx ==0 && svy == 0 && svz == 0) || B >= 0.)
		{
			fout << sqrt(C) / (double)N;
			fout << " ";
			fout << "0.00000000" << endl;
		}		
		else
		{
			double t = fabs (- B / (2. * A));
			fout << sqrt ( C + B * t + A * t * t) / (double)N;
			fout << " ";
			fout << t << endl;
		}
			
	}
	fin.close ( );
	fout.close ( );
}