#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
	ifstream input ("A-small.in", ios::in);
	int T = 0;
	if (input.is_open())
	{
		input >> T;
		for (int i = 0; i < T; ++i)
		{
			int N, K;
			input >> N;
			input >> K;
			
			int j;
			for (j = 0; j < N; ++j, K = K >> 1) if (!(K & 1)) break;
			cout << "Case #" << (i+1) << ": " << (j == N ? "ON" : "OFF") << endl;
		}
	}
	return 0;
}
