#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>

std::ifstream input;
std::ofstream output;

void TestCase(int testCase);

int main()
{
	input.open("C-small-attempt0.in");
	output.open("output.txt", std::ios_base::trunc);
	if(input.is_open() == false || output.is_open() == false)
		return 0;
	
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

void FindMsg(std::string::const_iterator msgIter, std::string::const_iterator msgEnd, std::string::const_iterator strIter, std::string::const_iterator strEnd, int &numWelcomes)
{
	if(msgIter == msgEnd)
	{
		numWelcomes = (numWelcomes + 1)%10000;
		return;
	}

	while(strIter != strEnd)
	{
		if(*msgIter == *strIter)
		{
			FindMsg(msgIter + 1, msgEnd, strIter, strEnd, numWelcomes);
		}

		++strIter;
	}
}

void TestCase(int testCase)
{
	const std::string targetMsg = "welcome to code jam";

	int numWelcomes = 0;
	std::string msg;
	std::getline(input, msg);

	FindMsg(targetMsg.begin(), targetMsg.end(), msg.begin(), msg.end(), numWelcomes);

	output << "Case #" <<  testCase << ": " << std::setw(4) << std::setfill('0') << numWelcomes << '\n';
}
