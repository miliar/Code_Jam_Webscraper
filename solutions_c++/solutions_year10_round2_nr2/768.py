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

	int i,j,k,l;

	unsigned long long int B;
	int N, K, C;

	unsigned long long int final[50];
	unsigned long long int loc, speed, swap, slow;

	bool done;
	int count;

	// Fill array and print	
	for (i = 1; i <= T; i++)
	{
		done = false; count = 0; swap = 0; slow = 0;
		input >> N >> K >> B >> C;
		
		
		for (j = 0; j < N; j++)
		{
			input >> loc;

			final[j] = loc;
		}

		for (k = 0; k < N; k++)
		{
			input >> speed;

			final[k] = final[k] + speed*C;
		}

		if (K == 0)
			done = true;
		else
		{
			for (l = N-1; l >= 0; l--)
			{
				if (final[l] >= B)
				{
					count++;
					swap += slow;
				}
				else
					slow++;

				if (count == K)
				{
					done = true;
					break;
				}
			}
		}
		
		if (done)
			output << "Case #" << i << ": " << swap << endl;
		else
			output << "Case #" << i << ": IMPOSSIBLE" << endl;
	}

	input.close();
	output.close();
	return 0;
}