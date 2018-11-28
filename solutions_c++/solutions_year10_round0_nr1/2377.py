#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int T;
	in >> T;
	for(int c=0;c<T;c++)
	{
		int N,K;
		in >> N >> K;

		double D = pow(2.0,N)-1;
		int A = int(D);

		if( K < A )
			out << "Case #" << c+1 << ": OFF" << endl;
		else if( K == A )
			out << "Case #" << c+1 << ": ON" << endl;
		else
		{
			if( (K-A)%(A+1) == 0 )
				out << "Case #" << c+1<< ": ON" << endl;
			else
				out << "Case #" << c+1 << ": OFF" << endl;
		}
	}
	return 0;

}