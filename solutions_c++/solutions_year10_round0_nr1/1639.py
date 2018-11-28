#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>

using namespace std; /* Use stand name space*/

char* solve(int N, long K)
{	
	  long i=0;

	  for(; i<N; i++)
	  {
			if((K & 1) == 0)
			{
				 return "OFF";
			}
			else
			{
				 K = K >> 1;
			}
	  }

	return "ON";
}

int main(int argc, char** args)
{
		char* result;
		int T; /* Number of test cases */
		int N; /* Number of snappers */
		long K; /* Number of finger snaps */

	 /* Initialize input and output file */ 
		fstream input_file("A-large.in", ios_base::in);
		fstream output_file("output.txt", ios_base::out);
		if(!input_file.is_open() || !output_file.is_open())
		{
				cout << "Unalbe to open file!" << endl;
				return 1;
		}
 
	/* Read the number of test cases*/
		input_file >> T;
		cout << "The number of test cases is " << T << endl;

   /* For each test case, load variables*/
		for(int i=0; i<T; i++)
		{
// cout << "Test case: " << i+1 << endl;

			input_file >> N;
			input_file >> K;

// cout << endl << "Number N, K is: " << N << ", "<< K<< endl <<endl;

			result = solve(N, K);

// cout << "Case #" << i +1<< ":	" << result << endl<<endl<<endl;
output_file << "Case #" << i+1 << ":	" << result << endl;
		}

}