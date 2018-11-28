#include<iostream>
#include<fstream>
using namespace std;

// #define input cin
// #define output cout

ifstream input("C-large.in");
ofstream output("C-largeout.txt");

int candy[1024];
int T, N, C;

int main()
{
	input >> T;
	for(int count = 0; count < T; count++)
	{
		input >> N;
		int minimum = 10000000;
		int xorsum = 0;
		int sum = 0;
		for(int i = 0; i < N; i++)
		{
			input >> candy[i];
			if(candy[i] < minimum)
				minimum = candy[i];
			xorsum = xorsum ^ candy[i];
			sum = sum + candy[i];
		}
		if(xorsum == 0)
		{
			output << "Case #" << count+1 << ": " << sum - minimum << endl;
		}
		else
		{
			output << "Case #" << count+1 << ": " << "NO" << endl;
		}
	}
	return 0;
}