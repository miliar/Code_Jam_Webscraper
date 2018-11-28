#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>

using namespace std; /* Use stand name space*/

long long solve(long R, long K, int N, long* g)
{	
    long long total_income = 0;
    long *local_sum =  new long[N];
    int *next = new int[N];
	int j, l;
   
	// Calculate local_sum[0]
	local_sum[0] = 0;
	j = 0;
	while(j< N && local_sum[0] + g[j] <= K)
	{
		local_sum[0] = local_sum[0] + g[j]; 
		j++;
	}

	if(j == N)
	{
		j = 0;
	}
	next[0] = j;

	for(int i=1; i<N; i++)
	{	
		local_sum[i] = local_sum[i-1] - g[i-1];

			if(j == N)
			{
					j = 0;
			}

		while(local_sum[i] + g[j] <= K)
		{
			local_sum[i] = local_sum[i] + g[j]; 
			j++;

			if(j == N)
			{
				j = 0;
			}
			if(j == i)
			{
				break;
			}
		}
		next[i] = j;
	}

    l = 0;
	for(int i=0; i<R; i++)
	{	
		total_income = total_income + local_sum[l]; 
		l = next[l];
	}

	delete[] local_sum;
	delete[] next;

	return total_income;
}

int main(int argc, char** args)
{
		long long result;
		int T; /* Number of test cases */
		long R; /* Number of runs */
		long K; /* Capacity */
		int N; /* Number of groups */
	    long* g; 
		

	 /* Initialize input and output file */ 
		fstream input_file("C-large.in", ios_base::in);
		fstream output_file("output.txt", ios_base::out);
		if(!input_file.is_open() || !output_file.is_open())
		{
				cout << "Unalbe to open file!" << endl;
				return 1;
		}
 
	/* Read the number of test cases*/
		input_file >> T;
//		cout << "The number of test cases is " << T << endl << endl;

   /* For each test case, load variables*/
		for(int i=0; i<T; i++)
		{
//        cout << "Test case: " << i+1 << endl;

			input_file >> R;
			input_file >> K;
		    input_file >> N;

//cout << "Number R, K, N is: " << R << ", "<< K<< ", "<< N << endl;

			g = new long[N];

			for(int i=0; i<N; i++)
			{
				input_file >> g[i] ;
			}

			result = solve(R, K, N, g);

			delete[] g;

// cout << "Case #" << i +1<< ":	" << result << endl<<endl;
output_file << "Case #" << i+1 << ":	" << result << endl;
		}

}