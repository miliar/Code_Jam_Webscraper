#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream input("A-large.in");
ofstream output("A-large.txt");
// #define input cin
// #define output cout

int T, N;

int main()
{
	input >> T;
	int count = 0;
	char ch;
	int pos;
	int oleft = 0;
	int bleft = 0;
	int op = 1;
	int bp = 1;
	int time = 0;
	int turn = 0; //0: O, 1: B

	for(count = 0; count < T; count ++)
	{
		input >> N;
		time = 0;
		oleft = bleft = 0;
		op = bp = 1;
		turn = 0;
		for(int i = 0; i < N; i++)
		{
			input >> ch >> pos;
			if(ch == 'O')
			{
				if(turn == 0)
				{
					bleft = bleft + abs(pos - op) + 1;
					time = time + abs(pos - op) + 1;
					op = pos;
				}
				else
				{
					if(oleft >= abs(pos - op))
					{
						time++;
						bleft = 1;
					}
					else
					{
						time = time + (abs(pos-op)+1-oleft);
						bleft = abs(pos-op)+1-oleft;
					}
					op = pos;
				}
				turn = 0;
			}
			else
			{
				if(turn == 1)
				{
					oleft = oleft + abs(pos - bp) + 1;
					time = time + abs(pos - bp) + 1;
					bp = pos;
				}
				else
				{
					if(bleft >= abs(pos - bp))
					{
						time++;
						oleft = 1;
					}
					else
					{
						time = time + (abs(pos-bp)+1-bleft);
						oleft = abs(pos-bp)+1-bleft;
					}
					bp = pos;
				}
				turn = 1;
			}
		}
		output << "Case #" << count+1 << ": " << time <<endl;
	}
	return 0;
}