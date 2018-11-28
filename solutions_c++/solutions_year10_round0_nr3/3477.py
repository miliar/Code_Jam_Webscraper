//#include <stdio.h>
//#include <tchar.h>

/*
Input
  	
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Output

Case #1: 21
Case #2: 100
Case #3: 20

*/
/*
The first line of the input gives the number of test cases, T. T test cases follow, 
with each test case consisting of two lines. The first line contains three space-separated 
integers: R, k and N. The second line contains N space-separated integers gi, each of 
which is the size of a group that wants to ride. g0 is the size of the first group, g1 
is the size of the second group, etc. 

3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
#include <fstream>
#include <iostream>

int main(int argc, char* argv[])
{
	std::fstream input("small.txt", std::ios::in);

	int cases = 0; input >> cases;

	//printf("->%d cases.\n", cases);
	std::fstream output("output.txt", std::ios::out);

	for(int i=0; i<cases; i++)
	{
		int R,k,N = 0;
		input >> R;
		input >> k;
		input >> N;

		//printf("-->R: %d.\n", R); // number of times RC will run
		//printf("-->k: %d.\n", k); // RC people limit
		//printf("-->N: %d.\n", N);

		int* groups = new int[N];
		//printf("--->");
		for(int j=0; j<N; j++)
		{
			input >> groups[j];
			//printf("%d ", groups[j]);
		}
		//printf("\n");

		int* gPointer = groups;
		int* gLast = &groups[N-1];

		int totalProfit = 0;

		for(int j=0; j<R; j++)
		{
			int currentProfit = 0;
			int slots = k;
			int queueSize = N;

			while(slots >= *gPointer && queueSize > 0)
			{
				slots -= *gPointer;

				currentProfit += *gPointer;
				
				queueSize--;
				if(gPointer < gLast)
				{
					gPointer++;
				}
				else
				{
					gPointer = groups;
				}
			}

			//printf("----->Profit: %d\n", currentProfit);

			totalProfit += currentProfit;
		}

		//printf("------>Total Profit: %d\n", totalProfit);
		printf("Case #%d: %d\n", (i+1), totalProfit);
		output << "Case #" << (i+1) << ": " << totalProfit << "\n";
	}

	getchar();

	return 0;
}