#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main()
{
	long long T, N, K;
	long long result;
	long long state;

	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	
	ifs >> T;
	for(int i=0;i<T;i++)
	{
		ifs >> N >> K;
		state=1;
		for (int j=0;j<N;j++)
			state *= 2;

		result = K%state;
		if (result == state-1)
			ofs << "Case #" << i+1 << ": ON" << endl;
		else
			ofs << "Case #" << i+1 << ": OFF" << endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}
