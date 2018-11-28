#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void)
{
	int n, g, s, p, count, div, triplet, rem;
	
	ofstream file;
	ifstream in;
	file.open("file.txt"); //open a file
	in.open("input.txt");

	in >> n;

	for (int i = 0; i < n; i++)
	{
		in >> g >> s >> p;
		count = 0;
		for (int t = 0; t < g; t++)
		{
			in >> triplet;
			div = triplet / 3;
			rem = triplet % 3;
			if (div >= p)
			{
				count++;
			}
			else if (div + 1 == p && rem > 0)
			{
				count++;
			}
			else if (div + 2 == p && rem == 2 && s > 0)
			{
				count++;
				s--;
			}
			else if (div > 0 && div + 1 == p && s > 0)
			{
				count++;
				s--;
			}
		}
		file << "Case #" << i + 1 << ": " << count << endl;
	}
	file.close(); 
    return 0;
}