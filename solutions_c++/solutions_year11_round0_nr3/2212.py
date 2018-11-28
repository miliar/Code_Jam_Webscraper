#include <fstream>
using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	for(int t=1; t<=T; t++)
	{
		int N;
		int A;
		int xor = 0 ;
		long sum = 0, min = 10000000;  
		fin >> N;
		for(int i=0; i<N; i++)
		{
			fin >> A;
			sum += A;
			xor ^= A;
			if(min > A)
				min = A;
		}
		if(xor == 0)
			fout << "Case #" << t << ": " << sum-min << endl;
		else
			fout << "Case #" << t << ": NO" << endl;
	}
	return 0;
}

