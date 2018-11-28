#include <iostream>
#include <fstream>

bool snappercheck(int n, int k)
{
	int mask = 0xffffffff >> (32 - n);
	return (mask & k) == mask;
}

int main(int argc, char* argv[])
{
	std::ifstream input;
	input.open(argv[1]);

	int num_cases;
	input >> num_cases;

	int i = 1;
	while(num_cases--)
	{
		int n,k;
		input >> n;
		input >> k;

		std::cout << 
			"Case #" << 
			i++ << ": ";
			
		snappercheck(n,k)? std::cout << "ON":
								 std::cout << "OFF";

		std::cout << std::endl;
	}
	return 0;
}
