#include <iostream>
#include <fstream>
using namespace std;

bool isLightOn(unsigned int n, unsigned int k)
{
	unsigned int snapBits = 0;
	
	for (int i = 0; i < k; i++)
	{
		snapBits++;
	}
	
	for (int i = 0; i < n; i++)
	{
		if (((snapBits >> i) & 1) != 1)
			return false;
	}
	
	return true;
}

int main(int argc, char **argv)
{
	int caseCount;
	int n, k;
	bool result;
	
	ifstream input(argv[1]);
	ofstream output(argv[2]);
	
	input >> caseCount;
	
	for (int i = 0; i < caseCount; i++)
	{
		//cout << i+1 << endl;
		input >> n >> k;
		result = isLightOn(n, k);
		output << "Case #" << i+1 << ": ";
		if (result)
			output << "ON" << endl;
		else
			output << "OFF" << endl;
	}
	
	input.close();
	output.close();

	return 0;
}
