#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

//const std::string FILE_NAME = "test";
//const std::string FILE_NAME = "A-small-attempt0";
const std::string FILE_NAME = "A-large";
const std::string FILE_NAME_IN = FILE_NAME + ".in";
const std::string FILE_NAME_OUT = FILE_NAME + ".out";

const int GRID_SIZE = 4;

struct TestCase
{
	char grid[GRID_SIZE][GRID_SIZE];

	std::string toString() const;
};

void executeTest(const TestCase& testCase, std::ofstream& fout);
void executeTests(const std::vector<TestCase>& testCases);
TestCase readTestCase(std::ifstream& fin);
std::vector<TestCase> readTestCases();

int main()
{
	auto tests = readTestCases();
	executeTests(tests);

	return 0;
}

void executeTest(const TestCase& test, std::ofstream& fout)
{
	static int number = 1;
	std::cout << "Executing test case " << number << ": ";
	auto result = test.toString();
	std::cout << result << std::endl;
	fout << "Case #" << number++ << ": " << result << std::endl;
}

void executeTests(const std::vector<TestCase>& tests)
{
	std::ofstream fout(FILE_NAME_OUT);
	std::for_each(tests.begin(), tests.end(), [&](const TestCase& test) { executeTest(test, fout); });
	fout.flush();
	fout.close();
}

TestCase readTestCase(std::ifstream& fin)
{
	TestCase test;

	for (int i = 0; i < GRID_SIZE; i++)
	{
		std::string line;
		fin >> line;
		
		for (int j = 0; j < GRID_SIZE; j++)
			test.grid[i][j] = line[j];
	}

	return test;
}

std::vector<TestCase> readTestCases()
{
	std::vector<TestCase> cases;
	std::ifstream fin(FILE_NAME_IN);

	int caseCount = 0;
	fin >> caseCount;
	std::cout << "Reading in " << caseCount << " test cases.\n";

	std::generate_n(std::back_inserter(cases), caseCount, [&] { return readTestCase(fin); });
	
	fin.close();

	return cases;
}

std::string gridWinnerString(char c)
{
	switch(c)
	{
	case 'O': return "O won";
	case 'T': return "Draw";
	case 'X': return "X won";
	default: return "Game has not completed";
	}
}

std::string TestCase::toString() const
{
	char* wild = nullptr;

	auto copy = *this;


	for (int row = 0; row < GRID_SIZE; row++)
	{
		for (int col = 0; col < GRID_SIZE; col++)
		{
			char p = copy.grid[row][col];
			if (p == 'T')
			{
				wild = &copy.grid[row][col];
				copy.grid[row][col] = 'O';
				break;
			}
		}
		if (wild)
			break;
	}

	char first, won;
	for (int pass = 0; pass < 2; pass++)
	{
		for (int row = 0; row < GRID_SIZE; row++)
		{
			first = won = copy.grid[row][0];
			for (int col = 1; col < GRID_SIZE; col++)
			{
				auto p = copy.grid[row][col];
				if (p != first || p == '.')
				{
					won = '.';
					break;
				}
			}
			if (won != '.')
				return gridWinnerString(won);
		}

		for (int col = 0; col < GRID_SIZE; col++)
		{
			first = won = copy.grid[0][col];
			for (int row = 1; row < GRID_SIZE; row++)
			{
				auto p = copy.grid[row][col];
				if (p != first || p == '.')
				{
					won = '.';
					break;
				}
			}
			if (won != '.')
				return gridWinnerString(won);
		}

		first = won = copy.grid[0][0];
		for (int i = 1; i < GRID_SIZE; i++)
		{
			auto p = copy.grid[i][i];
			if (p != first || p == '.')
			{
				won = '.';
				break;
			}
		}
		if (won != '.')
			return gridWinnerString(won);

		first = won = copy.grid[0][GRID_SIZE - 1];
		for (int i = 1; i < GRID_SIZE; i++)
		{
			auto p = copy.grid[i][GRID_SIZE - i - 1];
			if (p != first || p == '.')
			{
				won = '.';
				break;
			}
		}
		if (won != '.')
			return gridWinnerString(won);

		if (!wild)
			break;
		*wild = 'X';
	}

	for (int row = 0; row < GRID_SIZE; row++)
		for (int col = 0; col < GRID_SIZE; col++)
			if (grid[row][col] == '.')
				return gridWinnerString('.');

	return gridWinnerString('T');
}
