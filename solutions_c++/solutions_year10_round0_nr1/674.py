
#include <fstream>
#include <iostream>

using namespace std;

size_t minimum(size_t n)
{
	if (n == 1) 
	{	
		return 1;
	}
	else
	{
		return (minimum(n - 1) * 2 + 1);
	}	
}

bool snapper(size_t n, size_t k)
{
	// Calculate the minimum number of snap to light a bulb
	size_t m = minimum(n);	

	// Check if k is enough to light a bulb
	size_t q = (k + 1) / (m + 1);

	return (((m + 1) * q) == (k + 1)) ? true : false;
}

int main(int argc, char** argv) 
{
	size_t t, n, k;

	std::ifstream fin("A-large.in");
	std::ofstream fout("A-large.out");
	
	fin >> t;
	for (size_t i = 0; i < t; ++i)
	{
		fin >> n >> k;
		
		if (n == 0)
		{
			fout << "Case #" << (i + 1) << ": OFF" << std::endl;
			continue ;
		}

		if (snapper(n, k))
		{
			fout << "Case #" << (i + 1) << ": ON" << std::endl;
		}
		else
		{
			fout << "Case #" << (i + 1) << ": OFF" << std::endl;
		}
	}

	fin.close();
	fout.close();

    return (0);
}

