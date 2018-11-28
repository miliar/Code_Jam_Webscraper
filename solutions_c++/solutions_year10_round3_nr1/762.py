#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>

using namespace std; /* Use stand name space*/

 
int solve(int N, int *A, int *B)
{	
	int count = 0;

	for(int i=0; i<N; i++)
	{
		for(int j=1; j<N; j++)
		{
			if(((A[i] < A[j]) && (B[i] > B[j]))||
				((A[i] > A[j]) && (B[i] < B[j]))
				) 
			{
					count++;
			}
		}
	}

	return count;
}

int main(int argc, char** args)
{
		int result;
		int T; /* Number of test cases */
		int N; /* Number of lines */
		int* A;
		int* B;

	 /* Initialize input and output file */ 
		fstream input_file("A-small-attempt1.in", ios_base::in);
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
		
			A = new int[N];
			B = new int[N];

            for(int i=0; i<N; i++)
			{
					input_file >> A[i] ;
					input_file >> B[i];
			}

//cout << endl << "Number N is: " << N << endl;

//            for(int i=0; i<N; i++)
//			{
//cout << endl << "A = : " << A[i] ;
//cout << endl << "B = : " << B[i] << endl;
//			}


			result = solve(N, A, B);

//			cout << " The result is: "  <<  result << endl;

			delete[] A;
			delete[] B;

cout << "Case #" << i +1<< ":	" << result << endl<<endl<<endl;
output_file << "Case #" << i+1 << ":	" << result << endl;
		}

}