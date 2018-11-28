#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

std::ifstream input;
std::ofstream output;

void TestCase(int testCase);

int main()
{
	input.open("A-small-attempt0.in");
	output.open("output.txt", std::ios_base::trunc);

	int numTestCases = 0;
	input >> numTestCases;
	input.ignore(INT_MAX, '\n');
	for(int i=0; i<numTestCases; ++i)
	{
		TestCase(i + 1);
	}

	output.close();
	input.close();

	return 0;
}

bool IsHappy(int n, int base)
{
	std::set<int> used;
	
	int curr = n;
	for(;;)
	{
		if(curr == 1)
			return true;

		used.insert(curr);

		int temp = curr;
		curr = 0;
		while(temp > 0)
		{
			curr += (temp%base) * (temp%base);
			temp /= base;
		}

		if(used.find(curr) != used.end())
			return false;
	}
}

void TestCase(int testCase)
{
	std::vector<int> bases;
	{
		std::string buffer;
		std::getline(input, buffer);
		std::stringstream sstream(buffer);

		int temp;
		while(sstream >> temp)
		{
			bases.push_back(temp);
		}
	}

	int current = 2;
	for(;;)
	{
		unsigned int i = 0;
		for(; i<bases.size(); ++i)
		{
			if(IsHappy(current, bases[i]) == false)
				break;
		}
		if(i == bases.size())
			break;

		++current;
	}

	output << "Case #" << testCase << ": " << current << '\n';
}
