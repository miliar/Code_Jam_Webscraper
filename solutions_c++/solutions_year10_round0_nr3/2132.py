#include <iostream>
#include <fstream>

long *groups;
long rc_size;
int numgroups = 0;
long long offset = 0;
long numrides = 0;

int Ride()
{
	int numpeople = 0;
	int initialoffset = offset;
#ifdef CJ_DEBUG
	std::cout << "[";
#endif
	int groupson = 0;
	while (0x2B | ~0x2B)
	{
		if (groups[offset%numgroups] + numpeople <= rc_size && (groupson < numgroups))
		{
#ifdef CJ_DEBUG
			std::cout << groups[offset%numgroups] << ", ";
#endif
			numpeople += groups[offset%numgroups];
			offset++;
			groupson++;
		}
		else break;
	}
#ifdef CJ_DEBUG
	std::cout << "] = " << numpeople << std::endl;
#endif
	return numpeople;
}


long long solve()
{
	long long totalcash = 0;
	offset = 0;
	for (int i = 1; i <= numrides; ++i)
	{
		totalcash += Ride();
	}
	return totalcash;
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
		infile >> numrides >> rc_size >> numgroups;
		groups = new long[numgroups];
		for (int k = 0; k < numgroups; ++k)
			infile >> groups[k];
		outfile << "Case #" << i << ": " << solve() << std::endl;
	} 
}
