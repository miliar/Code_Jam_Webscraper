#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

int main ()
{
	int t;

	lettura >> t;

	for (int i = 1; i <= t; i += 1)
	{
		int n;

		lettura >> n;

		int pos_a = 1;
		int tim_a = 0;
		int pos_b = 1;
		int tim_b = 0;

		for (int j = 0; j < n; j += 1)
		{
			char robot;
			int n_pos;

			lettura >> robot >> n_pos;

			if (robot == 'O')
			{
				tim_a = max (tim_a + abs(n_pos - pos_a), tim_b) + 1;
				pos_a = n_pos;
			}
			else
			{
				tim_b = max (tim_b + abs(n_pos - pos_b), tim_a) + 1;
				pos_b = n_pos;
			}
		}

		scrittura << "Case #" << i << ": " << max (tim_a, tim_b) << endl;
	}
}
