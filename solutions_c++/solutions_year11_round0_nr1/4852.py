#include <iostream>
#include <fstream>
#include <stack>

using namespace std;

int alzero (int val)
{
	return val<0?0:val;
}

int main(int argc, char* argv[])
{
	int total, orange, blue, pos;
	int oPos, bPos;
	char current, last;

	fstream fin = fstream("A-large.in");
	ofstream output;
	output.open("output.txt");

	int cases;

	fin >> cases;

	int instructions;

	for (int i = 0; i < cases; i++)
	{
		total = 0;
		orange = 0;
		blue = 0;
		oPos = 1;
		bPos = 1;
		last = 'A';
		fin >> instructions;
		for (int j = 0; j < instructions; j ++)
		{
			fin >> current;
			fin >> pos;
			if ( current == 'B') 
			{
				if ( last == 'O' )
				{
					 blue = alzero( abs(bPos - pos) - orange) + 1;
					 total += orange;
					 orange = 0;
				}
				else 
				{
					blue += abs(bPos - pos) + 1;
				}
				bPos = pos;
			}
			else
			{
				if (last == 'B')
				{
					orange = alzero( abs(oPos - pos) - blue) + 1;
					total += blue;
					blue = 0;
				}
				else
				{
					orange += abs(oPos - pos) + 1;
				}
				oPos = pos;
			}
			last = current;
		}
		total = total + blue + orange;
		output << "Case #" << (i + 1) << ": " << total << endl;
	}
}