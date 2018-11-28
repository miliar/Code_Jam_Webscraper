//#include "sort.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
//////////////////////////////////////////////////////////////
// declarations
class TestCase {
public :
	// for printing case id
	int id;

	// add member data
	int count;
	std::vector<int> x;
	std::vector<int> y;
public:
	TestCase(int i) : id(i) {}

	friend std::istream& operator>>(std::istream& input, TestCase& testCase);
};

void load(const char* fileName, std::vector<TestCase*>& testCases);

//////////////////////////////////////////////////////////////
// definition
std::ofstream output;

//////////////////////////////////////////////////////////////
// PROCESS
void process(TestCase* instance)
{
	
	int value = 0;
	
	for (int i = 0, j = instance->count - 1; i < instance->count; ++i, --j)
	{
		value += instance->x[i] * instance->y[j];
	}

	// PRINT RESULT
	output << "Case #" << instance->id << ": ";
	output << value;
	output << std::endl;
}

//////////////////////////////////////////////////////////////
// MAIN
int main(int argc, char* argv[])
{
	std::vector<TestCase*> testCases;

	if (argc < 2) return 0;
	load(argv[1], testCases);

	//sort(testCase->dataset);

	output.open("output.txt", std::ios::binary);
	for_each(testCases.begin(), testCases.end(), process);

	output.close();
}

//////////////////////////////////////////////////////////////
// DATA LOAD
void load(const char* fileName, std::vector<TestCase*>& testCases)
{
	std::ifstream input(fileName, std::ios::binary);

	int testCount = 0;
	char buff[256];

	// get testcase count
	input.getline(buff, 256);
	testCount = atoi(buff);
	testCases.resize(testCount);

	TestCase* aTestCase;
	
	for (int i = 0; i < testCount; ++i)
	{
		aTestCase = new TestCase(i + 1);

		input >> *aTestCase;

		testCases[i] = aTestCase;
	}
	
	input.close();
}

inline std::istream& operator>>(std::istream& input, TestCase& testCase)
{
	// READ DATA
	int datacount = 0;

	// READ TESTCASE
	int size = 1024 * 1024 * 1024;
	static char* buff = new char[size];


	int num_integers;
	input.getline(buff, size);
	num_integers = atoi(buff);

	input.getline(buff, size);
	std::istringstream ins;
	ins.str(buff);
	int a;
	
	testCase.count = num_integers;
	for (int i = 0; i < num_integers; ++i)
	{
			ins >> a;

			testCase.x.push_back(a);

	}

	input.getline(buff, size);
	std::istringstream ins2;
	ins2.str(buff);
	for (int i = 0; i < num_integers; ++i)
	{
			ins2 >> a;

			testCase.y.push_back(a);
	}
	
	std::sort(testCase.x.begin(), testCase.x.end());
	std::sort(testCase.y.begin(), testCase.y.end());
	
	//delete [] buff;

	return input;
}

