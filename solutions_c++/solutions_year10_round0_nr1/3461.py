#include <fstream>
#include <string>
using namespace std;

int main ()
{
	// Generic File Instantiations
	ifstream input;
	ofstream output;
	
	string inputname, outputname;
	
	inputname = "input.in";
	outputname = "output.out";
	input.open (inputname.c_str ());
	output.open (outputname.c_str ());
	
	// Input Read & Initializations
	
	int T; // number of test cases
	input >> T;

	int i,j;

	unsigned int N, K;
	bool on = false;

	// Fill array and print	
	for (i = 1; i <= T; i++)
	{
		input >> N >> K;

		if (N == 0 || K == 0)
		{
			on = false;
		}
		else
		{
			K++;

			for (j = 0; j < N; j++)
			{
				if (K%2 == 0)
				{
					K=K/2;
					on = true;
				}
				else
				{
					on = false;
					break;
				}
			}
		}

		if (on)
			output << "Case #" << i << ": ON" << endl;
		else
			output << "Case #" << i << ": OFF" << endl;
	}

	input.close();
	output.close();
	return 0;
}