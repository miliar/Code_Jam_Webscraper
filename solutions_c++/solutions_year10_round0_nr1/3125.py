// Code Jam 2010 No.1
// Yuxiang Wang @ Tsinghua University

#include <fstream>
#include <memory>
#include <cmath>
using namespace std;

int main()
{
	ifstream in ("input.in");
	long int T, N, K;
	in >> T;
	
	ofstream out ("output.out");
	for (int i=0; i<T; i++)
	{
		in >> N >> K;
		long int temp = 1;
		for (int j=0; j<N; j++)
			temp = 2*temp;

		long int t = temp - 1;
		if (K % temp == t)
		{
			out << "Case #" << i+1 << ": " <<  "ON" << endl;
			continue;
		}
		else
		{
			out << "Case #" << i+1 << ": " <<  "OFF" <<endl;
			continue;
		}
	}

	out.close();
	return 0;
}