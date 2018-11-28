#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("out.txt");
	int count, num; 
	int pile[1000];
	int can;

	fin >> count;
	
	for(int i = 0; i < count; i++)
	{
		fin >> num;
		for(int j = 0; j < num; j++)
		{
			fin >> pile[j];
			if(j == 0) can = pile[j];
			else can ^= pile[j];
		}

		if(can == 0)
		{
			int min = pile[0];
			int sum = pile[0];
			for(int j = 1; j < num; j++)
			{
				if(pile[j] < min) min = pile[j];
				sum += pile[j];
			}
			fout << "Case #" << i + 1 << ": " << sum - min <<"\n";
		}
		else fout << "Case #" << i + 1 << ": NO\n";
	}
	return 0;
}