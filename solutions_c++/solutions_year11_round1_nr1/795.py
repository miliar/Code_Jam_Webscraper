// Round 1A 2011

#include "stdafx.h"
#include <algorithm>
#include <stdio.h>
#include <vector>
#include "assert.h"
#include <hash_map>

using namespace std;

namespace CodeJam
{

class InputReader
{
public:
	InputReader(const char* inputFile);
	~InputReader();

	// Reads a line that contains a single integer and return the value.
	int ReadIntLine();

	// Reads a new line from file into m_line.
	// Returns true for success and false if no more line.
	bool ReadLine();

	// Reads an integer from m_p.
	// Returns the value of the integer if exists or -1 if no more.
	int ReadInt();

	__int64 ReadInt64();

private:
	void SkipSpace();
	FILE * m_fp;
	static const int c_maxLineLen = 100 * 1024;
	char m_line[c_maxLineLen];  // current line read.
	char* m_p;  // pointer to current character in the line.

	InputReader(const InputReader&);
	void operator=(const InputReader&);
};

InputReader::InputReader(const char* inputFile)
{
	m_fp = NULL;
	fopen_s(&m_fp, inputFile, "r");
	assert(m_fp != NULL);
}

InputReader::~InputReader()
{
	fclose(m_fp);
}

int InputReader::ReadIntLine()
{
	ReadLine();
	return ReadInt();
}

bool InputReader::ReadLine()
{
	memset(m_line, 0, c_maxLineLen);
	m_p = m_line;
	return fgets(m_line, c_maxLineLen, m_fp) != NULL;
}

int InputReader::ReadInt()
{
	SkipSpace();
	// Returns -1 to indicate no more data.
	if (*m_p == 0)
	{
		return -1;
	}
	int value = 0;
	while (*m_p >= '0' && *m_p <= '9')
	{
		value = value * 10 + (*m_p - '0');
		m_p++;
	}
	// printf("%d\n", value);
	return value;
}

__int64 InputReader::ReadInt64()
{
	SkipSpace();
	// Returns -1 to indicate no more data.
	if (*m_p == 0)
	{
		return -1;
	}
	__int64 value = 0;
	while (*m_p >= '0' && *m_p <= '9')
	{
		value = value * 10 + (*m_p - '0');
		m_p++;
	}
	return value;
}

void InputReader::SkipSpace()
{
	while (*m_p == ' ' || *m_p == '\r' || *m_p == '\n' || *m_p == '\t') m_p++;
}

// A single TestCase
class TestCase
{
public:
    TestCase(InputReader& reader);
	~TestCase();
	void Solve();
	void ShowInput() const;
	void ShowOutput(int caseNum) const;
private:
	__int64 m_N;
	int m_PD;
	int m_PG;
	int m_today;
	int m_global;
	bool m_possible;

	TestCase(const TestCase&);
	void operator=(const TestCase&);
};

// All test cases
class TestSet
{
public:
    TestSet(const char* inputFile);
	~TestSet();
	void SolveAll();
	void ShowInput() const;
	void ShowOutput() const;
private:
	// max possible number of test cases.
	static const int c_maxT = 2000;
	int m_T;  // number of test cases
	TestCase* m_cases[c_maxT];

	InputReader* m_reader;

	TestSet(const TestSet&);
	void operator=(const TestSet&);
};

TestCase::TestCase(InputReader& reader)
{
	reader.ReadLine();
	m_N = reader.ReadInt64();
	m_PD = reader.ReadInt();
	m_PG = reader.ReadInt();
	assert(m_N > 0 && m_PD >= 0 && m_PG >= 0);
	m_possible = false;
}

TestCase::~TestCase()
{
}

void TestCase::ShowInput() const
{
	printf("%lld %d %d\n", m_N, m_PD, m_PG);
}

void TestCase::ShowOutput(int caseNum) const
{
	printf("Case #%d: %s\n", caseNum, m_possible? "Possible" : "Broken");
}

void Reduce(int* upper, int* lower)
{
	// 76% reduce to 19/25
	if (*upper % 2 == 0)
	{
		*upper /= 2;
		*lower /= 2;
	}
	if (*upper % 2 == 0)
	{
		*upper /= 2;
		*lower /= 2;
	}
	if (*upper % 5 == 0)
	{
		*upper /= 5;
		*lower /= 5;
	}
	if (*upper % 5 == 0)
	{
		*upper /= 5;
		*lower /= 5;
	}
}

static int g_multiples[9] = {1, 2, 4, 5, 10, 20, 25, 50, 100};

void Map(int upper, int lower, int N, vector<int>& uppers, vector<int>& lowers)
{
	assert(upper <= lower);
    for (int i = 0; i < 9; i++)
	{
		if (g_multiples[i] * lower > 100) break;
		uppers.push_back(upper * g_multiples[i]);
		lowers.push_back(lower * g_multiples[i]);
	}
}


void TestCase::Solve()
{
	m_possible = false;
	if (m_PG == 100 && m_PD < 100) return;  // impossible
	if (m_PD > 0 && m_PG == 0) return;  // impossible
	// 76% reduce to 19/25
	int upper = m_PD;
	int lower = 100;
	Reduce(&upper, &lower);
	// if 19/25 and today played <= 23, impossible
	if (lower > m_N) return;
    // Now it is always possible?
	m_possible = true;
}

TestSet::TestSet(const char* inputFile)
{
	for (int i = 0; i < c_maxT; i++) m_cases[i] = NULL;
	m_reader = new InputReader(inputFile);
	m_T = m_reader->ReadIntLine();
	assert(m_T >= 1 && m_T <= c_maxT);
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i] = new TestCase(*m_reader);
	}
	ShowInput();
}

TestSet::~TestSet()
{
	delete m_reader;
	for (int i = 0; i < m_T; i++)
	{
		delete m_cases[i];
	}
}

void TestSet::SolveAll()
{
	for (int i = 0; i < m_T; i++)
	{
		printf("Case %d\n", i + 1);
		m_cases[i]->ShowInput();
		m_cases[i]->Solve();
		m_cases[i]->ShowOutput(i + 1);
	}
	printf("Final output:\n");
	ShowOutput();
}

void TestSet::ShowInput() const
{
	printf("%d\n", m_T);
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i]->ShowInput();
	}
}

void TestSet::ShowOutput() const
{
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i]->ShowOutput(i + 1);
	}
}
}  // end namespace

using namespace CodeJam;
int main(int argc, char* argv[])
{
	const char c_sampleInput[] = 
		"C:\\CodeJam\\Round1A2011\\A-large.in";
	TestSet cases(c_sampleInput);
	cases.SolveAll();
	
	return 0;
}