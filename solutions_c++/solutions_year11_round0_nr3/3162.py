#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	unsigned T;
	input >> T;

	for(unsigned t=0; t<T; ++t)
	{
		unsigned N;
		input >> N;

	    unsigned result;
		input >> result;
		unsigned sum = result;
		unsigned min = result;

		for(unsigned n=1; n<N; ++n)
		{
			unsigned current;
			input >> current;
			result ^= current;
			sum += current;
			if(current<min)
				min = current;
		}

		if(result == 0)
			output << "Case #" << t+1 << ": " << sum-min << endl;
		else
			output << "Case #" << t+1 << ": NO" << endl;

	}
	
	input.close();
	output.close();
	return 0;
}