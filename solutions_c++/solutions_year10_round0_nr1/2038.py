// SnapperChain.cpp : Defines the entry point for the console application.
//

#include <fstream>

#define MAX_SNAPPER		50

unsigned int MinCounts[MAX_SNAPPER + 1] = {0};

void FillMinSnapCounts()
{
	unsigned int res = 0;

	for (unsigned int i = 1; i <= MAX_SNAPPER; ++i)
	{
		res = res * 2 + 1;
		MinCounts[i] = res;
	}
}

bool IfLigths(unsigned int n, unsigned int k)
{
	if ( (k == 0) || (n == 0) || (n > MAX_SNAPPER) )
	{
		return false;
	}

	if (k < MinCounts[n])
	{
		return false;
	}

	return ((k + 1) % (MinCounts[n] + 1)) == 0;
}

int main(int argc, char * argv[])
{
	FillMinSnapCounts();

	unsigned int t = 0;

	std::ifstream fIn("A-large.in");
	fIn >> t;

	std::ofstream fOut("A-large.out");

	for (unsigned int i = 0; i < t; ++i)
	{
		unsigned int n = 0, k = 0;
		fIn >> n >> k;

		fOut << "Case #" << i + 1 << ": " << (IfLigths(n, k) ? "ON" : "OFF") << std::endl;
		fOut.flush();
	}

	fOut.close();
	fIn.close();
	
	return 0;
}

