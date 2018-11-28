#include <iostream>
#include <fstream>
#include <math.h>


bool checkIfOn(unsigned long long nbSnappers, unsigned long long nbClicks)
{
	for (int k = 1; k <= nbSnappers; k++)
	{
		int res = (nbClicks % static_cast<unsigned long long int>(powf(2.f, k))) / static_cast<unsigned long long int>(powf(2.f, k - 1));
		if (res == 0)
			return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	std::ifstream input(argv[1]);

	int T_nbCases;

	input >> T_nbCases;

	for (int iter_case = 1; iter_case <= T_nbCases; iter_case++)
	{
		unsigned long long int N_nbSnappers = 0;
		unsigned long long int K_nbClicks = 0;

		input >> N_nbSnappers;
		input >> K_nbClicks;

		bool res = checkIfOn(N_nbSnappers, K_nbClicks);

		std::cout << "Case #" << iter_case << ": " << (res ? "ON" : "OFF") << std::endl;		
	}
}
