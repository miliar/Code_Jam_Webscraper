/*
ID: ebappa11
PROG: solder
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>



#define MAXN 1005
using namespace std;

int main() {
	ofstream out ("C.out");
	ifstream in ("C.in");
	int T = 0, Total, A, N, M;
	
	int ts;
	in >> ts;

	for (unsigned int t = 0; t < ts; t += 1)
	{
		T = 0;
		M = 10000000;
		Total = 0;
		in >> N;

		for (unsigned int i = 0; i < N; i += 1)
		{
			in >> A;
			T ^= A;
			M = min (M, A);
			Total += A;
		}

		
		out << "Case #" << t+1 << ": ";
		if( T == 0 )	out << Total - M << "\n";
		else		out << "NO\n";
	}


	
	
	return 0;
}








