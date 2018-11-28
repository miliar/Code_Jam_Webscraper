#include <iostream>
#include <fstream>


using namespace std;

int gcd ( int A, int B )
{
	if( A == 0 )	return B;
	else		return gcd( B%A, A );
}

pair <int, int> reduce ( int A, int B )
{
	int C = gcd(A, B);
	return make_pair (A/C, B/C);
	
}

int main (int argc, char const* argv[])
{
	ifstream in ("A.in");
	ofstream out ("A.out");
	
	int T, Pd[2], Pg[2];
	long long N;
	pair <int, int> P;
	in >> T;
	
	for (unsigned int t = 0; t < T; t += 1)
	{
		in >> N >> Pd[0] >> Pg[0];
		
		P=reduce(Pd[0], 100);
		Pd[0] = P.first;
		Pd[1] = P.second;
		//cout << t+1 << " -> " ;
		//cout << Pd[0] << ' ' << Pd[1];
		P=reduce(Pg[0], 100);
		Pg[0] = P.first;
		Pg[1] = P.second;
		//cout << ' ' << Pg[0] << ' ' << Pg[1] << "\n";
		out << "Case #" << t+1 << ": ";
		if(Pd[1] > N)	out << "Broken\n";
		else
		{
			if( (Pg[1] - Pg[0]) == 0 && (Pd[1]-Pd[0]) != 0  )	out << "Broken\n";
			else if ( Pg[0] == 0 && Pd[0] != 0 )	out << "Broken\n";
			else	out << "Possible\n";
		}
	}
	
	return 0;
}














