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

	unsigned int R, K, N, g;
	unsigned int groups[1000];
	
	unsigned long long int total_final, total_current, total_next;
	unsigned int index_start, index_end;

	// Fill array and print	
	for (i = 1; i <= T; i++)
	{
		input >> R >> K >> N;
		
		total_final = 0; total_current = 0; total_next = 0;
		
		for (j = 0; j < N; j++)
		{
			input >> g;
			groups[j] = g;
		}
		
		index_start = 0;
		index_end = 0;
		total_final = 0;
		
		for (k = 0; k < R; k++)
		{
			total_current = 0;
			
			while(true)
			{
				total_next = total_current + groups[index_end];
				
				if (total_next > K)
					break;
				else
					total_current = total_next;
					
				index_end++;
				
				if (index_end == N)
					index_end = 0;
				
				if (index_end == index_start)
					break;
			}
			
			index_start = index_end;
			total_final += total_current;
		}
		
		output << "Case #" << i << ": " << total_final << endl;
	}

	input.close();
	output.close();
	return 0;
}