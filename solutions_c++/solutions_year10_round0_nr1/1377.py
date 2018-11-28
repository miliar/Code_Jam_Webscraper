#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	ifstream in("A-large.in", ios::in);
	ofstream out("large.out", ios::out);

	if(in.good())
	{
		long long nbCase;
		in >> nbCase;
		for(long long i=0; i<nbCase; i++)
		{
			long long N;
			long long K;

			in >> N >> K;

			long long range = pow((long double) 2.0, (long double) (N+0.0));

			if((K+1)%range==0)
			{
				out << "Case #" << (i+1) << ": ON" << endl;
			}
			else
				out << "Case #" << (i+1) << ": OFF" << endl;
		}
	}
	return 0;
}