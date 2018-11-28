#define INPUT_FILE "C-small-attempt0.in"
#define OUTPUT_FILE "C-small.out"

#include <iostream>
#include <fstream>
#include <cstdlib>

using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;

double roller_coaster(int R, int k, int N, int g[]);


int main(void)
{
	//get input from file
	ifstream infile (INPUT_FILE);
	if (!infile)
	{
		cout << "Cannot open input file!" << endl;
		exit(1);
	}
	ofstream outfile ( OUTPUT_FILE );
	if (!outfile)
	{
		cout << "Cannot open output file!" << endl;
		exit(1);
	}
	
	int T;			//number of cases
	int R, k, N;	// round R, capacity k, and groups N

	infile >> T;

	for (int i = 1; i <= T; i++)
	{
		infile >> R >> k >> N;
		int* g = new int[N];
		for (int j = 0; j < N; j++)
			infile >> g[j];
		outfile << "Case #" << i  << ": " 
	    	 << roller_coaster(R, k, N, g) << endl;
		delete [] g;
	}
	return 0;
}
		
double roller_coaster(int R, int k, int N, int g[])
{
	// test edge case, in which total number of people is no larger than
	// capacity k
	bool queue = false;
	int sum_g = 0;
	for (int i = 0; i< N; i++)
	{
		sum_g += g[i];
		if (sum_g > k)
		{
			queue = true;
			break;
		}
	}

	if (queue == false)
		return static_cast<double>(sum_g) * R;
			
	// there is a queue,  preprocessing the queue
//	int p[N];		// p[i] is num of people that fit in k if starting group i
//	int g_next[N]; 		// next group 
	int* p = new int[N];
	int* g_next = new int[N];
	for (int i=0; i<N; i++)
	{
		p[i] = 0;
		int j = i;  // pointer to next group
		while ( (p[i] += g[j] ) <= k )
		{
			j++;
			if (j == N)
				j = 0;
		}

		p[i] -= g[j];
		g_next[i] = j;
		//cout << i << '\t' << p[i] << '\t' << g_next [i] << endl;
	}

	int next_group = 0;
	double total = 0.0;

	for (int i = 0; i< R; i++)
	{
		total +=  p[next_group];
		next_group = g_next[next_group];
	}

	delete [] p;
	delete [] g_next;
	return total;
}
