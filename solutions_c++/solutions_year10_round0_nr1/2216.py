#include <iostream>
#include <fstream>
#include <cmath>

bool solve(int a, int b)
{
	return ((b+1)%(1<<a) == 0);
}

int main(int argc, char **argv)
{
	char *filein, *fileout;
	if (argc < 3)
	{
		filein = "test.in";
		fileout = "test.out";
	}
	else
	{
		filein = argv[1];
		fileout = argv[2];
	}
	std::ifstream infile(filein);
	std::ofstream outfile(fileout);
	int numtrials;
	infile >> numtrials;
	for (int i = 1; i <= numtrials; ++i)
	{
		int a,b;
		infile >> a >> b;
		if (solve(a,b))
			outfile << "Case #" << i << ": ON" << std::endl;
		else
			outfile << "Case #" << i << ": OFF" << std::endl;
	} 
}
